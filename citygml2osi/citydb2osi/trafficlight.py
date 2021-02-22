import typing

import osi3.osi_trafficlight_pb2 as osi_trafficlight
from . import osidb

from .common import BaseStationary, Identifier


class TrafficLight_Classification:
    """
    Classification data for a traffic light.
    """
    color: int
    icon: int
    mode: int
    counter: float
    assigned_lane_id: typing.List[Identifier]
    is_out_of_service: bool

    def __init__(self, color: int = None, icon: int = None, mode: int = None, counter: float = None, assigned_lane_id: typing.List[Identifier] = None, is_out_of_service: bool = None) -> None:
        if color is not None:
            self.color = color if color in range(7) else 0

        if icon is not None:
            self.icon = icon if icon in range(25) else 0

        if mode is not None:
            self.mode = mode if mode in range(6) else 0

        if counter is not None:
            self.counter = counter

        if assigned_lane_id is not None:
            self.assigned_lane_id = assigned_lane_id

        if is_out_of_service is not None:
            self.is_out_of_service = is_out_of_service

    def write_pb(self, tlc_pb: osi_trafficlight._TRAFFICLIGHT_CLASSIFICATION) -> None:
        if hasattr(self, 'color'):
            tlc_pb.color = self.color

        if hasattr(self, 'icon'):
            tlc_pb.icon = self.icon

        if hasattr(self, 'mode'):
            tlc_pb.mode = self.mode

        if hasattr(self, 'counter'):
            tlc_pb.counter = self.counter

        if hasattr(self, 'assigned_lane_id'):
            for element in self.assigned_lane_id:
                osi_assigned_lane_id = tlc_pb.assigned_lane_id.add()
                element.write_pb(osi_assigned_lane_id)  # TODO MUST be checked
            # raise Exception(f"Assigned lane id is not yet implemented for traffic light classification")  # TODO implement

        if hasattr(self, 'is_out_of_service'):
            tlc_pb.is_out_of_service = self.is_out_of_service
        pass


class TrafficLight:
    """
    A traffic light.
    One traffic light message defines a single 'bulb' and not a box of several bulbs, e.g. red, yellow, green are three separate traffic lights.
    """
    id_: Identifier
    base: BaseStationary
    classification: TrafficLight_Classification

    def __init__(self, id_: Identifier = None, base: BaseStationary = None, classification: TrafficLight_Classification = None) -> None:
        if id_ is not None:
            self.id_ = id_

        if base is not None:
            self.base = base

        if classification is not None:
            self.classification = classification

    def write_pb(self, tl_pb: osi_trafficlight) -> None:
        if hasattr(self, 'id_'):
            self.id_.write_pb(tl_pb.id)

        if hasattr(self, 'base'):
            self.base.write_pb(tl_pb.base)

        if hasattr(self, 'classification'):
            self.classification.write_pb(tl_pb.classification)
