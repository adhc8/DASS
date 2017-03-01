import math
import serial

# self.target_info = x,y,z,w,h
class engage_target:

    const_cm_pix = 0.44963
    x_centre = 160
    y_centre = 100

    def __init__(self, portName):
        self.portName = portName
        self.target_info = []

        ser = serial.Serial(self.portName)
        xyz_coord = ser.readline()
        xyz_coord = str.split(xyz_coord,',')

        while len(xyz_coord) < 5:
            xyz_coord = ser.readline()
            xyz_coord = str.split(xyz_coord,',')

        for coord in xyz_coord:
            print(val)
            try:
                self.target_info.append(float(coord))
            except:
                self.target_info.append(0)

    def guess_dist(self):
        try:
            guess_width = 20 # in cm
            guess_distance = guess_width*self.target_info[3]/const_cm_pix
        except:
            guess_distance = 100
        return guess_distance

    def calc_x_velocity(self):

        x_vel = round((self.target_info[0]-x_centre)/2,3)*100 # m/s to one decimal
        return x_vel

    def calc_y_velocity(self):
        y_vel = round((self.target_info[1]-y_centre)/2,3)*100 #m/s to one decimal
        return y_vel

    def get_angle_to_target(self):
        if not self.z:
            target_angle = math.atan((self.target_info[0]-x_centre)/self.guess_dist())
        else:
            target_angle = math.atan((self.target_info[0]-x_centre)/self.z)
