#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Models.Checksum import Checksum
from Models.LSUniversalKey import LSUniversalKey
from Models.MISB601Packet import MISB0601Packet
from Models.Mission import Mission
from Models.SensorHorizontalFieldOfView import SensorHorizontalFieldOfView
from Models.SensorLatitude import SensorLatitude
from Models.SensorLongitude import SensorLongitude
from Models.SensorTrueAltitude import SensorTrueAltitude
from Models.Timestamp import Timestamp
from Models.Version import Version

from time import strptime
from datetime import datetime, timezone

def main():
    """
    l = LSUniversalKey()
    tmp_l = str(l)
    print(tmp_l)

    t = Timestamp(int(datetime.strptime('2008-10-24T00:13:29.913Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()*1000))
    tmp_t = str(t)
    print(tmp_t)

    m = Mission('MISSION01')
    tmp_m = str(m)
    print(tmp_m)

    la = SensorLatitude(60.176822967)#(48.80363)
    tmp_la = str(la)
    print(tmp_la)

    lo = SensorLongitude(128.426759042)#(2.29022)
    tmp_lo = str(lo)
    print(tmp_lo)

    al = SensorTrueAltitude(14190.72)#(100.584)
    tmp_al = str(al)
    print(tmp_al)

    h = SensorHorizontalFieldOfView(144.5713)
    tmp_h = str(h)
    print(tmp_h)

    v = Version()
    tmp_v = str(v)
    print(tmp_v)

    c = Checksum(bytearray.fromhex(tmp_t) + bytearray.fromhex(tmp_m) + bytearray.fromhex(tmp_la) + bytearray.fromhex(tmp_lo) + bytearray.fromhex(tmp_al) + bytearray.fromhex(tmp_h) + bytearray.fromhex(tmp_v))
    print(c)
    """

    result = MISB0601Packet()
    result.add_data(Timestamp(int(datetime.strptime('2008-10-24T00:13:29.913Z', '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc).timestamp()*1e6)))
    result.add_data(Mission('MISSION01'))
    result.add_data(SensorLatitude(60.176822967))
    result.add_data(SensorLongitude(128.426759042))
    result.add_data(SensorTrueAltitude(14190.72))
    result.add_data(SensorHorizontalFieldOfView(144.5713))
    result.add_data(Version())

    print(result)

if __name__ == '__main__':
    main()
