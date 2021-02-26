import sys
from sqlalchemy.orm import Session
from citygml2osi.main import connect_to_database, query_database, Coordinate, convert_gt_to_osi_sensor_view
from osi3test import *


class HelperOSIViewer:
    # Helper class to manage the OSI viewer
    """ 
    OSIViewer Settings

    xsize, ysize            Set window size, unit: pixels
    showGrid                False: hide grid layout of OSIViewer; default: True
    userModelPath           Set path to folder with custom 3d models, format: /c/Users/name/osi_models
    landscapeFileName       Set filename of custom environment model located in userModelPath folder,
                            requires userModelPath
    sensorConeFileName      Set filename of custom sensor cone 3d model located in userModelPath folder,
                            requires userModelPath,
                            overwrites coneHorizontalFov, coneVerticalFov, coneRadius
    coneHorizontalFov       Specified horizontal sensor field of view, FOR VISUALIZATION ONLY, unit: deg
    coneVerticalFov         Specified vertical sensor field of view, FOR VISUALIZATION ONLY, unit: deg
    coneRadius              Specified sensor range, FOR VISUALIZATION ONLY, unit: m

    """

   
    def __init__(self, session: Session, start: float = 0.0, stop: float = 120.0, step: float = 0.0020, origin: Coordinate = Coordinate(x=678000, y=5403000, z=400), position: Coordinate = Coordinate(x=4130, y=-1220, z=414)) -> None:
        self.start: float = start
        self.stop: float = stop
        self.step: float = step

        self.origin: Coordinate = origin
        self.position: Coordinate = position
        self.buffer_radius: int = 50

        self.ego_id: int = 14
        
        self.session: Session = session
        self.osi_viewer: Viewer = Viewer(showGrid=True, coneHorizontalFov=90, coneVerticalFov=30, coneRadius=50)
        self.osi_sensor_simulation: SensorSimulation = SensorSimulation()

        # self.runSimulation()

    def runSimulation(self):
        self.simulationStart()
        self.simulationInit()
        time = self.start
        while (time < self.stop):
            next_ = time + self.step
            self.preStep(time, next_)
            #sleep(step)
            time = next_
        self.simulationStop()
        return True

    def collectOutput(self, xtime,step,values):
        return True

    def simulationInit(self):
        return True

    def simulationStart(self):
        # osi_template_source.start(self.start)
        return True

    def simulationStop(self, start,stop,step):
        sys.stdout.flush()
        return True

    def generateSensorView(self, time, nexttime):
        # Time might be used to update postion; TODO use attribute instead of argument
        gt = query_database(self.session, self.origin, self.position, self.buffer_radius)
        view = convert_gt_to_osi_sensor_view(gt)
        #view.groundtruth.timestamp.seconds, sv_ground_truth.timestamp.nanos = seconds, nanos
        currentGT = view.global_ground_truth
        
        sec, ns = int(time), int((time-int(time))*1000000000.0)
        view.timestamp.seconds, view.timestamp.nanos = sec, ns
        currentGT.timestamp.seconds, currentGT.timestamp.nanos = sec, ns
        
        self.add_ego_vehicle(currentGT)

        return view
        

    def preStep(self, time, nexttime):
        # global osi_viewer
        # view = osi_template_source.generateSensorView(time, self.step, nexttime)
        view = self.generateSensorView(time, nexttime)
        view.mounting_position.position.x = 2
        view.mounting_position.position.y = 1
        view.mounting_position.position.z = 1
        view.mounting_position.orientation.yaw = .5

        self.osi_viewer.setInput(view)
        self.osi_viewer.step(time)
        data = self.osi_sensor_simulation.simulate(time, view)
        self.osi_viewer.setOutput(data)

        return True

    def add_ego_vehicle(self, gt) -> int:
        # Hard coded ego vehicle
        veh = gt.moving_object.add()
        veh.id.value = self.ego_id
        veh.type=osi3.osi_object_pb2.MovingObject.TYPE_VEHICLE
        veh.vehicle_classification.type=osi3.osi_object_pb2.MovingObject.VehicleClassification.TYPE_DELIVERY_VAN
        veh.vehicle_classification.light_state.indicator_state=osi3.osi_object_pb2.MovingObject.VehicleClassification.LightState.INDICATOR_STATE_OFF
        veh.vehicle_classification.light_state.brake_light_state=osi3.osi_object_pb2.MovingObject.VehicleClassification.LightState.BRAKE_LIGHT_STATE_OFF
        veh.base.dimension.height=3.0
        veh.base.dimension.width=2.5
        veh.base.dimension.length=8.0
        veh.base.position.x,veh.base.position.y,veh.base.position.z = self.position  # trajectory.getPosition()
        veh.base.position.z = 0 # workaround to check height
        veh.base.position.x -= 8
        veh.base.velocity.x,veh.base.velocity.y,veh.base.velocity.z = 0, 0, 0  #  trajectory.getVelocity()
        veh.base.acceleration.x,veh.base.acceleration.y,veh.base.acceleration.z = 0, 0, 0
        veh.base.orientation.roll,veh.base.orientation.pitch,veh.base.orientation.yaw = 0, 0, 0
        veh.base.orientation_rate.roll,veh.base.orientation_rate.pitch,veh.base.orientation_rate.yaw = 0, 0, 0

        gt.host_vehicle_id.value = self.ego_id

        return 0


def main() -> int:
    print("Hello world")

    """
    SELECT osi."StationaryObject".cityobject_id AS "osi_StationaryObject_cityobject_id", osi."StationaryObject"."Type" AS "osi_StationaryObject_Type", ST_AsEWKB(osi."StationaryObject".basepolygon) AS "osi_StationaryObject_basepolygon", osi."StationaryObject".geometry_rotation_x AS "osi_StationaryObject_geometry_rotation_x", osi."StationaryObject".geometry_rotation_y AS "osi_StationaryObject_geometry_rotation_y", osi."StationaryObject".geometry_rotation_z AS "osi_StationaryObject_geometry_rotation_z", osi."StationaryObject".width AS "osi_StationaryObject_width", osi."StationaryObject".length AS "osi_StationaryObject_length", osi."StationaryObject".height AS "osi_StationaryObject_height", osi."StationaryObject".centroid_x AS "osi_StationaryObject_centroid_x", osi."StationaryObject".centroid_y AS "osi_StationaryObject_centroid_y", osi."StationaryObject".centroid_z AS "osi_StationaryObject_centroid_z", osi."StationaryObject".model_reference AS "osi_StationaryObject_model_reference" 
    FROM osi."StationaryObject" 
    WHERE ST_Contains(ST_Buffer(ST_SRID(ST_GeomFromText(%(ST_GeomFromText_1)s), %(ST_SRID_1)s), %(ST_Buffer_1)s), osi."StationaryObject".basepolygon) AND osi."StationaryObject"."Type" IN (%(Type_1)s, %(Type_2)s, %(Type_3)s, %(Type_4)s)]
    [parameters: {'ST_GeomFromText_1': 'POINT(678130 5403779 414)', 'ST_SRID_1': 32632, 'ST_Buffer_1': 50, 'Type_1': 'BUILDING', 'Type_2': 'WALL', 'Type_3': 'TREE', 'Type_4': 'POLE'}]
    """

    session = connect_to_database(user="postgres", password="changeMe!", host="localhost", port=5432, database="citydb")
    osi_viewer = HelperOSIViewer(session) # , position=Coordinate(678148, 5403733, 0))
    osi_viewer.runSimulation()
    
    print("OSI Viewer is done")

    return 0

if __name__ == "__main__":
    sys.exit(main())
