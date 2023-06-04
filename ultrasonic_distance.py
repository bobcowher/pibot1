#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# set GPIO Pins
GPIO_TRIGGER = 7
GPIO_ECHO = 11
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    print("Calculating distance")

    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(GPIO_TRIGGER, GPIO.LOW)

    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        print("In the GPIO_ECHO == 1 loop")
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':

    GPIO.output(GPIO_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")

    time.sleep(2)

    try:
        while True:
            dist = distance()
            print(f"Measured Distance {dist}")
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()