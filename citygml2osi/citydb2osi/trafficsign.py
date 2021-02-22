import typing
from warnings import warn
from math import isclose as math_isclose
import osi3.osi_trafficsign_pb2 as osi_trafficsign

from . import osidb

from .common import BaseStationary, Identifier, Vector3d, Dimension3d, Orientation3d


class TrafficSignValue:
    """
    Additional value associated with a traffic sign or road marking, its unit and its text. The interpretation of this text is left to a user-defined procedure
    """
    text: str
    value_unit: int   # would be an enum
    value: float

    def __init__(self, text: str = None, value_unit: int = None, value: float = None) -> None:
        if text is not None:
            self.text = text
        if value_unit is not None:
            self.value_unit = value_unit if value_unit in range(15) else 0
        if value is not None and (math_isclose(value, -1.0, rel_tol=1e-5) is False):
            self.value = value

    @staticmethod
    def from_sql(tsql: osidb.TrafficSign) -> 'TrafficSignValue':
        return TrafficSignValue(
            text=tsql.text if hasattr(tsql, "text") else None,
            value_unit=tsql.value_unit if hasattr(tsql, "value_unit") else None,
            value=tsql.opendrive_roadSignal_value if hasattr(tsql, "opendrive_roadSignal_value") else None
        )

    def write_pb(self, tsv_pb: osi_trafficsign._TRAFFICSIGNVALUE) -> None:
        if hasattr(self, 'text'):
            tsv_pb.text = self.text

        if hasattr(self, 'value_unit'):
            tsv_pb.value_unit = self.value_unit

        if hasattr(self, 'value'):
            tsv_pb.value = self.value


class TrafficSign_MainSign_Classification:
    """
    Classification data for a traffic sign.
    """
    value: TrafficSignValue
    variability: int
    direction_scope: int
    assigned_lane_id: typing.List[Identifier]
    vertically_mirrored_is_out_of_service: bool
    # prevent python keyword conflict
    type_: int

    def __init__(self, value: TrafficSignValue = None, variability: int = None, direction_scope: int = None, assigned_lane_id: typing.List[Identifier] = None, vertically_mirrored_is_out_of_service: bool = None, type_str: str = None) -> None:
        if value is not None:
            self.value = value

        if variability is not None:
            self.variability = variability

        if direction_scope is not None:
            self.direction_scope = direction_scope if direction_scope in range(
                6) else 0  # 0: direction unknown

        if assigned_lane_id is not None:
            self.assigned_lane_id = assigned_lane_id

        if vertically_mirrored_is_out_of_service is not None:
            self.vertically_mirrored_is_out_of_service = vertically_mirrored_is_out_of_service

        if type_str is not None and Map_OpenDrive2OSI.get_osi_value(type_str) != 0:
            self.type_ = Map_OpenDrive2OSI.get_osi_value(type_str)

    @staticmethod
    def from_sql(tsql: osidb.TrafficSign) -> 'TrafficSign_MainSign_Classification':
        return TrafficSign_MainSign_Classification(
            value=TrafficSignValue.from_sql(tsql),
            type_str=tsql.opendrive_roadSignal_type,
            direction_scope=tsql.direction_scope if hasattr(tsql, "direction_scope") else 2  # 2 = No direction is set
        )

    def write_pb(self, tsmsc_pb: osi_trafficsign._TRAFFICSIGN_MAINSIGN_CLASSIFICATION) -> None:
        if hasattr(self, 'value'):
            self.value.write_pb(tsmsc_pb.value)

        if hasattr(self, 'type_'):
            tsmsc_pb.type = self.type_

        if hasattr(self, 'variability'):
            tsmsc_pb.variability = self.variability

        if hasattr(self, 'direction_scope'):
            tsmsc_pb.direction_scope = self.direction_scope

        if hasattr(self, 'vertically_mirrored_is_out_of_service'):
            tsmsc_pb.vertically_mirrored_is_out_of_service = self.vertically_mirrored_is_out_of_service

        if hasattr(self, 'assigned_lane_id'):
            for element in self.assigned_lane_id:
                osi_assigned_lane_id = tsmsc_pb.assigned_lane_id.add()
                element.write_pb(osi_assigned_lane_id)  # TODO MUST be checked

            # raise Exception(f"Assigned lane id is not yet implemented for traffic light classification")  # TODO implement

        pass


