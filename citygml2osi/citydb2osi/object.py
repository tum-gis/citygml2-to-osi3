import typing

import osi3.osi_object_pb2 as osi_object
from . import osidb

from .common import BaseStationary, Identifier


class StationaryObject_Classification:
    """
    Classification data for a stationary object.
    """
    type_: int
    material: int
    density: int
    color: int

    def __init__(self, type_: int = None, material: int = None, density: int = None, color: int = None) -> None:
        if type_ is not None:
            self.type_ = type_ if type_ in range(17) else 0

        if material is not None:
            self.material = material if material in range(9) else 0

        if density is not None:
            self.density = density if density in range(7) else 0

        if color is not None:
            self.color = color if color in range(11) else 0

    @staticmethod
    def from_sql(tsql: typing.Any) -> 'StationaryObject_Classification':
        return StationaryObject_Classification()

    def write_pb(self, soc_pb: osi_object._STATIONARYOBJECT_CLASSIFICATION) -> None:
        if hasattr(self, 'type_'):
            soc_pb.type = self.type_

        if hasattr(self, 'material'):
            soc_pb.material = self.material

        if hasattr(self, 'density'):
            soc_pb.density = self.density

        if hasattr(self, 'color'):
            soc_pb.color = self.color


class StationaryObject:
    """
    A simulated object that is neither a moving object (vehicle or MovingObject e.g. pedestrian, animal, or vehicle)
        nor a traffic related object (TrafficLight, TrafficSign).
    """
    model_reference: str    # Opaque reference of an associated 3D model of the stationary object.
    base: BaseStationary    # The base parameters of the stationary object.
    id_: Identifier         # The ID of the object.
    # The classification of the stationary object.
    classification: StationaryObject_Classification
    #T_StationaryObj: osidb.StationaryObject

    _type_mapping = {"VEGETATION": 9, "BUILDING": 3, "BARRIER": 8, "TREE": 7, "POLE": 4, "OBSTACLE": 8, "WALL": 11}

    # def __init__(self, t_StationaryObj: osidb.StationaryObject) -> None:
    #     self.model_reference = t_StationaryObj.model_reference
    #     self.base = BaseStationary()

    @staticmethod
    def from_sql(t_StationaryObj: osidb.StationaryObject) -> 'StationaryObject':
        # const building mappig as mapping is required  int(t_StationaryObj.Type)
        # type_ = 3
        try: 
            type_ = StationaryObject._type_mapping[t_StationaryObj.Type]
            type_ = type_ if type_ != 3 else 11  # avoid buildings as they are not implemented in the visualizer
        except Exception:
            type_ = 0  # unknown
        return StationaryObject(model_reference=t_StationaryObj.model_reference,
                                base=BaseStationary.from_sql(t_StationaryObj),
                                id_=Identifier(t_StationaryObj.cityobject_id),
                                classification=StationaryObject_Classification(type_=type_))

    def __init__(self, model_reference: str = None, base: BaseStationary = None, id_: Identifier = None, classification: StationaryObject_Classification = None) -> None:
        if model_reference is not None:
            self.model_reference = model_reference

        if base is not None:
            self.base = base

        if id_ is not None:
            self.id_ = id_

        if classification is not None:
            self.classification = classification

    def write_pb(self, so_pb: osi_object._STATIONARYOBJECT) -> None:
        if hasattr(self, 'model_reference'):
            so_pb.model_reference = self.model_reference

        if hasattr(self, 'base'):
            self.base.write_pb(so_pb.base)

        if hasattr(self, 'id_'):
            self.id_.write_pb(so_pb.id)

        if hasattr(self, 'classification'):
            self.classification.write_pb(so_pb.classification)
