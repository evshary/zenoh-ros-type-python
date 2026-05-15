from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import float32

from ..common_interfaces.geometry_msgs import Pose


@dataclass
class PathPoint(IdlStruct, typename='PathPoint'):
    pose: Pose
    longitudinal_velocity_mps: float32
    lateral_velocity_mps: float32
    heading_rate_rps: float32
    is_final: bool
