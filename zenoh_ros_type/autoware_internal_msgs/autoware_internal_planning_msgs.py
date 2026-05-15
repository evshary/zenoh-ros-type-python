from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import int64, sequence

from ..autoware_msgs.autoware_planning_msgs import PathPoint
from ..common_interfaces.geometry_msgs import Point
from ..common_interfaces.std_msgs import Header


@dataclass
class PathPointWithLaneId(IdlStruct, typename='PathPointWithLaneId'):
    point: PathPoint
    lane_ids: sequence[int64]


@dataclass
class PathWithLaneId(IdlStruct, typename='PathWithLaneId'):
    header: Header
    points: sequence[PathPointWithLaneId]
    left_bound: sequence[Point]
    right_bound: sequence[Point]
