import serial
import struct
import time

import numpy as np

def record():
    s = serial.Serial(port='COM3', baudrate=9600)
    max = 0.0
    y_accels = []
    t_stamps = []
    start_time = time.time()
    try:

        for i in range(100):
            s.readline()

        while True:
            res = s.readline()
            res = res.strip().decode('utf-8', 'ignore')
            print(res)
            print(time.time())
            y_accels.append(float(res))
            t_stamps.append(time.time() - start_time)
            
    except KeyboardInterrupt:
        pass

    s.close()
    return t_stamps, y_accels

def main():
    record()

    
if __name__== '__main__':
    main()