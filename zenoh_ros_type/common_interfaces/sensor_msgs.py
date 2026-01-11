from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import array, float32, float64, int8, int32, sequence, uint8, uint16, uint32

from ..rcl_interfaces.builtin_interfaces import Time
from .geometry_msgs import Point32, Quaternion, Transform, Twist, Vector3, Wrench
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


@dataclass
class BatteryState(IdlStruct, typename='BatteryState'):
    class POWER_SUPPLY_STATUS(Enum):
        UNKNOWN = 0
        CHARGING = 1
        DISCHARGING = 2
        NOT_CHARGING = 3
        FULL = 4

    class POWER_SUPPLY_HEALTH(Enum):
        UNKNOWN = 0
        GOOD = 1
        OVERHEAT = 2
        DEAD = 3
        OVERVOLTAGE = 4
        UNSPEC_FAILURE = 5
        COLD = 6
        WATCHDOG_TIMER_EXPIRE = 7
        SAFETY_TIMER_EXPIRE = 8

    class POWER_SUPPLY_TECHNOLOGY(Enum):
        UNKNOWN = 0
        NIMH = 1
        LION = 2
        LIPO = 3
        LIFE = 4
        NICD = 5
        LIMN = 6
        TERNARY = 7
        VRLA = 8

    header: Header
    voltage: float32
    temperature: float32
    current: float32
    charge: float32
    capacity: float32
    design_capacity: float32
    percentage: float32
    power_supply_status: uint8
    power_supply_health: uint8
    power_supply_technology: uint8
    present: bool
    cell_voltage: sequence[float32]
    cell_temperature: sequence[float32]
    location: str
    serial_number: str


@dataclass
class ChannelFloat32(IdlStruct, typename='ChannelFloat32'):
    name: str
    values: sequence[float32]


@dataclass
class CompressedImage(IdlStruct, typename='CompressedImage'):
    header: Header
    format: str
    data: sequence[uint8]


@dataclass
class FluidPressure(IdlStruct, typename='FluidPressure'):
    header: Header
    fluid_pressure: float64
    variance: float64


@dataclass
class Illuminance(IdlStruct, typename='Illuminance'):
    header: Header
    illuminance: float64
    variance: float64


@dataclass
class JointState(IdlStruct, typename='JointState'):
    header: Header
    name: sequence[str]
    position: sequence[float64]
    velocity: sequence[float64]
    effort: sequence[float64]


@dataclass
class Joy(IdlStruct, typename='Joy'):
    header: Header
    axes: sequence[float32]
    buttons: sequence[int32]


@dataclass
class JoyFeedback(IdlStruct, typename='JoyFeedback'):
    class TYPE(Enum):
        LED = 0
        RUMBLE = 1
        BUZZER = 2

    type: uint8
    id: uint8
    intensity: float32


@dataclass
class JoyFeedbackArray(IdlStruct, typename='JoyFeedbackArray'):
    array: sequence[JoyFeedback]


@dataclass
class LaserEcho(IdlStruct, typename='LaserEcho'):
    echoes: sequence[float32]


@dataclass
class LaserScan(IdlStruct, typename='LaserScan'):
    header: Header
    angle_min: float32
    angle_max: float32
    angle_increment: float32
    time_increment: float32
    scan_time: float32
    range_min: float32
    range_max: float32
    ranges: sequence[float32]
    intensities: sequence[float32]


@dataclass
class MagneticField(IdlStruct, typename='MagneticField'):
    header: Header
    magnetic_field: Vector3
    magnetic_field_covariance: array[float64, 9]


@dataclass
class MultiDOFJointState(IdlStruct, typename='MultiDOFJointState'):
    header: Header
    joint_names: sequence[str]
    transforms: sequence[Transform]
    twist: sequence[Twist]
    wrench: sequence[Wrench]


@dataclass
class MultiEchoLaserScan(IdlStruct, typename='MultiEchoLaserScan'):
    header: Header
    angle_min: float32
    angle_max: float32
    angle_increment: float32
    time_increment: float32
    scan_time: float32
    range_min: float32
    range_max: float32
    ranges: sequence[LaserEcho]
    intensities: sequence[LaserEcho]


@dataclass
class PointCloud(IdlStruct, typename='PointCloud'):
    header: Header
    points: sequence[Point32]
    channels: sequence[ChannelFloat32]


@dataclass
class Range(IdlStruct, typename='Range'):
    class RADIATION_TYPE(Enum):
        ULTRASOUND = 0
        INFRARED = 1

    header: Header
    radiation_type: uint8
    field_of_view: float32
    min_range: float32
    max_range: float32
    range: float32
    variance: float32


@dataclass
class RelativeHumidity(IdlStruct, typename='RelativeHumidity'):
    header: Header
    relative_humidity: float64
    variance: float64


@dataclass
class Temperature(IdlStruct, typename='Temperature'):
    header: Header
    temperature: float64
    variance: float64


@dataclass
class TimeReference(IdlStruct, typename='TimeReference'):
    header: Header
    time_ref: Time
    source: str
