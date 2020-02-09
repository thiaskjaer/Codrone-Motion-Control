import CoDrone
from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import time
import os

#The program starts by pressing the button, which will pair the nearest drone
#While flying, the converted sensor positions are continuosly sent to the drone
#in the same loop the button is being checked for being pressed (Polling loop)
#When it is pressed, the drone lands and disconnects
#The start method is automaticall called again when ended

#The gyroscope gives values in the range -11 to +11, which has to be converted
#To a range from -100 to +100, with a small buffer to prevent too extreme values

#Setup button
GPIO.setmode(GPIO.BOARD)
buttonPin=35
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Make the drone object
drone = CoDrone.CoDrone()

#Make the gyrscope object
sensor = mpu6050(0x68)

#to find serial port:
#dmesg | grep tty
#or ls /dev/ttyUSB*
#cp210x converter

def start():
    
    global drone
    global sensor
    
    print("Start called")

    #Wait for button press
    buttonState=True
    while buttonState==True:
        buttonState=GPIO.input(buttonPin)
        
    #find serial port automatically since it switches sometimes    
    serial = os.popen('ls /dev/ttyUSB*').read().strip()
    drone.pair(drone.Nearest, serial)
    
    print("Fly Called")
    
    pitch = 0
    throttle = 80
    #70
    roll = 0
    buttonState = True

    #While button is not presed, get pitch and roll values, convert and send
    while buttonState==True:
        buttonState=GPIO.input(buttonPin)
        accelerometer_data = sensor.get_accel_data()
        pitch = int(accelerometer_data["x"]*-9.4)
        if pitch>100:
            pitch=100
        roll = int(accelerometer_data["y"]*9.4)
        if roll>100:
            roll=100
        drone.move(roll, pitch, 0, throttle)


    time.sleep(.5)
    print("Land called")

    drone.land()
    drone.disconnect()
    time.sleep(1)

#Using while true loop to avoid placing excessive method calls on stack
#(Like having the start method calling itself would)
while True:
    start()

