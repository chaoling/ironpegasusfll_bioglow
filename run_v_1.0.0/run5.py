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
async def turn_arm():
    await multitask(
        amBl.run_angle(1000, 300),
        db.straight(450),
    )
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=800)
db.settings(straight_acceleration=450)
db.settings(turn_acceleration=450)

db.straight(200)
db.turn(-90)
run_task(turn_arm())
db.turn(90)
db.straight(510)
db.straight(-50)
db.turn(90)
db.straight(205)
db.turn(-90)
db.settings(straight_speed=1080)
db.straight(300)
db.settings(straight_speed=70)
db.straight(22)
db.settings(straight_speed=1080)
db.straight(45)
amBl.run_angle(1800, -340)

db.straight(10)
db.turn(45)
db.straight(168)

amBl.run_angle(500, 200)

db.straight(100)
db.turn(-25)
db.straight(460)