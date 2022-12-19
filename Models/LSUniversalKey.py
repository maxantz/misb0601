#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class LSUniversalKey:
    def __init__(self):
        self._value = bytearray.fromhex('060E2B34020B01010E01030101000000')

    def __str__(self):
        return self._value.hex().upper()
