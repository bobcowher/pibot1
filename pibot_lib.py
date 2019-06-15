from time import sleep
import atexit
from Raspi_MotorHAT import Raspi_MotorHAT

mh = Raspi_MotorHAT(addr=0x6f)

lm = mh.getMotor(1)
rm = mh.getMotor(2)


def turn_off_motors():
    lm.run(Raspi_MotorHAT.RELEASE)
    rm.run(Raspi_MotorHAT.RELEASE)

def forward(sleep_time):
    lm.setSpeed(150)
    rm.setSpeed(150)
    lm.run(Raspi_MotorHAT.FORWARD)
    rm.run(Raspi_MotorHAT.FORWARD)
    sleep(sleep_time)
    turn_off_motors()

def back(sleep_time):
    lm.setSpeed(150)
    rm.setSpeed(150)
    lm.run(Raspi_MotorHAT.BACKWARD)
    rm.run(Raspi_MotorHAT.BACKWARD)
    sleep(sleep_time)
    turn_off_motors()

def turn_left():
    lm.setSpeed(50)
    rm.setSpeed(50)
    lm.run(Raspi_MotorHAT.FORWARD)
    rm.run(Raspi_MotorHAT.BACKWARD)
    sleep(0.25)
    turn_off_motors()

def turn_right():
    lm.setSpeed(50)
    rm.setSpeed(50)
    lm.run(Raspi_MotorHAT.BACKWARD)
    rm.run(Raspi_MotorHAT.FORWARD)
    sleep(0.25)
    turn_off_motors()


atexit.register(turn_off_motors)



