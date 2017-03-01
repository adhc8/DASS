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

    def calc_x_velocity(self):
        if self.target_info[0] == 0:
            x_vel = 0
        else:
            x_vel = round((self.target_info[0]-x_centre)/2,3)*100 # m/s to one decimal
        return x_vel

    def calc_y_velocity(self):
        if self.target_info[1] == 0:
            y_vel = 0
        else:
            y_vel = round((self.target_info[1]-y_centre)/2,3)*100 #m/s to one decimal
        return y_vel

    def get_angle_to_target(self):
        if self.target_info[2]==0:
            target_angle = -3
        else:
            target_angle = math.atan((self.target_info[0]-x_centre)/self.z)
        return target_angle

    def guess_dist(self):
        if self.target_info[3] == 0:
            guess_distance = 0
        else:
            guess_width = 20 # in cm
            guess_distance = guess_width*self.target_info[3]/const_cm_pix
        return guess_distance

    def target_Area(self):
        if self.target_info[3]==0:
            target_A = 0
        else:
            target_A = self.target_info[3]*self.target_info[4]

        return target_A
