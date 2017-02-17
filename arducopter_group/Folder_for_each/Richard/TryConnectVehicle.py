from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
from Find_serial_ports import serial_ports
import time
import math

# com=serial_ports()
# com=str(com)

import argparse
parser = argparse.ArgumentParser(description='Control Copter and send commands in GUIDED mode ')
parser.add_argument('--connect', default = 'COM8')
args = parser.parse_args()

connection_string = args.connect
sitl = None

# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)

if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """
    count=0
    print "Basic pre-arm checks"
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print"In vehicle.is_armable loop"
        str_mode= str(vehicle.mode.name)
        str_GPS = str(vehicle.gps_0.fix_type)
        str_ekf = str(vehicle._ekf_predposhorizabs)
        print"vehicle mode: %s" % str_mode
        print"gps fix type: %s" % str_GPS
        print"EKF type: %s" % str_ekf
        print " Waiting for vehicle to initialise..."
        count=count+1
        break
        time.sleep(1)

    print "Arming motors"
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    print (str(vehicle.armed))

    while not vehicle.armed:
        print"In vehicle.armed loop"
        print"vehicle mode: %s" % str_mode
        print"gps fix type: %s" % str_GPS
        print"EKF type: %s" % str_ekf

        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    count = 1
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: #Trigger just below target alt.
            print "Reached target altitude"
            break
        elif count>15:
            break
        count = count+1
        time.sleep(1)
        print(count)

#Arm and take of to altitude of 5 meters
arm_and_takeoff(0.3)

print("Setting LAND mode...")
vehicle.mode = VehicleMode("LAND")
# Close vehicle object before exiting script
print "Close vehicle object"
vehicle.close()
