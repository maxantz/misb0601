#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class SensorLatitude(UASLSPacket):
    def __init__(self, latitude: float):
        super().__init__()
        self._key = 13
        self._length = 4
        """
            00000000 ->        0
            7FFFFFFF ->       90
            80000000 -> INVALIDE
            80000001 ->      -90
            FFFFFFFF ->       -1
        """
        if 0.0 == latitude:
            self._value = bytearray.fromhex('00000000')
        elif 0.0 < latitude <= 90.0:
            self._value = bytearray(
                int((latitude / 90.0) * 0x7FFFFFFF).to_bytes(self._length, 'big'))
        elif -90.0 <= latitude < 0.0:
            self._value = bytearray(
                int(0x80000000 + ((abs(latitude) / 90.0) * 0x7FFFFFFF)).to_bytes(self._length, 'big'))
        else:
            self._value = bytearray.fromhex('80000000')

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
