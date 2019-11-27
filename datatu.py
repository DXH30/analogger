import os, sys, serial
import serial.tools.list_ports

while True:
    ser = serial.Serial(serial.tools.list_ports.comports()[2].device, 115200, timeout=1)
    filename="datalog.txt"
    datafile=open(filename, 'ab')
    while True:
        line = ser.readline()
        datafile.write(line)
    datafile.close()
    ser.close()
