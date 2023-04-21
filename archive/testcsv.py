import serial
from time import sleep
from datetime import datetime

ser = serial.Serial('/dev/ttyAMA0', 9600)

while True:

    line = "index, timestamp, data\n"
    for i in range(0,10):

        received_data = ser.read()
        sleep(0.03)
        data_left = ser.inWaiting()
        received_data += ser.read(data_left)

        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")

        datastr = str(received_data)

        entry = str(i) + ", " + timestamp + ", " + datastr + " \n"
        line += entry
        print(entry)
        
        #ser.write(received_data)

    with open("data.csv", "w") as file:
        file.write(line)
