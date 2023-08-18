from dataclasses import dataclass
from pycdr2 import IdlStruct,Enum
from pycdr2.types import uint8, uint32, float32
from ..rcl_interfaces.builtin_interfaces import Time
from ..common_interfaces.std_msgs import Header
from ..service import ServiceHeader

@dataclass
class ControlModeCommand(IdlStruct, typename="ControlModeCommand"):
    stamp: Time
    class MODE(Enum):
        NO_COMMAND = 0
        AUTONOMOUS = 1
        MANUAL = 2
    mode: uint8

@dataclass
class ControlModeReport(IdlStruct, typename="ControlModeReport"):
    stamp: Time
    class MODE(Enum):
        NO_COMMAND = 0
        AUTONOMOUS = 1
        MANUAL = 2
    mode: uint8

@dataclass
class Engage(IdlStruct, typename="Engage"):
    stamp: Time
    enable: bool

@dataclass
class GearCommand(IdlStruct, typename="GearCommand"):
    stamp: Time
    class COMMAND(Enum):
        DRIVE = 2
        REVERSE = 20
        PARK = 22
        LOW = 23
    command: uint8

@dataclass
class GearReport(IdlStruct, typename="GearReport"):
    stamp: Time
    class REPORT(Enum):
        DRIVE = 2
        REVERSE = 20
        PARK = 22
        LOW = 23
    report: uint8

@dataclass
class SteeringReport(IdlStruct, typename="SteeringReport"):
    stamp: Time
    steering_tire_angle: float32

@dataclass
class VelocityReport(IdlStruct, typename="VelocityReport"):
    header: Header
    longitudinal_velocity: float32
    lateral_velocity: float32
    heading_rate: float32

# -----service-----

@dataclass
class EngageRequest(IdlStruct, typename="EngageRequest"):
    header: ServiceHeader
    mode: bool

@dataclass
class EngageResponse(IdlStruct, typename="EngageResponse"):
    header: ServiceHeader
    code: uint32
    message: str
    success: bool
