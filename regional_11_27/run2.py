from pybricks.tools import wait

def safe_turn(angle, absolute=False):
    global db
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
    db.settings(straight_speed=1080)
    db.settings(turn_rate=800)
    db.settings(turn_acceleration=450)
    db.straight(10)
    safe_turn(46)
    db.straight(430)
#=== Take seed from Exploding Seeds =============================================
    amBl.run_angle(1000, 265)
    db.settings(straight_speed=900)
    db.straight(-425)
    safe_turn(39)
#=== Lower speed and lift Drone Survey Drone ===================================================
    db.settings(straight_speed=350)
    db.straight(550)
    db.settings(straight_speed=1080)
    db.straight(-600)

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
