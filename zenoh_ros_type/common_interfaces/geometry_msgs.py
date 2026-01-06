from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import array, float32, float64, int64, sequence

from .std_msgs import Header


@dataclass
class Vector3(IdlStruct, typename='Vector3'):
    x: float64
    y: float64
    z: float64


@dataclass
class Vector3Stamped(IdlStruct, typename='Vector3Stamped'):
    header: Header
    vector: Vector3


@dataclass
class Point(IdlStruct, typename='Point'):
    x: float64
    y: float64
    z: float64


@dataclass
class Point32(IdlStruct, typename='Point32'):
    x: float32
    y: float32
    z: float32


@dataclass
class PointStamped(IdlStruct, typename='PointStamped'):
    header: Header
    point: Point


@dataclass
class Quaternion(IdlStruct, typename='Quaternion'):
    x: float64
    y: float64
    z: float64
    w: float64


@dataclass
class QuaternionStamped(IdlStruct, typename='QuaternionStamped'):
    header: Header
    quaternion: Quaternion


@dataclass
class Pose(IdlStruct, typename='Pose'):
    position: Point
    orientation: Quaternion


@dataclass
class PoseStamped(IdlStruct, typename='PoseStamped'):
    header: Header
    pose: Pose


@dataclass
class PoseArray(IdlStruct, typename='PoseArray'):
    header: Header
    poses: sequence[Pose]


@dataclass
class PoseWithCovariance(IdlStruct, typename='PoseWithCovariance'):
    pose: Pose
    covariance: array[float64, 36]


@dataclass
class PoseWithCovarianceStamped(IdlStruct, typename='PoseWithCovarianceStamped'):
    header: Header
    pose: PoseWithCovariance


@dataclass
class Transform(IdlStruct, typename='Transform'):
    translation: Vector3
    rotation: Quaternion


@dataclass
class TransformStamped(IdlStruct, typename='TransformStamped'):
    header: Header
    child_frame_id: str
    transform: Transform


@dataclass
class Twist(IdlStruct, typename='Twist'):
    linear: Vector3
    angular: Vector3


@dataclass
class TwistStamped(IdlStruct, typename='TwistStamped'):
    header: Header
    twist: Twist


@dataclass
class TwistWithCovariance(IdlStruct, typename='TwistWithCovariance'):
    twist: Twist
    covariance: array[float64, 36]


@dataclass
class TwistWithCovarianceStamped(IdlStruct, typename='TwistWithCovarianceStamped'):
    header: Header
    twist: TwistWithCovariance


@dataclass
class Accel(IdlStruct, typename='Accel'):
    linear: Vector3
    angular: Vector3


@dataclass
class AccelStamped(IdlStruct, typename='AccelStamped'):
    header: Header
    accel: Accel


@dataclass
class AccelWithCovariance(IdlStruct, typename='AccelWithCovariance'):
    accel: Accel
    covariance: array[float64, 36]


@dataclass
class AccelWithCovarianceStamped(IdlStruct, typename='AccelWithCovarianceStamped'):
    header: Header
    accel: AccelWithCovariance


@dataclass
class Wrench(IdlStruct, typename='Wrench'):
    force: Vector3
    torque: Vector3


@dataclass
class WrenchStamped(IdlStruct, typename='WrenchStamped'):
    header: Header
    wrench: Wrench


@dataclass
class Inertia(IdlStruct, typename='Inertia'):
    m: float64
    com: Vector3
    ixx: float64
    ixy: float64
    ixz: float64
    iyy: float64
    iyz: float64
    izz: float64


@dataclass
class InertiaStamped(IdlStruct, typename='InertiaStamped'):
    header: Header
    inertia: Inertia


@dataclass
class Polygon(IdlStruct, typename='Polygon'):
    points: sequence[Point32]


@dataclass
class PolygonStamped(IdlStruct, typename='PolygonStamped'):
    header: Header
    polygon: Polygon


@dataclass
class PolygonInstance(IdlStruct, typename='PolygonInstance'):
    polygon: Polygon
    id: int64


@dataclass
class PolygonInstanceStamped(IdlStruct, typename='PolygonInstanceStamped'):
    header: Header
    polygon: PolygonInstance


@dataclass
class VelocityStamped(IdlStruct, typename='VelocityStamped'):
    header: Header
    body_frame_id: str
    reference_frame_id: str
    velocity: Twist
