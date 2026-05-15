from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import float32, int64, sequence, uint8

from ..rcl_interfaces.builtin_interfaces import Time


@dataclass
class TrafficLightElement(IdlStruct, typename='TrafficLightElement'):
    color: uint8
    shape: uint8
    status: uint8
    confidence: float32


@dataclass
class PredictedTrafficLightState(IdlStruct, typename='PredictedTrafficLightState'):
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
