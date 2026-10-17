from robot_config import RobotConfig
from pybricks.tools import wait, StopWatch
robot = RobotConfig()
db = robot.drive_base
amBl = robot.back_attachment_motor
amFr = robot.front_attachment_motor

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=800)
db.settings(straight_acceleration=450)
db.settings(turn_acceleration=450)
db.straight(425)
amBl.run_angle(1000, 465)
db.straight(-45)
amBl.run_angle(1000, 45)
db.straight(20)
amBl.run_angle(500, -500)
db.straight(-100)
db.turn(45, absolute=True)
db.straight(375)
db.turn(-90)
db.straight(350)
amFr.run_angle(1000, 300)
db.straight(-50)
amFr.run_angle(25, -50)
wait(550)
amFr.run_angle(25, 50)
db.straight(50)
amFr.run_angle(1000, -300)
db.straight(-170)
db.turn(45)
db.straight(-600)
