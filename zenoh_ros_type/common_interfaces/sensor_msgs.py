from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import array, float64, int8, sequence, uint8, uint16, uint32

from .geometry_msgs import Quaternion, Vector3
from .std_msgs import Header


@dataclass
class RegionOfInterest(IdlStruct, typename='RegionOfInterest'):
    x_offset: uint32
    y_offset: uint32
    height: uint32
    width: uint32
    do_rectify: bool


@dataclass
class CameraInfo(IdlStruct, typename='CameraInfo'):
    header: Header
    height: uint32
    width: uint32
    distortion_model: str
    d: sequence[float64]
    k: array[float64, 9]
    r: array[float64, 9]
    p: array[float64, 12]
    binning_x: uint32
    binning_y: uint32
    roi: RegionOfInterest


@dataclass
class Image(IdlStruct, typename='Image'):
    header: Header
    height: uint32
    width: uint32
    encoding: str
    is_bigendian: uint8
    step: uint32
    data: sequence[uint8]


@dataclass
class IMU(IdlStruct, typename='IMU'):
    header: Header
    orientation: Quaternion
    orientation_covariance: array[float64, 9]
    angular_velocity: Vector3
    angular_velocity_covariance: array[float64, 9]
    linear_acceleration: Vector3
    linear_acceleration_covariance: array[float64, 9]


@dataclass
class NavSatStatus(IdlStruct, typename='NavSatStatus'):
    class STATUS(Enum):
        NO_FIX = -1  # unable to fix position
        FIX = 0  # unaugmented fix
        SBAS_FIX = 1  # with satellite-based augmentation
        GBAS_FIX = 2  # with ground-based augmentation

    status: int8

    class SERVICE(Enum):
        GPS = 1
        GLONASS = 2
        COMPASS = 4  # includes BeiDou
        GALILEO = 8

    service: uint16


@dataclass
class NavSatFix(IdlStruct, typename='NavSatFix'):
    header: Header
    status: NavSatStatus
    latitude: float64
    longitude: float64
    altitude: float64
    position_covariance: array[float64, 9]

    class POSITION_COVARIANCE_TYPE(Enum):
        UNKNOWN = 0
        APPROXIMATED = 1
        DIAGONAL_KNOWN = 2
        KNOWN = 3

    position_covariance_type: uint8


@dataclass
class PointField(IdlStruct, typename='PointField'):
    name: str
    offset: uint32

    class DATA_TYPE(Enum):
        INT8 = 1
        UINT8 = 2
        INT16 = 3
        UINT16 = 4
        INT32 = 5
        UINT32 = 6
        FLOAT32 = 7
        FLOAT64 = 8

    datatype: uint8
    count: uint32


@dataclass
class PointCloud2(IdlStruct, typename='PointCloud2'):
    header: Header
    height: uint32
    width: uint32
    fields: sequence[PointField]
    is_bigendian: bool
    point_step: uint32
    row_step: uint32
    data: sequence[uint8]
    is_dense: bool
