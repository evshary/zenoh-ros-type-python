from ..geographic_info.geographic_msgs import GeoPointStamped
from ..common_interfaces.geometry_msgs import PoseWithCovarianceStamped, TwistWithCovarianceStamped, AccelWithCovarianceStamped

@dataclass
class VehicleKinematics(IdlStruct, typename="VehicleKinematics"):
    geographic_pose: GeoPointStamped
    pose: PoseWithCovarianceStamped
    twist: TwistWithCovarianceStamped
    accel: AccelWithCovarianceStamped