import typing

import osi3.osi_common_pb2 as osi_common
from . import osidb
from geoalchemy2.shape import to_shape


class Orientation3d:
    """ orientation of type Orientation3d"""
    roll: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0

    def __init__(self, roll: float, pitch: float, yaw: float) -> None:
        # Workaround replacement should be probably done at db side
        self.yaw = yaw if yaw is not None else 0.0
        self.pitch = pitch if pitch is not None else 0.0
        self.roll = roll if roll is not None else 0.0

    def write_pb(self, o_pb: osi_common._ORIENTATION3D) -> None:
        o_pb.yaw = self.yaw
        o_pb.pitch = self.pitch
        o_pb.roll = self.roll


class Vector3d:
    """
    position of type Vector3d
    The reference point for position and orientation, i.e. the center (x,y,z) of the bounding box.
    """
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x if x is not None else 0.0
        self.y = y if y is not None else 0.0
        # self.z = z if z is not None else 0.0
        self.z = 0  # workaround for pmsf osi visualizer TODO

    def write_pb(self, v3_pb: osi_common._VECTOR3D) -> None:
        v3_pb.x = self.x 
        v3_pb.y = self.y
        v3_pb.z = self.z


class Vector2d:
    """
    base_polygon of type Vector
    The base attributes of a stationary object or entity.
    """
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def write_pb(self, v2_pb: osi_common._VECTOR2D) -> None:
        v2_pb.x = self.x
        v2_pb.y = self.y


class Identifier:
    """
    id, assigned_lane_id of type Identifier
    A common identifier (ID), represented as an integer.
    """
    value: int = 1

    def __init__(self, value: int) -> None:
        self.value = value    

    def write_pb(self, id_pb: osi_common._IDENTIFIER) -> None:
        id_pb.value = self.value


class Dimension3d:
    """
    Dimension of type dimension
    The dimension of a 3D box, e.g. the size of a 3D bounding box or its uncertainties.
    """
    width: float = 0.0
    height: float = 0.0
    length: float = 0.0

    def __init__(self, width: float, height: float, length: float) -> None:
        self.width = width
        self.height = height
        self.length = length

    @staticmethod
    def from_sql(tsql: typing.Any) -> 'Dimension3d':
        return Dimension3d(tsql.width, tsql.height, tsql.length)

    def write_pb(self, d_pb: osi_common._DIMENSION3D) -> None:
        d_pb.width = self.width
        d_pb.height = self.height
        d_pb.length = self.length


class BaseStationary:
    orientation: Orientation3d
    position: Vector3d
    dimension: Dimension3d
    base_polygon: typing.List[Vector2d]

    def __init__(self, orientation: Orientation3d = None, position: Vector3d = None, dimension: Dimension3d = None, base_polygon: typing.List[Vector2d] = None) -> None:
        if orientation is not None:
            self.orientation = orientation

        if position is not None:
            self.position = position

        if dimension is not None:
            self.dimension = dimension

        if base_polygon is not None:
            self.base_polygon = base_polygon

    @staticmethod
    def from_sql(tsql: typing.Any) -> 'BaseStationary':
        # print(f"Buidling - Height: {tsql.centroid_z - tsql.height / 2}") -> center of mass is not correctly visualised in the PMSF osi viewer => use footprint centroid
        return BaseStationary(
            orientation=Orientation3d(roll=tsql.geometry_rotation_x, pitch=tsql.geometry_rotation_y, yaw=tsql.geometry_rotation_z)
                if all(hasattr(tsql, attr) for attr in ["geometry_rotation_x", "geometry_rotation_y", "geometry_rotation_z"]) else None,
            position= Vector3d(x=tsql.centroid_x, y=tsql.centroid_y, z=tsql.centroid_z) if hasattr(tsql, "centroid_x") else None,
            dimension= Dimension3d(width=tsql.width, length=tsql.length, height=tsql.height) if hasattr(tsql, "width") else None,
            base_polygon=list(map(lambda c: Vector2d(x=c[0], y=c[1]), list(to_shape(tsql.basepolygon).exterior.coords))) if hasattr(tsql, "basepolygon") else None
            )

    def write_pb(self, bs_pb: osi_common.BaseStationary) -> None:
        if hasattr(self, 'orientation'):
            self.orientation.write_pb(bs_pb.orientation)

        if hasattr(self, 'position'):
            self.position.write_pb(bs_pb.position)

        if hasattr(self, 'dimension'):
            self.dimension.write_pb(bs_pb.dimension)

        if hasattr(self, 'base_polygon'):
            for element in self.base_polygon:
                osi_vector2d = bs_pb.base_polygon.add()
                element.write_pb(osi_vector2d)
