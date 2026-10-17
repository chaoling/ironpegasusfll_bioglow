from robot_config import RobotConfig

# Set up.
robot = RobotConfig()
db = robot.drive_base
amBl = robot.back_attachment_motor
amFr = robot.front_attachment_motor

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=820)
db.straight(730)
db.turn(55)
db.straight(230)
amBl.run_angle(500, 150)
amBl.run_angle(500, -150)
db.straight(-150)
db.turn(-55)
db.straight(-750)
