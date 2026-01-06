from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import (
    char,
    float32,
    float64,
    int8,
    int16,
    int32,
    int64,
    sequence,
    uint8,
    uint16,
    uint32,
    uint64,
)

from ..rcl_interfaces.builtin_interfaces import Time


@dataclass
class Bool(IdlStruct, typename='Bool'):
    data: bool


@dataclass
class Byte(IdlStruct, typename='Byte'):
    data: uint8


@dataclass
class Char(IdlStruct, typename='Char'):
    data: char


@dataclass
class ColorRGBA(IdlStruct, typename='ColorRGBA'):
    r: float32
    g: float32
    b: float32
    a: float32


@dataclass
class Empty(IdlStruct, typename='Empty'):
    pass


@dataclass
class Float32(IdlStruct, typename='Float32'):
    data: float32


@dataclass
class Float64(IdlStruct, typename='Float64'):
    data: float64


@dataclass
class Header(IdlStruct, typename='Header'):
    stamp: Time
    frame_id: str


@dataclass
class Int8(IdlStruct, typename='Int8'):
    data: int8


@dataclass
class Int16(IdlStruct, typename='Int16'):
    data: int16


@dataclass
class Int32(IdlStruct, typename='Int32'):
    data: int32


@dataclass
class Int64(IdlStruct, typename='Int64'):
    data: int64


@dataclass
class String(IdlStruct, typename='String'):
    data: str


@dataclass
class UInt8(IdlStruct, typename='UInt8'):
    data: uint8


@dataclass
class UInt16(IdlStruct, typename='UInt16'):
    data: uint16


@dataclass
class UInt32(IdlStruct, typename='UInt32'):
    data: uint32


@dataclass
class UInt64(IdlStruct, typename='UInt64'):
    data: uint64


@dataclass
class MultiArrayDimension(IdlStruct, typename='MultiArrayDimension'):
    label: str
    size: uint32
    stride: uint32


@dataclass
class MultiArrayLayout(IdlStruct, typename='MultiArrayLayout'):
    dim: sequence[MultiArrayDimension]
    data_offset: uint32


@dataclass
class ByteMultiArray(IdlStruct, typename='ByteMultiArray'):
    layout: MultiArrayLayout
    data: sequence[uint8]


@dataclass
class Float32MultiArray(IdlStruct, typename='Float32MultiArray'):
    layout: MultiArrayLayout
    data: sequence[float32]


@dataclass
class Float64MultiArray(IdlStruct, typename='Float64MultiArray'):
    layout: MultiArrayLayout
    data: sequence[float64]


@dataclass
class Int8MultiArray(IdlStruct, typename='Int8MultiArray'):
    layout: MultiArrayLayout
    data: sequence[int8]


@dataclass
class Int16MultiArray(IdlStruct, typename='Int16MultiArray'):
    layout: MultiArrayLayout
    data: sequence[int16]


@dataclass
class Int32MultiArray(IdlStruct, typename='Int32MultiArray'):
    layout: MultiArrayLayout
    data: sequence[int32]


@dataclass
class Int64MultiArray(IdlStruct, typename='Int64MultiArray'):
    layout: MultiArrayLayout
    data: sequence[int64]


@dataclass
class UInt8MultiArray(IdlStruct, typename='UInt8MultiArray'):
    layout: MultiArrayLayout
    data: sequence[uint8]


@dataclass
class UInt16MultiArray(IdlStruct, typename='UInt16MultiArray'):
    layout: MultiArrayLayout
    data: sequence[uint16]


@dataclass
class UInt32MultiArray(IdlStruct, typename='UInt32MultiArray'):
    layout: MultiArrayLayout
    data: sequence[uint32]


@dataclass
class UInt64MultiArray(IdlStruct, typename='UInt64MultiArray'):
    layout: MultiArrayLayout
    data: sequence[uint64]
