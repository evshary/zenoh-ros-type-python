from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import float32, float64, sequence, uint8

from ..common_interfaces.geometry_msgs import Twist
from ..rcl_interfaces import Time


@dataclass
class CpuStatus(IdlStruct, typename='CpuStatus'):
    class STATUS(Enum):
        OK = 0
        HIGH_LOAD = 1
        VERY_HIGH_LOAD = 2
        STALE = 3

    status: uint8
    total: float32
    usr: float32
    nice: float32
    sys: float32
    idle: float32


@dataclass
class CpuUsage(IdlStruct, typename='CpuUsage'):
    stamp: Time
    all: CpuStatus
    cpus: sequence[CpuStatus]


@dataclass
class Steering(IdlStruct, typename='Steering'):
    data: float32


@dataclass
class TurnSignal(IdlStruct, typename='TurnSignal'):
    class DATA(Enum):
        NONE = 0
        LEFT = 1
        RIGHT = 2
        HAZARD = 3

    data: uint8


@dataclass
class TurnSignalStamped(IdlStruct, typename='TurnSignalStamped'):
    stamp: Time
    turn_signal: TurnSignal


@dataclass
class GearShift(IdlStruct, typename='GearShift'):
    class DATA(Enum):
        NONE = 0
        PARKING = 1
        REVERSE = 2
        NEUTRAL = 3
        DRIVE = 4
        LOW = 5

    data: uint8


@dataclass
class GearShiftStamped(IdlStruct, typename='GearShiftStamped'):
    stamp: Time
    gear_shift: GearShift


@dataclass
class VehicleStatus(IdlStruct, typename='VehicleStatus'):
    twist: Twist
    steering: Steering
    turn_signal: TurnSignal
    gear_shift: GearShift


@dataclass
class VehicleStatusStamped(IdlStruct, typename='VehicleStatusStamped'):
    stamp: Time
    status: VehicleStatus


@dataclass
class ControlCommand(IdlStruct, typename='ControlCommand'):
    steering_angle: float64
    steering_angle_velocity: float64
    throttle: float64
    brake: float64


@dataclass
class ControlCommandStamped(IdlStruct, typename='ControlCommandStamped'):
    stamp: Time
    control: ControlCommand
