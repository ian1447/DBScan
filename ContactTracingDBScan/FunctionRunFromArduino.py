import serial.tools.list_ports
import serial

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist = []

for onePort in ports:
    portlist.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portlist)):
    if (portlist[x].startswith("COM" + str(val))):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
counter = 0
while True:
    sent = serialInst.write(b'A')
    #print(sent)
    #serialInst.write(temp.encode())
    packet = serialInst.readline()
    temp = packet.decode('utf-8')
    counter +=1
    if len(temp) > 3:
        print(temp)
        break
    if counter == 3:
        print("Nothing")
        break
