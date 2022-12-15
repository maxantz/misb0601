#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class Version(UASLSPacket):
    def __init__(self):
        super().__init__()
        self._key = 65
        self._length = 1
        self._value = bytearray(int(13).to_bytes(self._length, 'big'))

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
