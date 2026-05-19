from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import float32, int64, sequence, uint8

from ..rcl_interfaces.builtin_interfaces import Time


@dataclass
class TrafficLightElement(IdlStruct, typename='TrafficLightElement'):
    class COLOR(Enum):
        UNKNOWN = 0
        RED = 1
        AMBER = 2
        GREEN = 3
        WHITE = 4

    class SHAPE(Enum):
        UNKNOWN = 0
        CIRCLE = 1
        LEFT_ARROW = 2
        RIGHT_ARROW = 3
        UP_ARROW = 4
        UP_LEFT_ARROW = 5
        UP_RIGHT_ARROW = 6
        DOWN_ARROW = 7
        DOWN_LEFT_ARROW = 8
        DOWN_RIGHT_ARROW = 9
        CROSS = 10

    class STATUS(Enum):
        UNKNOWN = 0
        SOLID_OFF = 1
        SOLID_ON = 2
        FLASHING = 3

    color: uint8
    shape: uint8
    status: uint8
    confidence: float32


@dataclass
class PredictedTrafficLightState(IdlStruct, typename='PredictedTrafficLightState'):
    INFORMATION_SOURCE_V2N = 'V2N'
    INFORMATION_SOURCE_V2I = 'V2I'
    INFORMATION_SOURCE_V2V = 'V2V'
    INFORMATION_SOURCE_LOCAL_PERCEPTION = 'LOCAL_PERCEPTION'
    INFORMATION_SOURCE_MANUAL_OVERRIDE = 'MANUAL_OVERRIDE'
    INFORMATION_SOURCE_SIMULATION = 'SIMULATION'
    INFORMATION_SOURCE_INTERNAL_ESTIMATION = 'INTERNAL_ESTIMATION'

    predicted_stamp: Time
    simultaneous_elements: sequence[TrafficLightElement]
    reliability: float32
    information_source: str


@dataclass
class TrafficLightGroup(IdlStruct, typename='TrafficLightGroup'):
    traffic_light_group_id: int64
    elements: sequence[TrafficLightElement]
    predictions: sequence[PredictedTrafficLightState]


@dataclass
class TrafficLightGroupArray(IdlStruct, typename='TrafficLightGroupArray'):
    stamp: Time
    traffic_light_groups: sequence[TrafficLightGroup]
