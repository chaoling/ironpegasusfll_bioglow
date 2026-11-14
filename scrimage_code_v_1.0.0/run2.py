from pybricks.tools import wait

def safe_turn(db, angle, absolute=True):
    db.turn(angle, absolute=absolute, wait=False)

    while not db.done():
        if db.stalled():
            db.stop()
            wait(100)
            return False
        wait(10)

    return True

def run2(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.use_gyro(True)
    db.settings(straight_speed=300)
    db.settings(turn_rate=800)
    db.settings(turn_acceleration=450)
    db.straight(590)
    db.settings(straight_acceleration=450)
    safe_turn(db, -15, absolute=True)
    db.straight(90)
    safe_turn(db, -54, absolute=True)
    db.settings(straight_speed=1080)
    safe_turn(db, 0, absolute=True)
    db.straight(-600)
    db.arc(-120, angle=48)
    db.straight(338)
    amBl.run_angle(1000, 270)
    db.straight(-200)
    safe_turn(db, 15, absolute=False)
    db.straight(-400)

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
    run2(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
