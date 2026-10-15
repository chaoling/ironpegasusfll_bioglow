from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

# Set up.
prime_hub = PrimeHub()
amBl = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amFr = Motor(Port.F, Direction.CLOCKWISE)
dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dmE = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(dmA, dmE, 62.4, 148)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)

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
