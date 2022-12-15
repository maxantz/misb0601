#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class SensorTrueAltitude(UASLSPacket):
    def __init__(self, altitude: float):
        super().__init__()
        self._key = 15
        self._length = 2
        if -900 <= altitude <= 19000:
            """
                0000 ->     -900
                FFFF ->    19000
            """
            self._value = bytearray(
                int(((altitude + 900) / 19900) * 0xFFFF).to_bytes(self._length, 'big'))
        else:
            self._value = bytearray.fromhex('8000')

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
