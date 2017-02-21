from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative, CommandSequence
from pymavlink import mavutil # Needed for command message definitions
import time
import math


#Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Control Copter and send commands in GUIDED mode ')
parser.add_argument('--connect',
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

#Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()


# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)

# Get Vehicle Home location - will be `None` until first set by autopilot
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    if not vehicle.home_location:
        print " Waiting for home location ..."
        time.sleep(1)

# We have a home location.
print "\n Home location: %s" % vehicle.home_location


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print "Basic pre-arm checks"
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

    print "Arming motors"
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: #Trigger just below target alt.
            print "Reached target altitude"
            break
        time.sleep(1)

#Arm and take of to altitude of specified meters
arm_and_takeoff(1)

def condition_yaw(heading, relative=False):
    if relative:
        is_relative=1 #yaw relative to direction of travel
    else:
        is_relative=0 #yaw is an absolute angle
# create the CONDITION_YAW command using command_long_encode()
    msg = vehicle.message_factory.command_long_encode(
        0, 0,   #target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0,        #confirmation
        heading,      #param 1, yaw in degrees
        10,       #param 2, yaw speed deg/s
        1,        #param 3, direction -1 ccw, 1 cw
        is_relative,        #param 4, relative offset 1, absolute angle 0
        0, 0, 0)    #param 5-7 not used
#send command to vehicle
    vehicle.send_mavlink(msg)

# Sends a move command that goes nowhere so drone can Yaw after startup
vehicle.simple_goto(vehicle.home_location)
time.sleep(1)

for x in range(0,37):
    target = open("coordinates.txt", "r")
    targ = target.read()
    #int_target = int(targ)
    if targ == "":
        condition_yaw(x * 10)
        time.sleep(1)
        print "Direction is:  ", vehicle.heading
    if targ != "":
        print "Target aquired"
        break

time.sleep(1)
print "New direction is:  ", vehicle.heading

print "Current Alt is:  ", vehicle.location.global_relative_frame.alt
time.sleep(1)

print "Ready to Land!"
vehicle.mode = VehicleMode("LAND")
print "Landed!"

time.sleep(5)
print "New Alt is:  ", vehicle.location.global_relative_frame.alt
time.sleep(1)

print "Close Vehicle Object"
vehicle.close()

sitl.stop
