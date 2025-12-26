from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import float32

from ..rcl_interfaces.builtin_interfaces import Time


@dataclass
class Bool(IdlStruct, typename='Bool'):
    data: bool


@dataclass
class ColorRGBA(IdlStruct, typename='ColorRGBA'):
    r: float32
    g: float32
    b: float32
    a: float32


@dataclass
class Header(IdlStruct, typename='Header'):
    stamp: Time
    frame_id: str


@dataclass
class String(IdlStruct, typename='String'):
    data: str
