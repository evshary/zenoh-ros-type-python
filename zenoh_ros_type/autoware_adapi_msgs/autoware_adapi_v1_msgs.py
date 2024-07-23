from dataclasses import dataclass
from pycdr2 import IdlStruct, Enum
from ..geographic_info.geographic_msgs import GeoPointStamped
from ..common_interfaces.geometry_msgs import PoseWithCovarianceStamped, TwistWithCovarianceStamped, AccelWithCovarianceStamped

@dataclass
class VehicleKinematics(IdlStruct, typename="VehicleKinematics"):
    geographic_pose: GeoPointStamped
    pose: PoseWithCovarianceStamped
    twist: TwistWithCovarianceStamped
    accel: AccelWithCovarianceStamped

@dataclass
class ResponseStatus(IdlStruct, typename="ResponseStatus"):
    class CODE(Enum):
        # Error codes
        UNKNOWN = 50000
        SERVICE_UNREADY = 50001
        SERVICE_TIMEOUT = 50002
        TRANSFORM_ERROR = 50003
        PARAMETER_ERROR = 50004

        # Warning codes
        DEPRECATED = 60000
        NO_EFFECT = 60001

    success: bool
    code: int
    message: str

@dataclass
class ChangeOperationMode(IdlStruct, typename="ChangeOperationMode"):
    status: ResponseStatus