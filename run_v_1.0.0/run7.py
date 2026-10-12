from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

# Set up.
prime_hub = PrimeHub()
amBL = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amFR = Motor(Port.F, Direction.CLOCKWISE)
dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dmE = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(dmA, dmE, 62.4, 148)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)


# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=800)
db.straight(500)
db.turn(28)
db.straight(93)
amBL.run_angle(500, 270)
db.turn(-14)
db.straight(-95)
amFR.run_angle(500, -500)
db.straight(61)
amFR.run_angle(600, 125)
db.turn(10)
db.straight(-20)
db.turn(-20)
db.straight(-130)
db.turn(-38)
db.straight(-88)
db.turn(40)
amFR.run_angle(500, -250)
db.straight(-309)
