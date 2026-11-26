# new attachment for biocentric architecture
#  Finish the mission from side.
from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.tools import multitask, wait, StopWatch, run_task

def run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    async def turn_arm():
        await multitask(
            amBl.run_angle(1800, 930),
            amFr.run_angle(1800,760),
        )
    async def turn_arm2():
        await multitask(
            db.straight(550),
            amBl.run_angle(1800, 400),
        )

    db.use_gyro(True)
    db.settings(straight_speed=1080)
    db.settings(turn_rate=800)
    db.settings(straight_acceleration=450)
    db.settings(turn_acceleration=450)

    run_task(turn_arm2())
    db.turn(-45)
    db.straight(310)
    db.turn(-45)

    # Push nesting platform and compost hatch
    db.settings(straight_speed=480)
    db.straight(99)

    # Push the skylight in
    amBl.run_angle(1800, -930)
    db.straight(-110)
    db.settings(straight_speed=1080)
    db.turn(45)
    db.straight(-50)
    db.turn(24)
    db.straight(250)

    # Get the seed from window to the past
    run_task(turn_arm())
    db.straight(50)
    amFr.run_angle(1800,-130)

    # Back to the base
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
    run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
