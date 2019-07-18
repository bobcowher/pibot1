from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM

class Servos(object):
    def __init__(self, addr=0x6f, deflect_90_in_ms = 1.15):
        """addr: The i2c address of the PWM chip.
        deflect_90_in_ms: set this to calibrate the servo motors. It is what a deflection of 90 degrees is in turns of a pulse length in milliseconds.
        """
        # deflect_90_in_ms - set this to calibrate the servo motors.
        self._pwm = PWM(addr)
        pwm_frequency = 60
        self._pwm.setPWMFreq(pwm_frequency)

        period_in_ms = 1000 / pwm_frequency

        pulse_steps = 4096.0

        servo_mid_point_ms = 1.5

        # Steps for every millisecond
        steps_per_ms = pulse_steps / period_in_ms

        self.steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90.0

        # Mid  point of the servo in steps
        self.servo_mid_point_steps = servo_mid_point_ms * steps_per_ms

    def stop_all(self):
        #0 in start is nothing, 4096 sets the off bit.
        self._pwm(0, 0, 4096)
        self._pwm(1, 0, 4096)
        self._pwm(14, 0, 4096)
        self._pwm(15, 0, 4096)
    
    def convert_degrees_to_pwm(position):
        return int(self.servo_mid_point_steps + (position * self.steps_per_degree))

    def set_servo_angle(self, channel, angle):
        """position: The position in degrees from the center. -90 to 90"""
        if angle > 90 or angle < -90:
            raise ValueError("Angle outside of range")
        off_step = self._convert_degrees_to_pwm(angle)
        self._pwm.setPWM(channel, 0, off_step)
