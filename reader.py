import serial
import serial.tools.list_ports
import time
from datetime import datetime

serialPort = None

for port in serial.tools.list_ports.comports():
    if "Serial" in port.description:
        serialPort = serial.Serial(port=port.device, baudrate=9600, timeout=.1, rtscts=False, dsrdtr=False)

fname = "data_" + "final_measurement" #datetime.now().strftime("%H_%M_%S")

with open(fname, "w") as f:
    print("timestamp,outVoltage,inVoltage,batVoltage", file=f)

startTime = time.time() * 1000 # in ms

while(1):
    if(serialPort.in_waiting > 0):
        timeStamp = time.time() * 1000 - startTime
        serialString = serialPort.readline()
        outVoltage, solarVoltage, batteryVoltage = [float(i) for i in serialString.decode('Ascii').strip().split(',')]
        with open(fname, "a") as f:
            print(timeStamp, outVoltage, solarVoltage, batteryVoltage, file=f, sep=",")
        print("OUT:\t", outVoltage)
        print("IN:\t",solarVoltage)
        print("BATTERY:\t",batteryVoltage)
        print("\n")
