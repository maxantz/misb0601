#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket
from time import time_ns


class Timestamp(UASLSPacket):
    def __init__(self, timestamp: int = None):
        super().__init__()
        self._key = 2
        self._length = 8
        if not timestamp:
            timestamp = int(time_ns() / 1000)
        self._value = bytearray(timestamp.to_bytes(self._length, 'big'))

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
