import typing

import osi3.osi_roadmarking_pb2 as osi_roadmarking
from . import osidb

from .common import BaseStationary, Identifier
from .trafficsign import TrafficSignValue


class RoadMarkingClassification:
    """
    Classification data for a road surface marking.
    """
    type_: int
    traffic_main_sign_type: int
    monochrome_color: int
    value: TrafficSignValue
    value_text: str
    assigned_lane_id: typing.List[Identifier]
    is_out_of_service: bool

    def __init__(self, type_: int = None, traffic_main_sign_type: int = None, monochrome_color: int = None, value: TrafficSignValue = None, value_text: str = None, assigned_lane_id: typing.List[Identifier] = None, is_out_of_service: bool = None) -> None:
        if type_ is not None:
            self.type_ = type_ if type_ in range(8) else 0
        if traffic_main_sign_type is not None:
            self.traffic_main_sign_type = traffic_main_sign_type
        if monochrome_color is not None:
            self.monochrome_color = monochrome_color if monochrome_color in range(
                9) else 0

        if value is not None:
            self.value = value

        if value_text is not None:
            self.value_text = value_text

        if assigned_lane_id is not None:
            self.assigned_lane_id = assigned_lane_id

        if is_out_of_service is not None:
            self.is_out_of_service = is_out_of_service

    @staticmethod
    def from_sql():
        pass

    def write_pb(self, rmc_pb: osi_roadmarking._ROADMARKING_CLASSIFICATION) -> None:
        if hasattr(self, 'type_'):
            rmc_pb.type = self.type_

        if hasattr(self, 'traffic_main_sign_type'):
            rmc_pb.traffic_main_sign_type = self.traffic_main_sign_type

        if hasattr(self, 'monochrome_color'):
            rmc_pb.monochrome_color = self.monochrome_color

        if hasattr(self, 'value'):
            self.value.write_pb(rmc_pb.value)

        if hasattr(self, 'value_text'):
            rmc_pb.value_text = self.value_text

        if hasattr(self, 'assigned_lane_id'):
            for element in self.assigned_lane_id:
                osi_assigned_lane_id = rmc_pb.assigned_lane_id.add()
                element.write_pb(osi_assigned_lane_id)

        if hasattr(self, 'is_out_of_service'):
            rmc_pb.is_out_of_service = self.is_out_of_service


class RoadMarking:
    """
    A road surface marking
    """
    id_: Identifier
    base: BaseStationary
    classification: RoadMarkingClassification

    def __init__(self, id_: Identifier = None, base: BaseStationary = None, classification: RoadMarkingClassification = None) -> None:
        if id_ is not None:
            self.id_ = id_

        if base is not None:
            self.base = base

        if classification is not None:
            self.classification = classification

    @staticmethod
    def from_sql():
        pass

    def write_pb(self, rm_pb: osi_roadmarking._ROADMARKING) -> None:
        if hasattr(self, 'id_'):
            self.id_.write_pb(rm_pb)

        if hasattr(self, 'base'):
            self.base.write_pb(rm_pb)

        if hasattr(self, 'classification'):
            self.classification.write_pb(rm_pb)
