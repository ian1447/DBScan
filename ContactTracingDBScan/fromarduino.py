import serial

try:
    arduino = serial.Serial()
    arduino.port = "COM5"
    arduino.baudrate = 9600
    arduino.open()
except:
    print("Please Check Port")

if arduino.isOpen() and arduino.in_waiting:
    packet = arduino.readline()
    rfid = packet.decode('utf')
    print(rfid)