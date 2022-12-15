#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class Mission(UASLSPacket):
    def __init__(self, mission: str):
        super().__init__()
        self._key = 3
        self._length = min(len(mission), 126)
        self._value = bytearray(mission[0:self._length].encode('utf-8'))

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
