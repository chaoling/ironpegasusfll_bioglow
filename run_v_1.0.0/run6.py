from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

# Set up.
prime_hub = PrimeHub()
ambl = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amfr = Motor(Port.F, Direction.CLOCKWISE)
dma = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dme = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(dma, dme, 62.4, 148)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=803)
db.straight(806)
ambl.run_angle(600, 540)
db.straight(-63)
db.straight(-50)
ambl.run_angle(500, -550)
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
