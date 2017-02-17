from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
import time
import math
import inspect


m=inspect.getmembers(VehicleMode.__getattribute__)

for i in m: print(m[1])
