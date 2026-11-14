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

def run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.use_gyro(True)
    db.settings(straight_speed=1080)
    db.settings(turn_rate=800)
    db.settings(turn_acceleration=450)
    db.straight(780)
    amFr.run_angle(100, -60)
    amFr.run_angle(100, 40)
    amFr.run_angle(800, -100)
    safe_turn(db, -45)
    db.straight(120)
    amBl.run_angle(1000, -300)
    db.settings(straight_speed=1080)
    db.settings(straight_acceleration=450)
    db.straight(-100)
    safe_turn(db, 50)
    db.straight(-690)

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
    run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
