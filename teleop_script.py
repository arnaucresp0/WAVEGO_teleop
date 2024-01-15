import serial
import time
import sys
import termios
import tty
import json


ser = serial.Serial("/dev/ttyS0",115200)
dataCMD = json.dumps({'var':"", 'val':0, 'ip':""})

#Move forward:
def forward(speed=100):
	dataCMD = json.dumps({'var':"move", 'val':1})
	ser.write(dataCMD.encode())
	print('robot-forward')
#Move backward:
def backward(speed=100):
	dataCMD = json.dumps({'var':"move", 'val':5})
	ser.write(dataCMD.encode())
	print('robot-backward')
#Turn left:
def left(speed=100):
	dataCMD = json.dumps({'var':"move", 'val':2})
	ser.write(dataCMD.encode())
	print('robot-left')
#Turn right:
def right(speed=100):
	dataCMD = json.dumps({'var':"move", 'val':4})
	ser.write(dataCMD.encode())
	print('robot-right')
#Stop left-right turn:
def stopLR():
	dataCMD = json.dumps({'var':"move", 'val':6})
	ser.write(dataCMD.encode())
	print('robot-stop')
#Stop forward_backward move
def stopFB():
	dataCMD = json.dumps({'var':"move", 'val':3})
	ser.write(dataCMD.encode())
	print('robot-stop')

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    serial_port = serial.Serial('/dev/ttyS0', 115200, timeout=1)  # Adjust port and baudrate as needed
    print("WELCOME TO WAVEGO TELEOP PYTHON SCRIPT:")
    print("Press 'W' to move forward, 'S' to move backward, 'A' to turn left, 'D' to turn right, 'E' to stop all the moves.")
    print("Press 'Q' to quit the program.")

    while True:
        key = get_key()

        if key == 'w':
            #Move forward:
            forward()
        elif key == 's':
            #Move backward:
            backward()
        elif key == 'a':
            #Turn left:
            left()
        elif key == 'd':
            #Turn right:
            right()
        elif key == 'e':
            #Stop all moves:
            stopLR()
            stopFB()
        elif key == 'q':
            #Exit the program:
            print("CLosing the teleop python script.")
            break

    serial_port.close()

if __name__ == "__main__":
    main()