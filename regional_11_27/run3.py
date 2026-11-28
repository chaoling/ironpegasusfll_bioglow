from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.tools import multitask, wait, StopWatch, run_task

# New attachment for biocentric architecture
# Finish the biocentric architecture mission from side.

def run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    async def turn_arm():
        await multitask(
            amBl.run_angle(1800, 600), #930 originall
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
    db.settings(straight_acceleration=700)
    db.settings(turn_acceleration=700)
    run_task(turn_arm2())
    db.turn(-45)
    db.straight(310)
    db.turn(-45)
    #=== Lift Nesting Canopy and open Compost ==================================
    db.settings(straight_speed=900)
    db.settings(straight_acceleration=600)
    db.settings(turn_acceleration=600)
    db.straight(99)
    #=== Push in Skylight ======================================================
    amBl.run_angle(1000, -930)
    db.straight(-120)
    db.settings(straight_speed=1080)
    db.turn(45)
    db.straight(-50)
    db.turn(22)
    db.straight(255)
    #=== Collect Window to the Past Seed =======================================
    run_task(turn_arm())
    db.straight(50)
    amFr.run_angle(1800,-130)
    #=== Go to Right Launch Area =============================================
    db.settings(straight_acceleration=700)
    db.settings(turn_acceleration=700)
    db.straight(-35)
    db.turn(40)
    db.straight(700)

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
