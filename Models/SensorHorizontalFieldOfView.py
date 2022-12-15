#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class SensorHorizontalFieldOfView(UASLSPacket):
    def __init__(self, hfov: float):
        super().__init__()
        self._key = 16
        self._length = 2
        """
            0000 ->        0
            FFFF ->      180
        """
        if 0.0 <= hfov <= 180.0:
            self._value = bytearray(
                int((hfov / 180.0) * 0xFFFF).to_bytes(self._length, 'big'))
        else:
            self._value = bytearray.fromhex('80000000')

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
