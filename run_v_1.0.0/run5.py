# imcomplete run just a backup
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, wait, StopWatch, run_task
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
db.settings(straight_speed=1080)
db.settings(turn_rate=800)
db.settings(straight_acceleration=450)
db.settings(turn_acceleration=450)
db.straight(250)
db.turn(90)
db.straight(600)
db.turn(-90)
db.straight(140)
db.settings(turn_rate=200)
db.turn(60)
db.straight(-100)
amFr.run_angle(1000, 360)
