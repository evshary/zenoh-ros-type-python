from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import float32, int8, sequence, uint32

from ..rcl_interfaces.builtin_interfaces import Time
from .geometry_msgs import (
    Accel,
    Point,
    Pose,
    PoseStamped,
    PoseWithCovariance,
    Twist,
    TwistWithCovariance,
    Wrench,
)
from .std_msgs import Header


@dataclass
class MapMetaData(IdlStruct, typename='MapMetaData'):
    map_load_time: Time
    resolution: float32
    width: uint32
    height: uint32
    origin: Pose


@dataclass
class OccupancyGrid(IdlStruct, typename='OccupancyGrid'):
    header: Header
    info: MapMetaData
    data: sequence[int8]


@dataclass
class Odometry(IdlStruct, typename='Odometry'):
    header: Header
    child_frame_id: str
    pose: PoseWithCovariance
    twist: TwistWithCovariance


@dataclass
class Path(IdlStruct, typename='Path'):
    header: Header
    poses: sequence[PoseStamped]


@dataclass
class GridCells(IdlStruct, typename='GridCells'):
    header: Header
    cell_width: float32
    cell_height: float32
    cells: sequence[Point]


@dataclass
class Goals(IdlStruct, typename='Goals'):
    header: Header
    goals: sequence[PoseStamped]


@dataclass
class TrajectoryPoint(IdlStruct, typename='TrajectoryPoint'):
    header: Header
    pose: Pose
    velocity: Twist
    acceleration: Accel
    effort: Wrench


@dataclass
class Trajectory(IdlStruct, typename='Trajectory'):
    header: Header
    points: sequence[TrajectoryPoint]
