import serial
import time

def main():
    s = serial.Serial(port='COM3', baudrate=9600)
    try:
        while True:
            time.sleep(0.01)
            res = s.readline()
            print(res)
    except KeyboardInterrupt:
        pass

    s.close()
    
if __name__== '__main__':
    main()