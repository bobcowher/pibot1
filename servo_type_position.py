from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM
import atexit

pwm = PWM(0x6f)
pwm_frequency = 60
pwm.setPWMFreq(pwm_frequency)


#Frequency is 1/period, but working ms, we can use 1000
period_in_ms = 1000 / pwm_frequency

# The chip has 4096 steps in each period
pulse_steps = 4096.0

# Mid point of the servo pulse length in milliseconds
servo_mid_point_ms = 1.5


# What a deflection of 90 degrees is in pulse length in milliseconds
deflect_90_in_ms = 0.7

# Steps for every millisecond
steps_per_ms = pulse_steps / period_in_ms

# Steps for a degree
steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90.0

# Mid  point of the servo in steps
servo_mid_point_steps = servo_mid_point_ms * steps_per_ms

def convert_degrees_to_pwm(position):
    return int(servo_mid_point_steps + (position * steps_per_degree))


def stop():
    pwm.setPWM(0, 0, 4096)

while(True):
    position = int(raw_input("Type your position in degrees (90 to -90, 0 is middle): "))
    end_step = convert_degrees_to_pwm(position)
    pwm.setPWM(0, 0, end_step)