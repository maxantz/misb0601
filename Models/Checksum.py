#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class Checksum(UASLSPacket):
    def __init__(self, data: bytearray):
        super().__init__()
        self._key = 1
        self._length = 2
        bcc16 = 0
        i = 1
        for b in data:
            bcc16 += (b << (i % 2))
            i += i
        self._value = bytearray(int(bcc16).to_bytes(self._length, 'big'))

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
