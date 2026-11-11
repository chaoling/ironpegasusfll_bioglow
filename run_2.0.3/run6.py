from pybricks.tools import wait

def safe_turn(db, angle, absolute=False):
    db.turn(angle, absolute=absolute, wait=False)
    while not db.done():
        if db.stalled():
            db.stop()
            wait(100)
            return False
        wait(10)
    return True

def run6(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.use_gyro(True)
    db.settings(straight_speed=1080)
    db.settings(turn_rate=803)
    db.straight(770)
    amBl.run_angle(700, -550)
    db.straight(-83)
    safe_turn(db, -88)
    db.straight(320)
    db.settings(straight_speed=90)
    safe_turn(db, 135)
    db.straight(290)
    db.settings(straight_speed=1080)
    db.straight(-80)
    safe_turn(db, 93)
    db.straight(800)
    safe_turn(db, 45)
    db.straight(250)

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
    run6(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
