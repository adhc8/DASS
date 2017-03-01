import serial
import glob
import sys

class DeviceOnPorts:

    def __init__(self, Baud_rate):
        self.Baud_rate = Baud_rate
        self.portName = []

    def serial_ports(self):

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        for port in ports:
            try:
                s = serial.Serial(port, self.Baud_rate)
                s.close()
                self.portName.append(port)
            except (OSError, serial.SerialException):
                pass


class move_to_pos_target:
    def __init__(self, portName):
            self.portName = portName
            ser = serial.Serial(self.portName)
            xyz_coord = ser.readline()
            xyz_coord = str.split(xyz_coord,',')
            while len(xyz_coord) < 5:
                xyz_coord = ser.readline()
                xyz_coord = str.split(xyz_coord,',')
            self.x_diff = float(xyz_coord[1])-x_centre
            self.y_diff = float(xyz_coord[2])-y_centre
            self.z = float(xyz_coord[3])
            self.w = float(xyz_coord[4])
            self.h = float(xyz_coord[5])

    def guess_dist(self)

dev1=DeviceOnPorts(9600)

print(dev1.serial_ports())
