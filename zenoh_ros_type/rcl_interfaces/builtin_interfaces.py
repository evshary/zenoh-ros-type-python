from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import int32, uint32


@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32
    nanosec: uint32


@dataclass
class Duration(IdlStruct, typename='Druation'):
    sec: int32
    nanosec: uint32
