import typing

import osi3.osi_groundtruth_pb2 as osi_groundtruth
from . import osidb
from .trafficsign import TrafficSign
from .trafficlight import TrafficLight
from .roadmarking import RoadMarking
from .lane import LaneBoundary, Lane
from .object import StationaryObject


class GroundTruth:
    """
    The ground truth information from the simulation environment.

    This ground truth information is supposed to describe the whole simulated environment around any simulated vehicle.
    For each simulated host vehicle (there may be one or multiple), define an area around the vehicle which is greater than
     the combined field of views (FOV) of all obstructed sensors in the vehicle.
    The ground truth data is supposed to describe the convex hull of all such areas w.r.t. a global simulation coordinate system.
    The simulation coordinate system may change during the simulation if and only if all coordinates w.r.t. this coordinate system are also changed.
    The data has to be sent at a rate defined by the receiving partner. When sending, values with default values might be left default in order to improve performance.
    To provide a complete interface, all fields of all contained messages must be properly set unless specifically stated in the field's definition that
     the field may remain unset.
    In enums (e.g. types) the unknown (first / default) value is not allowed to be used in the ground truth interface.
    """

    stationary_objects: typing.List[StationaryObject] = []
    traffic_signs: typing.List[TrafficSign] = []
    traffic_lights: typing.List[TrafficLight] = []
    road_markings: typing.List[RoadMarking] = []
    lane_boundarys: typing.List[LaneBoundary] = []
    lanes: typing.List[Lane] = []

    # version: InterfaceVersion
    # timestamp: Timestamp
    # host_vehicle_id: Identifier
    # moving_object: MovingObject

    # occupants: typing.List[Occupant]
    # environmental_conditions: EnvironmentalCondition  # no repeated obj

    # define default values as they wont change in our project
    country_code: int = 276  # Germany
    proj_string: str  # projection string that allows to transform all coordinates in groundtruth into a different cartographic projection
    map_reference: str = '892_SAVe_Ingoldstadt'


    def write_pb(self, gt_pb: osi_groundtruth.GroundTruth) -> None:
        if hasattr(self, 'stationary_objects'):
            for s in self.stationary_objects:
                so = gt_pb.stationary_object.add()
                s.write_pb(so)

        if hasattr(self, 'traffic_signs'):
            for t in self.traffic_signs:
                ts = gt_pb.traffic_sign.add()
                t.write_pb(ts)

        if hasattr(self, 'traffic_lights'):
            for t in self.traffic_lights:
                tl = gt_pb.traffic_light.add()
                t.write_pb(tl)
                
        if hasattr(self, 'road_markings'):
            for t in self.road_markings:
                rm = gt_pb.road_marking.add()
                t.write_pb(rm)

        if hasattr(self, 'lane_boundarys'):
            for l in self.lane_boundarys:
                lb = gt_pb.lane_boundary.add()
                l.write_pb(lb)

        if hasattr(self, 'lanes'):
            for l in self.lanes:
                ln = gt_pb.lane.add()
                l.write_pb(ln)

        if hasattr(self, 'country_code') :
            gt_pb.country_code = self.country_code

        if hasattr(self, 'proj_string') :
            gt_pb.proj_string = self.proj_string  

        if hasattr(self, 'map_reference') :
            gt_pb.map_reference = self.map_reference
