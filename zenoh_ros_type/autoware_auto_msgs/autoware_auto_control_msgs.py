from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import float32

from ..rcl_interfaces.builtin_interfaces import Time


@dataclass
class AckermannLateralCommand(IdlStruct, typename='AckermannLateralCommand'):
    stamp: Time
    steering_tire_angle: float32
    steering_tire_rotation_rate: float32


@dataclass
class LongitudinalCommand(IdlStruct, typename='LongitudinalCommand'):
    stamp: Time
    speed: float32
    acceleration: float32
    jerk: float32


@dataclass
class AckermannControlCommand(IdlStruct, typename='AckermannControlCommand'):
    stamp: Time
    lateral: AckermannLateralCommand
    longitudinal: LongitudinalCommand
