from robot_config import RobotConfig

robot = RobotConfig()
db = robot.drive_base
amBl = robot.back_attachment_motor
amFr = robot.front_attachment_motor

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=300)
db.settings(turn_rate=960)
db.settings(turn_acceleration=450)
db.turn(-3, absolute=True)
db.straight(590)
db.settings(straight_acceleration=450)
db.turn(-15, absolute=True)
db.straight(68)
db.turn(-57, absolute=True)
db.settings(straight_speed=1080)
db.turn(0, absolute=True)
db.straight(-600)
db.arc(-120, angle=48)
db.straight(338)
amBl.run_angle(1000, 270)
db.straight(-200)
db.turn(15, absolute=False)
db.straight(-400)
