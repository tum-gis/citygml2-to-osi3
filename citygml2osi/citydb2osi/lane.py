import typing
from typing import List

import osi3.osi_lane_pb2 as osi_lane
from sqlalchemy.sql.base import NO_ARG
from . import osidb

from .common import Identifier, Vector3d
from geoalchemy2.shape import to_shape

class BoundaryPoint:
    """
    A single point of a lane boundary.
    """
    position: Vector3d
    width: float
    height: float

    def __init__(self, position: Vector3d = None, width: float = None, height: float = None) -> None:
        if position is not None:
            self.position = position

        if width is not None:
            self.width = width

        if height is not None:
            self.height = height
        pass

    def write_pb(self, bp_pb: osi_lane._LANEBOUNDARY_BOUNDARYPOINT) -> None:
        if hasattr(self, 'position'):
            self.position.write_pb(bp_pb.position)

        if hasattr(self, 'width'):
            bp_pb.width = self.width

        if hasattr(self, 'height'):
            bp_pb.height = self.height
        pass


class LaneBoundaryClassification:
    """
    Classification of a lane boundary.
    """
    type_: int
    color: int
    limiting_structure_id: typing.List[Identifier]

    # Custum mapping for the opendrive standard 2 the PMSF osi visualizer
    map_type = {"CURB": 12, "BROKEN": 4}  # Type_Dashed_Line == 4
    map_color = {"STANDARD": 3}

    def __init__(self, type_: int = None, color: int = None, limiting_structure_id: typing.List[Identifier] = None) -> None:
        if type_ is not None:
            self.type_ = type_
        if color is not None:
            self.color = color

        if limiting_structure_id is not None:
            self.limiting_structure_id = limiting_structure_id

    @staticmethod
    def from_sql(lb_sql: osidb.LaneBoundary) -> 'LaneBoundaryClassification':
        return LaneBoundaryClassification(
            type_ = LaneBoundaryClassification.map_type.get(lb_sql.opendrive_roadMarking_type),  # will return None case NA
            color = LaneBoundaryClassification.map_color.get(lb_sql.opendrive_roadMarking_color),
            limiting_structure_id = None  # not available
        )
        pass

    def write_pb(self, lbc_pb: osi_lane._LANEBOUNDARY_CLASSIFICATION) -> None:
        if hasattr(self, 'type_'):
            lbc_pb.type = self.type_

        if hasattr(self, 'color'):
            lbc_pb.color = self.color

        if hasattr(self, 'limiting_structure_id'):
            for element in self.limiting_structure_id:
                osi_limiting_structure_id = lbc_pb.limiting_structure_id.add()
                # TODO MUST be checked
                element.write_pb(osi_limiting_structure_id)

            # raise Exception(f"Limiting structure id is not yet implemented")  # TODO


class LaneBoundary:
    """
    A lane boundary defining the border of a lane.
    The left and right lane boundary define the width of the lane.
    Additionally, free markings can be defined, e.g. at construction sites.
    Free markings across multiple lanes may be defined multiple times for all affected lanes.
    """
    id_: Identifier
    boundary_line: typing.List[BoundaryPoint] = []
    classification: LaneBoundaryClassification

    def __init__(self, id_: Identifier = None, boundary_line: typing.List[BoundaryPoint] = None, classification: LaneBoundaryClassification = None) -> None:
        if id_ is not None:
            self.id_ = id_

        if boundary_line is not None:
            self.boundary_line = boundary_line

        if classification is not None:
            self.classification = classification
            
    @staticmethod
    def from_sql(lb_sql : osidb.LaneBoundary) -> 'LaneBoundary':
        return LaneBoundary(
                id_=Identifier(lb_sql.id),
                boundary_line=list(map(lambda c: BoundaryPoint(position=Vector3d(x=c[0], y=c[1], z=c[2]), width=lb_sql.opendrive_roadMarking_width), list(to_shape(lb_sql.geom).coords))) if lb_sql.geom is not None else None,  # BoundaryPoint
                classification=LaneBoundaryClassification.from_sql(lb_sql)
                # classification=LaneBoundaryClassification(type_=3)
            )

    def write_pb(self, lb_pb: osi_lane._LANEBOUNDARY) -> None:
        if hasattr(self, 'id_'):
            self.id_.write_pb(lb_pb.id)

        if hasattr(self, 'boundary_line'):
            for element in self.boundary_line:
                osi_boundary_line = lb_pb.boundary_line.add()
                element.write_pb(osi_boundary_line)
            #raise Exception(f'Boundary line not yet implemented')

        if hasattr(self, 'classification'):
            self.classification.write_pb(lb_pb.classification)

