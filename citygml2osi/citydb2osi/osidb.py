# coding: utf-8
from sqlalchemy import Column, Float, Integer, MetaData, String, Table
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

from geoalchemy2.shape import to_shape

Base = declarative_base()
metadata = MetaData(schema='osi')



class StationaryObject(Base):
    __tablename__ = 'StationaryObject'
    __table_args__ = {'schema': 'osi'}

    cityobject_id = Column(Integer, primary_key=True)
    Type = Column(String)
    basepolygon = Column(Geometry(from_text='ST_GeomFromEWKT', name='geometry'))
    geometry_rotation_x = Column(Float(53))
    geometry_rotation_y = Column(Float(53))
    geometry_rotation_z = Column(Float(53))
    width = Column(Float(53))
    length = Column(Float(53))
    height = Column(Float(53))
    centroid_x = Column(Float(53))
    centroid_y = Column(Float(53))
    centroid_z = Column(Float(53))
    model_reference = Column(String)

    def geom(self):
        print(f"{list(to_shape(self.basepolygon).exterior.coords)}")
    

class genericattribs(Base):
    __tablename__ = 'genericattribs'
    __table_args__ = {'schema': 'osi'}

    cityobject_id = Column(Integer, primary_key=True)
    geometry_rotation_x = Column(Float(53))
    geometry_rotation_y = Column(Float(53))
    geometry_rotation_z = Column(Float(53))
    identifier_laneId = Column(Integer)
    identifier_laneSectionId = Column(Integer)
    identifier_modelDate = Column(String)
    identifier_modelName = Column(String)
    identifier_modelVendor = Column(String)
    identifier_roadId = Column(String)
    identifier_roadObjectId = Column(String)
    identifier_roadObjectName = Column(String)
    identifier_sourceFileExtension = Column(String)
    identifier_sourceFileHashSha256 = Column(String)
    identifier_sourceFileName = Column(String)
    identifier_to_laneId = Column(Integer)
    identifier_to_laneSectionId = Column(Integer)
    identifier_to_modelDate = Column(String)
    identifier_to_modelName = Column(String)
    identifier_to_modelVendor = Column(String)
    identifier_to_roadId = Column(String)
    identifier_to_sourceFileExtension = Column(String)
    identifier_to_sourceFileHashSha256 = Column(String)
    identifier_to_sourceFileName = Column(String)
    opendrive_lane_heightOffset_curvePositionStart_0 = Column(Float(53))
    opendrive_lane_heightOffset_curvePositionStart_1 = Column(Float(53))
    opendrive_lane_heightOffset_inner_0 = Column(Float(53))
    opendrive_lane_heightOffset_inner_1 = Column(Float(53))
    opendrive_lane_heightOffset_outer_0 = Column(Float(53))
    opendrive_lane_heightOffset_outer_1 = Column(Float(53))
    opendrive_lane_level = Column(String)
    opendrive_lane_material_curvePositionStart_0 = Column(Float(53))
    opendrive_lane_material_friction_0 = Column(Float(53))
    opendrive_lane_material_roughness_0 = Column(Float(53))
    opendrive_lane_material_surface_0 = Column(String)
    opendrive_lane_predecessor_lane_0 = Column(Integer)
    opendrive_laneSection_curvePositionStart = Column(Float(53))
    opendrive_lane_speed_curvePositionStart_0 = Column(Float(53))
    opendrive_lane_speed_max_0_unit = Column(String)
    opendrive_lane_speed_max_0 = Column(Float(53))
    opendrive_lane_successor_lane_0 = Column(Integer)
    opendrive_lane_type = Column(String)
    opendrive_road_junction = Column(String)
    opendrive_road_length = Column(Float(53))
    opendrive_roadMarking_color = Column(String)
    opendrive_roadMarking_curvePositionStart = Column(Float(53))
    opendrive_roadMarking_material = Column(String)
    opendrive_roadMarking_type = Column(String)
    opendrive_roadMarking_weight = Column(String)
    opendrive_roadMarking_width = Column(Float(53))
    opendrive_roadObject_dynamic = Column(String)
    opendrive_roadObject_orientation = Column(String)
    opendrive_roadObject_type = Column(String)
    opendrive_roadObject_validLength = Column(Float(53))
    opendrive_road_predecessor_contactPoint = Column(String)
    opendrive_road_predecessor_junction = Column(String)
    opendrive_road_predecessor_road = Column(String)
    opendrive_road_rule = Column(String)
    opendrive_roadSignal_countryCode = Column(String)
    opendrive_roadSignal_dynamic = Column(String)
    opendrive_roadSignal_orientation = Column(String)
    opendrive_roadSignal_subtype = Column(String)
    opendrive_roadSignal_type = Column(String)
    opendrive_roadSignal_value = Column(Float(53))
    opendrive_road_successor_contactPoint = Column(String)
    opendrive_road_successor_junction = Column(String)
    opendrive_road_successor_road = Column(String)    


