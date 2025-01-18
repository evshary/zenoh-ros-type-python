from dataclasses import dataclass

from pycdr2 import IdlStruct
from pycdr2.types import array, uint8


@dataclass
class UUID(IdlStruct, typename='UUID'):
    uuid: array[uint8, 16]
