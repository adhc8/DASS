from Find_serial_ports import serial_ports
import serial

ser_name=serial_ports()
ser_name=str(ser_name)
print(ser_name)
print(type(ser_name))

ser = serial.Serial(ser_name,9600)

while 1 :
	ser.readline()
