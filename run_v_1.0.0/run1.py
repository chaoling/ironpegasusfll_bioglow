from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
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
db.settings(straight_speed=1080)
db.settings(turn_rate=960)
db.settings(straight_acceleration=450)
db.settings(turn_acceleration=450)
db.straight(425)
amBl.run_angle(1000, 465)
db.straight(-45)
amBl.run_angle(1000, 45)
db.straight(35)
amBl.run_angle(1000, -500)