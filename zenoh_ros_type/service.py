from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import int64, uint64


@dataclass
class ServiceHeader(IdlStruct, typename='ServiceHeader'):
    guid: int64
    seq: uint64
