import sys
from os import environ
import struct
from collections import namedtuple
import typing

from sqlalchemy import create_engine, func as sql_func
from sqlalchemy.orm import sessionmaker, Session

from shapely.geometry import Point

from citydb2osi.groundtruth import GroundTruth as c2o_GroundTruth
from citydb2osi.object import StationaryObject as c2o_StationaryObject
from citydb2osi.trafficlight import TrafficLight as c2o_TrafficLight
from citydb2osi.trafficsign import TrafficSign as c2o_TrafficSign
from citydb2osi.lane import Lane as c2o_Lane, LaneBoundary as c2o_LaneBoundary

from citydb2osi.osidb import StationaryObject as odb_StationaryObject, TrafficSign as odb_TrafficSign, Lane as odb_Lane, LaneBoundary as odb_LaneBoundary

import osi3.osi_sensorview_pb2 as osi_sensorview


Coordinate = namedtuple('Coordinate', ['x', 'y', 'z'])


def connect_to_database(user=environ.get('DATABASE_USER'), password=environ.get('DATABASE_PASSWORD'), host=environ.get('DATABASE_HOST'), port=environ.get('DATABASE_PORT'), database="citydb") -> Session:
    # Tries to connect and return the connection to the DB based on the environement variables
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{database}")
    engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def get_trace_name(osi_type: str = "gt", osi_ver: int = 300, proto_buf_ver: int = 1523,
                   nof_frames: int = 1, scen_name: str = "ingoldstadt", extension: str = "osi") -> str:
    # Returns a meaningful name for the osi trace name
    return f"{osi_type}_{osi_ver}_{proto_buf_ver}_{nof_frames}_{scen_name}.{extension}"


def write_osi_file(gt: c2o_GroundTruth, scen_name: str, seconds: int, nanos: int) -> int:
    # Appends the passed groundtruth to the specified trace file at the corresponding point in time
    # Create the sensorview
    sensorview = osi_sensorview.SensorView()

    # Fill the sensorview
    sv_ground_truth = sensorview.global_ground_truth
    sv_ground_truth.version.version_major, sv_ground_truth.version.version_minor, sv_ground_truth.version.version_patch = 3, 0, 0
    sv_ground_truth.timestamp.seconds, sv_ground_truth.timestamp.nanos = seconds, nanos

    # Write the senorview
    gt.write_pb(sv_ground_truth)
    sb = sensorview.SerializeToString()

    filename = get_trace_name(scen_name=scen_name)
    with open(filename, "ab") as f:
        f.write(struct.pack("<L", len(sb)) + sb)

    return 0

# def translate_centroid(sql_obj: typing.Any, origin: Coordinate) -> typing.Any:
#     sql_obj["centroid_x"] -= origin.x
#     sql_obj["centroid_y"] -= origin.y
#     sql_obj["centroid_z"] -= origin.z
#     
#     return sql_obj

def translate_z(tss: c2o_TrafficSign, z: float = 1.5) -> 'c2o_TrafficSign':
    tss.main_sign.base_stationary.position.z += z
    return tss

def query_database(session: Session, origin: Coordinate, position: Coordinate, buffer_radius: float, srid: int = 32632) -> c2o_GroundTruth:
    pos = sql_func.ST_SetSRID(sql_func.ST_GeomFromText(
        f'POINT({position.x} {position.y} {position.z})'), srid)
    gt = c2o_GroundTruth()

    # Populate StationaryObjects
    st_objs = session.query(odb_StationaryObject).filter(
            sql_func.ST_Contains(sql_func.ST_Buffer(pos, buffer_radius), odb_StationaryObject.basepolygon),
            odb_StationaryObject.Type.in_(["BUILDING", "WALL", "TREE", "POLE"])
        ).all()
    # print(str(session.query(odb_StationaryObject, odb_StationaryObject.centroid_x - origin.x).filter(
    #         sql_func.ST_Contains(sql_func.ST_Buffer(pos, buffer_radius), odb_StationaryObject.basepolygon),
    #         odb_StationaryObject.Type.in_(["BUILDING", "WALL", "TREE", "POLE"]))))
    gt.stationary_objects = list(map(c2o_StationaryObject.from_sql, st_objs))

    # Populate TrafficLights -> not supported 
    # tls = session.query(odb_TrafficLight).filter(sql_func.ST_Contains(
    #    sql_func.ST_Buffer(pos, buffer_radius), odb_TrafficLight.geom)).all()
    #gt.traffic_lights = list(map(c2oc2o_TrafficLight.from_sql, tls))

    # Populate TrafficSigns
    tss = session.query(odb_TrafficSign).filter(
            sql_func.ST_Contains(sql_func.ST_Buffer(pos, buffer_radius), odb_TrafficSign.geom),
            odb_TrafficSign.opendrive_roadSignal_type.in_(['283', '286', '294', '274.2', '274.1']) 
        ).all()
        
    temp = list(map(c2o_TrafficSign.from_sql, tss))
    gt.traffic_signs  = [translate_z(sign, z=1.5) for sign in temp]
    # temp = list(map(c2o_TrafficSign.from_sql, tss))
    # gt.traffic_signs = [x for x in temp 
    # if all(hasattr(x, atr) for atr in ["main_sign", "main_sign.classification", "main_sign.classification.type_"])]
    
    
    # Populate LaneBoundaries -> not perfect until now
    # lbs = session.query(odb_LaneBoundary).filter(sql_func.ST_Contains

    return gt

def convert_gt_to_osi_sensor_view(gt : c2o_GroundTruth) -> osi_sensorview.SensorView:
    sensorview = osi_sensorview.SensorView()

    sv_ground_truth = sensorview.global_ground_truth
    sv_ground_truth.version.version_major, sv_ground_truth.version.version_minor, sv_ground_truth.version.version_patch = 3, 0, 0
    #sv_ground_truth.timestamp.seconds, sv_ground_truth.timestamp.nanos = seconds, nanos
    gt.write_pb(sv_ground_truth)

    return sensorview


def main() -> int:
    session = connect_to_database()
    # x=678154, y=5403779, z=419
    origin = Coordinate(x=4130, y=-1220, z=414)
    position = Coordinate(x=4130, y=-1220, z=414)
    gt = query_database(session, origin, position, 50.0)
    write_osi_file(gt, scen_name="Ingoldstadt-offset", seconds=0, nanos=0)

    return 0


if __name__ == "__main__":
    sys.exit(main())