class LanePairing:
    """
    The lane ID pairings of antecessor and successor lanes.
    """

    antecessor_lane_id : Identifier
    successor_lane_id : Identifier

    def __init__(self, antecessor_lane_id : Identifier = None, successor_lane_id : Identifier = None) -> None:
        if antecessor_lane_id is not None:
            self.antecessor_lane_id = antecessor_lane_id

        if successor_lane_id is not None:
            self.successor_lane_id = successor_lane_id

    def write_pb(self, lp_pb : osi_lane._LANE_CLASSIFICATION_LANEPAIRING) -> None:
        if hasattr(self, 'antecessor_lane_id'):
            self.antecessor_lane_id.write_pb(lp_pb.antecessor_lane_id)
    
        if hasattr(self, 'successor_lane_id'):
            self.successor_lane_id.write_pb(lp_pb.successor_lane_id)


class RoadCondition:
    """
    The condition of the road surface
    """
    surface_temperature : float
    surface_water_film : float
    surface_freezing_point : float
    surface_ice : float
    surface_roughness : float
    surface_texture : float
    
    def __init__(self, surface_temperature : float = None, surface_water_film : float = None, 
    surface_freezing_point : float = None, surface_ice : float = None, surface_roughness : float = None,
    surface_texture : float = None) -> None:

        if surface_temperature is not None:
            self.surface_temperature = surface_temperature

        if surface_water_film is not None:
            self.surface_water_film = surface_water_film

        if surface_freezing_point is not None:
            self.surface_freezing_point = surface_freezing_point
        
        if surface_ice is not None:
            self.surface_ice = surface_ice

        if surface_roughness is not None:
            self.surface_roughness = surface_roughness

        if surface_texture is not None:
            self.surface_texture = surface_texture

    def write_pb(self, rc_pb : osi_lane._LANE_CLASSIFICATION_ROADCONDITION) -> None:
        if hasattr(self, 'surface_temperature'):
            rc_pb.surface_temperature = self.surface_temperature

        if hasattr(self, 'surface_water_film'):
            rc_pb.surface_water_film = self.surface_water_film

        if hasattr(self, 'surface_freezing_point'):
            rc_pb.surface_freezing_point = self.surface_freezing_point

        if hasattr(self, 'surface_ice'):
            rc_pb.surface_ice = self.surface_ice

        if hasattr(self, 'surface_roughness'):
            rc_pb.surface_roughness = self.surface_roughness

        if hasattr(self, 'surface_texture'):
            rc_pb.surface_texture = self.surface_texture
            