class TrafficSign(Base):
    __tablename__ = 'TrafficSign'
    __table_args__ = {'schema': 'osi'}

    cityobject_id = Column(Integer, primary_key=True)
    geometry_rotation_x = Column(Float(53))
    geometry_rotation_y = Column(Float(53))
    geometry_rotation_z = Column(Float(53))
    identifier_roadObjectName = Column(String)
    identifier_roadObjectId = Column(String)
    opendrive_roadSignal_countryCode = Column(String)
    opendrive_roadSignal_type = Column(String)
    opendrive_roadSignal_subtype = Column(String)
    opendrive_roadSignal_value = Column(Float(53))
    centroid_x = Column(Float(53))
    centroid_y = Column(Float(53))
    centroid_z = Column(Float(53))
    geom = Column(Geometry(from_text='ST_GeomFromEWKT', name='geometry'))


class Lane(Base):
    __tablename__ = 'Lane'
    __table_args__ = {'schema': 'osi'}

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    geom = Column(Geometry(from_text='ST_GeomFromEWKT', name='geometry'))
    right_lane_boundary_id = Column(Integer)
    left_lane_boundary_id = Column(Integer)
    identifier_laneId = Column(Integer)
    identifier_laneSectionId = Column(Integer)
    identifier_roadId = Column(String)
    opendrive_lane_type = Column(String)
    opendrive_road_junction = Column(String)
    opendrive_road_predecessor_junction = Column(String)
    opendrive_road_successor_junction = Column(String)
    opendrive_road_predecessor_road = Column(String)
    opendrive_road_successor_road = Column(String)


class LaneBoundary(Base):
   __tablename__ = 'LaneBoundary'
   __table_args__ = {'schema': 'osi'}

   id = Column(Integer, primary_key=True)
   side = Column(String)
   geom = Column(Geometry(from_text='ST_GeomFromEWKT', name='geometry'))
   identifier_laneId = Column(Integer)
   identifier_laneSectionId = Column(Integer)
   identifier_roadId = Column(String)
   opendrive_roadMarking_color = Column(String)
   opendrive_roadMarking_material = Column(String)
   opendrive_roadMarking_type = Column(String)
   opendrive_roadMarking_width = Column(Float(53))
   opendrive_roadMarking_weight = Column(String)


class RoadMarking(Base):
   __tablename__ = 'RoadMarking'
   __table_args__ = {'schema': 'osi'}

   cityobject_id = Column(Integer, primary_key=True)
   identifier_roadId = Column(String)
   identifier_laneSectionId = Column(Integer)
   identifier_laneId = Column(Integer)
   geom = Column(Geometry('GEOMETRYZ', 32632, from_text='ST_GeomFromEWKT', name='geometry'))
   opendrive_roadMarking_color = Column(String)
   opendrive_roadMarking_curvePositionStart = Column(Float(53))
   opendrive_roadMarking_material = Column(String)
   opendrive_roadMarking_type = Column(String)
   opendrive_roadMarking_weight = Column(String)
   opendrive_roadMarking_width = Column(Float(53))
