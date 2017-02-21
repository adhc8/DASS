from Find_serial_ports import serial_ports

print(serial_ports())
port_names=serial_ports()
for name in port_names:
	print"The serial port is: ", name
	print(type(name))


# for name in com_names:
# 	print"First Port is: ", name
