import time
import uuid
from dataclasses import dataclass, field

from pycdr2 import IdlStruct
from pycdr2.types import array, int64, uint8


@dataclass
class Attachment(IdlStruct, typename='Attachment'):
    """
    rmw_zenoh attachment (33 bytes).

    - sequence_number: 8 bytes, little-endian int64
    - timestamp_ns: 8 bytes, little-endian int64
    - gid_length: 1 byte (always 16)
    - gid: 16 bytes

    Source: https://github.com/ros2/rmw_zenoh/blob/humble/docs/design.md

    Usage:
        attachment = Attachment()
        data = attachment.serialize()  # auto increment sequence_number and timestamp
        data = attachment.serialize(increase=False)  # only update timestamp
    """

    sequence_number: int64 = field(default=0)
    timestamp_ns: int64 = field(default=0)
    gid_length: uint8 = 16
    gid: array[uint8, 16] = field(default_factory=lambda: list(uuid.uuid4().bytes))

    def serialize(self, increase: bool = True) -> bytes:
        # Optionally increment sequence number
        if increase:
            self.sequence_number += 1
        # Auto-update timestamp on serialize
        self.timestamp_ns = time.time_ns()
        # Strip the 4-byte CDR header added by pycdr2 (rmw_zenoh expects raw bytes)
        return super().serialize()[4:]

    @classmethod
    def deserialize(cls, data: bytes) -> 'Attachment':
        # Prepend CDR header for pycdr2 to parse
        # \x00\x01\x00\x00 = little-endian, CDR version 1, options 0
        cdr_data = b'\x00\x01\x00\x00' + data
        return super(Attachment, cls).deserialize(cdr_data)


@dataclass
class Empty(IdlStruct, typename='Empty'):
    # rmw_zenoh does not accept 0-byte payload, requires 1 byte padding
    padding: uint8 = 0
