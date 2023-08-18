from dataclasses import dataclass
from pycdr2 import IdlStruct,Enum
from pycdr2.types import uint8

@dataclass
class GateMode(IdlStruct, typename="GateMode"):
    class DATA(Enum):
        AUTO = 1
        EXTERNAL = 2
    data: uint8
