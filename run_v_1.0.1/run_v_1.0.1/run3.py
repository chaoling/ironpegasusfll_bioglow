from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
prime_hub = PrimeHub()
dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dmE = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(dmA, dmE, 62.4, 130)
amBl = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amFr = Motor(Port.F, Direction.CLOCKWISE)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=300)
db.settings(turn_rate=960)
db.settings(turn_acceleration=450)

db.straight(780)

amFr.run_angle(100, -60)
amFr.run_angle(100, 40)
amFr.run_angle(800, -100)
db.turn(-45, absolute=True)
db.straight(120)
amBl.run_angle(1000, -300)

db.settings(straight_speed=1080)
db.settings(straight_acceleration=450)
db.straight(-100)
db.turn(50, absolute=False)
db.straight(-690)