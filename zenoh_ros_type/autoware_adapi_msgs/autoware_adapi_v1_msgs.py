from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import int64, sequence, uint16

from ..common_interfaces.geometry_msgs import AccelWithCovarianceStamped, Pose, PoseWithCovarianceStamped, TwistWithCovarianceStamped
from ..common_interfaces.std_msgs import Header
from ..geographic_info.geographic_msgs import GeoPointStamped


@dataclass
class VehicleKinematics(IdlStruct, typename='VehicleKinematics'):
    geographic_pose: GeoPointStamped
    pose: PoseWithCovarianceStamped
    twist: TwistWithCovarianceStamped
    accel: AccelWithCovarianceStamped


@dataclass
class ResponseStatus(IdlStruct, typename='ResponseStatus'):
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
    code: uint16
    message: str


@dataclass
class ChangeOperationModeResponse(IdlStruct, typename='ChangeOperationModeResponse'):
    status: ResponseStatus


@dataclass
class RoutePrimitive(IdlStruct, typename='RoutePrimitive'):
    id: int64
    type: str


@dataclass
class RouteSegment(IdlStruct, typename='RouteSegment'):
    preferred: RoutePrimitive
    alternatives: sequence[RoutePrimitive]


@dataclass
class RouteData(IdlStruct, typename='RouteData'):
    start: Pose
    goal: Pose
    segments: sequence[RouteSegment]


@dataclass
class Route(IdlStruct, typename='Route'):
    header: Header
    data: sequence[RouteData]


@dataclass
class RouteOption(IdlStruct, typename='RouteOption'):
    allow_goal_modification: bool


@dataclass
class SetRoutePointsRequest(IdlStruct, typename='SetRoutePointsRequest'):
    header: Header
    option: RouteOption
    goal: Pose
    waypoints: sequence[Pose]


@dataclass
class SetRoutePointsResponse(IdlStruct, typename='SetRoutePointsResponse'):
    status: ResponseStatus


@dataclass
class ClearRouteResponse(IdlStruct, typename='ClearRouteResponse'):
    status: ResponseStatus
