from pybricks.tools import multitask, wait, run_task

def safe_turn(db, angle, absolute=False):
    db.turn(angle, absolute=absolute, wait=False)
    while not db.done():
        if db.stalled():
            db.stop()
            wait(100)
            return False
        wait(10)
    return True

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
    db.straight(200)
    safe_turn(db, -90)
    run_task(turn_arm())
    safe_turn(db, 90)
    db.straight(510)
    db.straight(-50)
    safe_turn(db, 90)
    db.straight(210)
    safe_turn(db, -90)
    db.settings(straight_speed=1080)
    db.straight(300)
    db.settings(straight_speed=70)
    db.straight(25)
    db.settings(straight_speed=1080)
    db.straight(45)
    amBl.run_angle(1800, -340)
    db.straight(10)
    safe_turn(db, 45)
    db.straight(168)
    amBl.run_angle(500, 200)
    db.straight(100)
    safe_turn(db, -25)
    db.straight(460)

if __name__ == "__main__":
    from pybricks.hubs import PrimeHub
    from pybricks.parameters import Direction, Port
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
    run5(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
