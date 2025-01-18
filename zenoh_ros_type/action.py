from dataclasses import dataclass

from pycdr2 import IdlStruct

from .rcl_interfaces import Time
from .unique_identifier_msgs import UUID


@dataclass
class ActionSendGoalResponse(IdlStruct, typename='ActionSendGoalResponse'):
    accept: bool
    timestamp: Time


@dataclass
class ActionResultRequest(IdlStruct, typename='ActionResultRequest'):
    goal_id: UUID
