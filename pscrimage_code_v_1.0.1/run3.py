# new attachment for biocentric architecture
#  Finish the mission from side.
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

def run5(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
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
    db.straight(550)
    db.turn(-45)
    db.straight(300)
    db.turn(-45)
    db.settings(straight_speed=180)
    db.straight(93)
    amBl.run_angle(1800, -1400)
    db.straight(-100)
    db.settings(straight_speed=1080)
    amBl.run_angle(1800, 1400)
    db.turn(45)
    db.straight(-50)
    db.turn(26)
    db.straight(250)
    amFr.run_angle(1800,760)
    db.straight(55)
    amFr.run_angle(1800,-130)
    db.straight(-20)
    db.turn(40)
    db.straight(680)

if __name__ == "__main__":
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
    run5(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)