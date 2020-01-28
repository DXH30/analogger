import os, sys, serial
import serial.tools.list_ports
import lcddriver
from time import *

lcd = lcddriver.lcd()

filename="datalog.txt"
datafile = open(filename, 'ab')
nilaike = 0
ser = serial
while True:
    try:
        ser = serial.Serial(serial.tools.list_ports.comports()[0].device, 115200, timeout=1)
        datafile=open(filename, 'ab')
        while True:
            line = ser.readline()
            # Nampil setiap 10 data sekali
            if ((nilaike % 1000) == 0):
                try:
                    lcd = lcddriver.lcd()
                    datan = line.split(',')
                    y1 = float(datan[0])+float(datan[1])+float(datan[2])
                    y2 = (float(datan[0])+float(datan[2])+100)/(float(datan[1])+float(datan[1])+1)
                    lcd.lcd_display_string("Y1 = "+str(round(y1,3)), 1)
                    lcd.lcd_display_string("Y2 = "+str(round(y2,3)), 2)
                except Exception as e:
                    print(e)
            datafile.write(line)
            nilaike = nilaike + 1
        datafile.close()
        ser.close()
    except KeyboardInterrupt:
        print("Tutup")
        datafile.close()
        ser.close()
        break;
