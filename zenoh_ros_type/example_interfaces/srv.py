from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import int64


@dataclass
class AddTwoIntsRequest(IdlStruct, typename='AddTwoIntsRequest'):
    a: int64
    b: int64


@dataclass
class AddTwoIntsReply(IdlStruct, typename='AddTwoIntsReply'):
    sum: int64


@dataclass
class SetBoolRequest(IdlStruct, typename='SetBoolRequest'):
    data: bool


@dataclass
class SetBoolReply(IdlStruct, typename='SetBoolReply'):
    success: bool
    message: str


@dataclass
class TriggerReply(IdlStruct, typename='TriggerReply'):
    success: bool
    message: str
