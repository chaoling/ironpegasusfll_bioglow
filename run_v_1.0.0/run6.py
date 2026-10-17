from robot_config import RobotConfig

# Set up.
robot = RobotConfig()
db = robot.drive_base
amBl = robot.back_attachment_motor
amFr = robot.front_attachment_motor

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=803)
db.straight(806)
amBl.run_angle(600, 540)
db.straight(-63)
db.straight(-50)
amBl.run_angle(500, -550)
db.turn(-88)
db.straight(320)
db.settings(straight_speed=90)
db.turn(135)
db.settings(straight_speed=80)
db.straight(300)
db.settings(straight_speed=1080)
db.straight(-80)
db.turn(93)
db.straight(800)
db.turn(45)
db.straight(250)
