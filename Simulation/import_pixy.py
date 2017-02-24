import serial
ser = serial.Serial('COM9',9600)

while 1:
	ser.readline()
