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
db.straight(425)
amBl.run_angle(1000, 460)
db.straight(-48)
amBl.run_angle(1000, 45)
db.straight(20)
amBl.run_angle(500, -500)
db.straight(-80)
db.turn(60, absolute=True)
db.straight(255)
db.turn(-88)
db.straight(400)
amFr.run_angle(500, 270)
amFr.run_angle(50, 45)
wait(150)
amFr.run_angle(35, -40)
amFr.run_angle(1000, -250)
db.straight(-170)
db.turn(20)
db.straight(-600)
