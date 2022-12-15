#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class UASLSPacket:
    def __init__(self):
        self._key: int = None
        self._length: int = None
        self._value: bytearray = None

    def get_key(self):
        return self._key

    def get_length(self):
        return self._length

    def get_value(self):
        return self._value
