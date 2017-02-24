import serial
from Find_serial_ports import serial_ports

port_names = serial_ports()
print(port_names)
print(type(port_names))
for name in port_names:
    try:
        ser = serial.Serial('%s', 9600) % name
        
        print('connected to device')
    except:
        print("could not connect to device")
        print(type(name))
        print(name)
# ser = serial.Serial
