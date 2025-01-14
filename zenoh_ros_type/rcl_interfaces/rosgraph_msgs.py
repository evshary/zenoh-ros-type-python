from dataclasses import dataclass

from pycdr2 import IdlStruct

from .builtin_interfaces import Time


@dataclass
class Clock(IdlStruct, typename='Clock'):
    clock: Time
