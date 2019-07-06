from time import sleep
import atexit
from Raspi_MotorHAT import Raspi_MotorHAT
from gpiozero import LineSensor

class Robot(object):
    def __init__(self, motorhat_addr=0x6f):
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)

        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)

        atexit.register(self.stop_motors)

        # Setup the line sensors
        self.right_line_sensor = LineSensor(23, queue_len=3, pull_up=True)
        self.left_line_sensor = LineSensor(16, queue_len=3, pull_up=True)

        self.right_line_sensor_stuck = ""
        self.left_line_sensor_stuck = ""



    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)

    def stop_all(self):
        self.stop_motors()

        # Clear sensor handlers
        self.left_line_sensor.when_line = None
        self.left_line_sensor.when_no_line = None
        self.right_line_sensor.when_line = None
        self.right_line_sensor.when_line = None

    def convert_speed(self, speed):
        #Choose the running mode
        mode = Raspi_MotorHAT.RELEASE
        
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD

        output_speed = (abs(speed) * 255) / 100
        return mode, int(output_speed)
    
    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)

        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)

    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)

        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)

    def set_left_line_sensor_stuck(self, stuck):
        self.left_line_sensor_stuck = stuck
    
    def set_right_line_sensor_stuck(self, stuck):
        self.right_line_sensor_stuck = stuck
    