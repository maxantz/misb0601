#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.UASLSPacket import UASLSPacket


class Checksum(UASLSPacket):
    def __init__(self, data: bytearray):
        super().__init__()
        self._key = 1
        self._length = 2

        """
        bcc16 = 0
        for i in range(len(data)):
            bcc16 += data[i] << (8 * ((i + 1) % 2))

        self._value = bytearray(int(bcc16 & 0xFFFF).to_bytes(self._length, 'big'))
        """

        bcc8 = 0
        bcc16 = 0
        for i in range(len(data)):
            if (i + 1) % 2:
                bcc16 = (bcc16 + (data[i] << 8)) % 0xFF00   # trim to 257-65535
            else:
                bcc8 = (bcc8 + data[i]) & 0xFF              # trim to 0-256

        self._value = bytearray(int(bcc16 + bcc8).to_bytes(self._length, 'big'))

    def __str__(self):
        return f'{self._key:02X}{self._length:02X}{self._value.hex().upper()}'
