from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import int8, int32, sequence

from ..unique_identifier_msgs import UUID


@dataclass
class FibonacciSendGoal(IdlStruct, typename='FibonacciSendGoal'):
    goal_id: UUID
    goal: int32


@dataclass
class FibonacciResult(IdlStruct, typename='FibonacciResult'):
    class STATUS(Enum):
        STATUS_UNKNOWN = 0
        STATUS_ACCEPTED = 1
        STATUS_EXECUTING = 2
        STATUS_CANCELING = 3
        STATUS_SUCCEEDED = 4
        STATUS_CANCELED = 5
        STATUS_ABORTED = 6

    status: int8
    sequence: sequence[int32]


@dataclass
class FibonacciFeedback(IdlStruct, typename='FibonacciFeedback'):
    goal_id: UUID
    partial_sequence: sequence[int32]
