from robot import Robot
from time import sleep

class LineFollowerBehavior:
    def __init__(self, robot, forward_speed, cornering):
        self.robot = robot
        self.forward_speed = forward_speed
        self.cornering = cornering
    
    def when_right_crosses_line(self):
        self.robot.set_right(self.cornering)
        print("Cornering right")

    def when_left_crosses_line(self):
        self.robot.set_left(self.cornering)
        print("Cornering Left")

    def when_right_off_line(self):
        self.robot.set_right(self.forward_speed)

    def when_left_off_line(self):
        self.robot.set_left(self.forward_speed)

    
    def run(self):
        

        self.robot.left_line_sensor.when_line = self.when_left_crosses_line
        self.robot.left_line_sensor.when_line = right_line_sensor_blocked = True

        self.robot.left_line_sensor.when_no_line = self.when_left_off_line
        self.robot.left_line_sensor.when_no_line = right_line_sensor_blocked = False


        self.robot.right_line_sensor.when_line = self.when_right_crosses_line
        self.robot.right_line_sensor.when_line = left_line_sensor_blocked = True

        self.robot.right_line_sensor.when_no_line = self.when_right_off_line
        self.robot.right_line_sensor.when_no_line = left_line_sensor_blocked = False

        if(left_line_sensor_blocked and right_line_sensor_blocked):
            self.robot.set_left(self.cornering)
            self.robot.set_right(self.cornering)
            sleep(0.5)
            self.robot.set_right(self.forward_speed)
            sleep(0.1)

        sleep(0.02)
        self.robot.set_left(self.forward_speed)
        self.robot.set_right(self.forward_speed)
        while True:
            sleep(0.02)

    

bot = Robot()
behavior = LineFollowerBehavior(bot, 30, -40)
behavior.run()