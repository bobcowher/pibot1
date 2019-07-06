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
        self.robot.left_line_sensor.when_no_line = self.when_left_off_line
        self.robot.right_line_sensor.when_line = self.when_right_crosses_line
        self.robot.right_line_sensor.when_no_line = self.when_right_off_line
        self.robot.set_left(self.forward_speed)
        self.robot.set_right(self.forward_speed)
        while True:
            sleep(0.02)

    

bot = Robot()
behavior = LineFollowerBehavior(bot, 30, -40)
behavior.run()