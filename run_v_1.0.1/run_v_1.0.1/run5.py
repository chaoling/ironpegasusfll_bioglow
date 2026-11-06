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
        amBl.run_angle(1000, -300),
        db.straight(550),
    )
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=800)
db.settings(straight_acceleration=450)
db.settings(turn_acceleration=450)
"""
run_task(turn_arm())
db.turn(90)
db.straight(625)
db.straight(-70)
db.turn(-90)
amBl.run_angle(1000, -100)
db.straight(-220)
db.turn(90)
db.straight(410)
"""
amBl.run_angle(1000, -140)
db.straight(-40)
amBl.run_angle(50, 60)
wait(75)
amBl.run_angle(100, -125)
db.straight(50)