class Map_OpenDrive2OSI:

    _map = {
        "283": 63,
        #"314": 74,
        "286": 64,
        "434": 118,
        "294": 17,
        "274.1": 53,
        "274.2": 54
    }

    @staticmethod
    def get_osi_value(stvo_type: str) -> int:

        try:
            res = Map_OpenDrive2OSI._map[stvo_type]
            warn(f"StVO-value {stvo_type} was found in the osi-map {res}")
        except KeyError:
            res = 0
            # warn(f"StVO-value {stvo_type} was not found in the osi-map")
        return res


class MainSign:
    """
    Main sign of the traffic sign.
    Note: TrafficSign::MainSign::Classification is only defined by its type
    """

    classification: TrafficSign_MainSign_Classification
    base_stationary: BaseStationary

    def __init__(self, base_stationary=None, classification: TrafficSign_MainSign_Classification = None) -> None:
        if base_stationary is not None:
            self.base_stationary = base_stationary

        if classification is not None:
            self.classification = classification

    @staticmethod
    def from_sql(tsql: osidb.TrafficSign) -> 'MainSign':
        return MainSign(
            base_stationary = BaseStationary(
                    orientation=Orientation3d(roll=tsql.geometry_rotation_x, pitch=tsql.geometry_rotation_y, yaw=tsql.geometry_rotation_z)
                    if all(hasattr(tsql, attr) for attr in ["geometry_rotation_x", "geometry_rotation_y", "geometry_rotation_z"]) else None,
                    position= Vector3d(x=tsql.centroid_x, y=tsql.centroid_y, z=tsql.centroid_z) if hasattr(tsql, "centroid_x") else None,
                    dimension= Dimension3d(width=tsql.width, length=tsql.length, height=tsql.height) if hasattr(tsql, "width") else 
                    Dimension3d(width=0.8, length=0.2, height=0.9)
                ),
            classification = TrafficSign_MainSign_Classification.from_sql(tsql)
            )

    def write_pb(self, ms_pb: osi_trafficsign._TRAFFICSIGN_MAINSIGN) -> None:
        if hasattr(self, 'base_stationary'):
            self.base_stationary.write_pb(ms_pb.base)

        if hasattr(self, 'classification'):
            self.classification.write_pb(ms_pb.classification)


class SupplementarySign:
    """
    Additional supplementary sign modifying the main sign.
    Note: TrafficSign::MainSign::Classification is only defined by its type
    """

    trafficSignType: int
    base_stationary: BaseStationary

    def __init__(self, base_stationary=None, trafficSignType: int = None) -> None:
        if base_stationary is not None:
            self.base_stationary = base_stationary
        if trafficSignType is not None:
            self.trafficSignType = trafficSignType

    @staticmethod
    def from_sql() -> 'SupplementarySign':
        Exception("Not implemented")
        pass

    def write_pb(self, ss_pb: osi_trafficsign._TRAFFICSIGN_SUPPLEMENTARYSIGN) -> None:
        if hasattr(self, 'base_stationary'):
            self.base_stationary.write_pb(ss_pb.base)
        if hasattr(self, 'trafficSignType'):
            # Ill designed as no additional information is available
            ss_pb.classification.type = self.trafficSignType


class TrafficSign:
    """
    A traffic sign.
    All coordinates and orientations are relative to the global ground truth coordinate system.
    """

    main_sign: MainSign
    supplementary_sign: typing.List[SupplementarySign]
    id_: Identifier

    def __init__(self, main_sign: MainSign = None, id_: Identifier = None) -> None:
        if main_sign is not None:
            self.main_sign = main_sign

        if id_ is not None:
            self.id_ = id_

    @staticmethod
    def from_sql(tsql: osidb.TrafficSign) -> 'TrafficSign':
        ts = None

        if tsql.identifier_roadObjectName == 'ZUSATZSCHILD':  # Supplementary sign
            pass
        else:  # Main Sign
            ts = TrafficSign(
                id_=Identifier(tsql.cityobject_id),
                main_sign=MainSign.from_sql(tsql)
            )

        return ts

    def write_pb(self, tf_pb: osi_trafficsign.TrafficSign) -> None:
        if hasattr(self, 'main_sign'):
            self.main_sign.write_pb(tf_pb.main_sign)

        if hasattr(self, 'id_'):
            self.id_.write_pb(tf_pb.id)

        if hasattr(self, 'supplementary_sign'):
            for element in self.supplementary_sign:
                osi_supplementary_sign = tf_pb.supplementary_sign.add()
                # TODO MUST be checked
                element.write_pb(osi_supplementary_sign)
            # raise Exception(f"supplementary_sign is not yet implemented for TrafficSign")  # TODO implement
