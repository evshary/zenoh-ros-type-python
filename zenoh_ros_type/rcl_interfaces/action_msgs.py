from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import int8, sequence

from ..unique_identifier_msgs import UUID
from .builtin_interfaces import Time


@dataclass
class GoalInfo(IdlStruct, typename='GoalInfo'):
    goal_id: UUID
    stamp: Time


@dataclass
class GoalStatus(IdlStruct, typename='GoalStatus'):
    class STATUS(Enum):
        STATUS_UNKNOWN = 0
        STATUS_ACCEPTED = 1
        STATUS_EXECUTING = 2
        STATUS_CANCELING = 3
        STATUS_SUCCEEDED = 4
        STATUS_CANCELED = 5
        STATUS_ABORTED = 6

    goal_info: GoalInfo
    status: int8


@dataclass
class GoalStatusArray(IdlStruct, typename='GoalStatusArray'):
    status_list: sequence[GoalStatus]


@dataclass
class CancelGoalRequest(IdlStruct, typename='CancelGoalRequest'):
    goal_info: GoalInfo


@dataclass
class CancelGoalResponse(IdlStruct, typename='CancelGoalResponse'):
    class RETURN_CODE(Enum):
        ERROR_NONE = 0
        ERROR_REJECTED = 1
        ERROR_UNKNOWN_GOAL_ID = 2
        ERROR_GOAL_TERMINATED = 3

    return_code: int8
    goals_canceling: sequence[GoalInfo]
