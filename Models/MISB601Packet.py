#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.Checksum import Checksum
from Models.LSUniversalKey import LSUniversalKey
from Models.UASLSPacket import UASLSPacket


class MISB0601Packet:
    def __init__(self):
        self._ls_universal_key = LSUniversalKey()
        self._length: int = None
        self._data: dict[UASLSPacket] = dict()

    def add_data(self, data: UASLSPacket):
        self._data[str(data.get_key())] = data

    def get_datas(self):
        datas: str = ''
        for key, value in self._data.items():
            if '1' != key:
                datas += str(value)
        return datas

    def __str__(self):
        datas: str = self.get_datas()

        # compute chacksum
        if '1' not in datas or not self._data.get('1'):
            self._data['1'] = Checksum(
                bytearray.fromhex(str(self._ls_universal_key)) +
                bytearray.fromhex(f'{int(len(datas)/2 + 2):02X}') +
                bytearray.fromhex(datas) +
                bytearray.fromhex('0102'))

        datas += str(self._data.get('1'))

        return str(self._ls_universal_key) + f'{int(len(datas)/2):02X}' + datas
