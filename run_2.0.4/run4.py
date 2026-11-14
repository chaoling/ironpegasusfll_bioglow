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

def run4(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    async def arm():
        wait(500)
        amFr.run_angle(1000, -400)
    async def lift_arm():
        await multitask(
            arm(), 
            db.straight(-800),
        )
    db.use_gyro(True)
    db.settings(straight_speed=1080)
    db.settings(turn_rate=800)
    db.settings(straight_acceleration=450)
    db.settings(turn_acceleration=450)
    db.straight(320)
    safe_turn(db, 40)
    db.straight(400)
    safe_turn(db, -42)
    amFr.run_angle(1000, 400)
    db.straight(160)
    amFr.run_angle(1000, -200)
    wait(50)
    db.straight(-30)
    amFr.run_angle(1000, 200)
    db.straight(320)
    for i in range(4):
        db.straight(30)
        wait(50)
        db.straight(-30)
        wait(30)
    db.straight(-150)
    safe_turn(db, 30)
    run_task(lift_arm())

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
    run4(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
