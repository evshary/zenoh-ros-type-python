from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, float64

@dataclass
class Point(IdlStruct, typename="Point"):
    x: float64
    y: float64
    z: float64

@dataclass
class Point32(IdlStruct, typename="Point32"):
    x: float32
    y: float32
    z: float32

@dataclass
class Quaternion(IdlStruct, typename="Quaternion"):
    x: float32
    y: float32
    z: float32
    w: float32

@dataclass
class Pose(IdlStruct, typename="Pose"):
    postion: Point
    orientation: Quaternion

@dataclass
class Vector3(IdlStruct, typename="Vector3"):
    x: float64
    y: float64
    z: float64

@dataclass
class Twist(IdlStruct, typename="Twist"):
    linear: Vector3
    angular: Vector3
