from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import uint8


@dataclass
class GateMode(IdlStruct, typename='GateMode'):
    class DATA(Enum):
        AUTO = 0
        EXTERNAL = 1

    data: uint8
