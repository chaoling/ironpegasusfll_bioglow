from robot_config import RobotConfig

# Set up.
robot = RobotConfig()
db = robot.drive_base
amBl = robot.back_attachment_motor
amFr = robot.front_attachment_motor

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=800)
db.straight(500)
db.turn(28)
db.straight(93)
amBl.run_angle(500, 270)
db.turn(-14)
db.straight(-95)
amFr.run_angle(500, -500)
db.straight(61)
amFr.run_angle(600, 125)
db.turn(10)
db.straight(-20)
db.turn(-20)
db.straight(-130)
db.turn(-38)
db.straight(-88)
db.turn(40)
amFr.run_angle(500, -250)
db.straight(-309)