class LaneClassification:
    """
    Classification of a lane.
    """

    type_ : int
    is_host_vehicle_lane : bool
    centerline : typing.List[Vector3d]
    centerline_is_driving_direction : bool
    left_adjacent_lane_id: typing.List[Identifier]
    right_adjacent_lane_id : typing.List[Identifier]
    lane_pairing : typing.List[LanePairing]
    right_lane_boundary_id: typing.List[Identifier]
    left_lane_boundary_id : typing.List[Identifier]
    free_lane_boundary_id : typing.List[Identifier]
    road_condition : RoadCondition

    # Custum Mapping
    @staticmethod
    def get_type_custom(opendrive_lane_type: str, opendrive_road_junction: str) -> int:
        # 0 if opendrive_lane_type != "DRIVING" else 2 if opendrive_road_junction is None else 4
        if opendrive_lane_type == "DRIVING":
            if opendrive_road_junction is None:
                res = 2
            else:
                res = 4
        else:
            res = 0
        return res

    def __init__(self,
        type_ : int = None,
        is_host_vehicle_lane : bool  = None,
        centerline : typing.List[Vector3d]  = None,
        centerline_is_driving_direction : bool  = None,
        left_adjacent_lane_id: typing.List[Identifier]  = None, 
        right_adjacent_lane_id : typing.List[Identifier]  = None,
        lane_pairing : typing.List[LanePairing]  = None, 
        right_lane_boundary_id: typing.List[Identifier]  = None,
        left_lane_boundary_id : typing.List[Identifier]  = None,
        free_lane_boundary_id : typing.List[Identifier]  = None,
        road_condition : RoadCondition  = None
        ) -> None:

        if type_ is not None:
            self.type_ = type_ if type_ in range(5) else 0
        
        if is_host_vehicle_lane is not None:
            self.is_host_vehicle_lane = is_host_vehicle_lane

        if centerline is not None:
            self.centerline = centerline

        if centerline_is_driving_direction is not None:
            self.centerline_is_driving_direction = centerline_is_driving_direction

        if left_adjacent_lane_id is not None:
            self.left_adjacent_lane_id = left_adjacent_lane_id
        
        if right_adjacent_lane_id is not None:
            self.right_adjacent_lane_id = right_adjacent_lane_id

        if lane_pairing is not None:
            self.lane_pairing = lane_pairing

        if right_lane_boundary_id is not None:
            self.right_lane_boundary_id = right_lane_boundary_id
        
        if left_lane_boundary_id is not None:
            self.left_lane_boundary_id = left_lane_boundary_id

        if free_lane_boundary_id is not None:
            self.free_lane_boundary_id = free_lane_boundary_id

        if road_condition is not None:
            self.road_condition = road_condition
            
    @staticmethod
    def from_sql(l_sql : osidb.Lane) -> 'LaneClassification':
        return LaneClassification(
            type_=LaneClassification.get_type_custom(l_sql.opendrive_lane_type, l_sql.opendrive_road_junction),
            centerline=list(map(lambda c: Vector3d(x=c[0], y=c[1], z=c[2]), list(to_shape(l_sql.geom).coords))) if l_sql.geom is not None else None,
            left_lane_boundary_id=[Identifier(l_sql.left_lane_boundary_id)],  # TODO right now only one id is available in materialized view
            right_lane_boundary_id=[Identifier(l_sql.right_lane_boundary_id)]
        )

    def write_pb(self, lc_pb : osi_lane._LANE_CLASSIFICATION) -> None:
        if hasattr(self, 'type_'):
            lc_pb.type = self.type_
        
        if hasattr(self, 'is_host_vehicle_lane'):
            lc_pb.is_host_vehicle_lane = self.is_host_vehicle_lane

        if hasattr(self, 'centerline'):
            for element in self.centerline:
                osi_centerline = lc_pb.centerline.add()
                element.write_pb(osi_centerline)

        if hasattr(self, 'centerline_is_driving_direction'):
            lc_pb.centerline_is_driving_direction = self.centerline_is_driving_direction

        if hasattr(self, 'left_adjacent_lane_id'):
            for element in self.left_adjacent_lane_id:
                osi_left_adjacent_lane_id = lc_pb.left_adjacent_lane_id.add()
                element.write_pb(osi_left_adjacent_lane_id)

        if hasattr(self, 'right_adjacent_lane_id'):
            for element in self.right_adjacent_lane_id:
                osi_right_adjacent_lane_id = lc_pb.right_adjacent_lane_id.add()
                element.write_pb(osi_right_adjacent_lane_id)

        if hasattr(self, 'lane_pairing'):
            for element in self.lane_pairing:
                osi_lane_pairing = lc_pb.lane_pairing.add()
                element.write_pb(osi_lane_pairing)

        if hasattr(self, 'right_lane_boundary_id'):
            for element in self.right_lane_boundary_id:
                osi_right_lane_boundary_id = lc_pb.right_lane_boundary_id.add()
                element.write_pb(osi_right_lane_boundary_id)

        if hasattr(self, 'left_lane_boundary_id'):
            for element in self.left_lane_boundary_id:
                osi_left_lane_boundary_id = lc_pb.left_lane_boundary_id.add()
                element.write_pb(osi_left_lane_boundary_id)

        if hasattr(self, 'free_lane_boundary_id'):
            for element in self.free_lane_boundary_id:
                osi_free_lane_boundary_id = lc_pb.free_lane_boundary_id.add()
                element.write_pb(osi_free_lane_boundary_id)

        if hasattr(self, 'road_condition'):
            self.road_condition.write_pb(lc_pb.road_condition)


class Lane:
    """
    A lane in the road network.
    A lane is part of a road and mainly characterized by its center line. It also knows about any adjacent lanes, antecessor and successor lanes. 
    """

    classification : LaneClassification
    id_ : Identifier

    def __init__(self, classification : LaneClassification = None, id_ : Identifier = None) -> None:
        if classification is not None:
            self.classification = classification

        if id_ is not None:
            self.id_ = id_
            
    @staticmethod
    def from_sql(l_sql : osidb.Lane) -> 'Lane':
        return Lane(
            id_=Identifier(l_sql.id),
            classification=LaneClassification.from_sql(l_sql)
        )

    def write_pb(self, ln_pb : osi_lane._LANE) -> None:
        if hasattr(self, 'classification'):
            self.classification.write_pb(ln_pb.classification)

        if hasattr(self, 'id_'):
            self.id_.write_pb(ln_pb.id)

