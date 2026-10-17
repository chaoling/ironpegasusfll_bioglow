#This run is incomplete due to the lack of a certain piece
from robot_config import RobotConfig
from pybricks.tools import multitask, wait, StopWatch, run_task
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
db.straight(400)
db.turn(45)
db.straight(375)
db.turn(-45)
amFr.run_angle(1000, 400)
db.straight(100)
amBl.run_angle(1000, 400)
amFr.run_angle(1000, -200)
wait(10)
db.straight(-10)
amFr.run_angle(1000, 200)
db.straight(-80)
db.turn(25)
amFr.run_angle(1000, -400)
db.straight(-800)
