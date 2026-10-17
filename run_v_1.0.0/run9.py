from robot_config import RobotConfig

# Set up.
robot = RobotConfig()
db = robot.drive_base
amBl = robot.back_attachment_motor
amFr = robot.front_attachment_motor

# The main program starts here.
db.settings(straight_speed=1080)
db.straight(190)
amBl.run_angle(400, 170)
amBl.run_angle(300, -130)
db.straight(50)
amBl.run_angle(500, 125)
amBl.run_angle(500, -120)
amBl.run_angle(500, 125)
amBl.run_angle(500, -120)
amBl.run_angle(500, 125)
amBl.run_angle(500, -120)
db.straight(-230)
