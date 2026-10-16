from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
prime_hub = PrimeHub()
dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dmE = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(dmA, dmE, 62.4, 148)
amBl = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amFr = Motor(Port.F, Direction.CLOCKWISE)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)

# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=300)
db.settings(turn_rate=1080)
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
