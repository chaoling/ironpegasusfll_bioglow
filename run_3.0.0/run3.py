# Run for Forest Elder and keystone species
# Alignment - cornor of Founder Edition

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

def run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.use_gyro(True)
    db.settings(straight_speed=1080)
    db.settings(straight_acceleration=450)
    db.settings(turn_rate=800)
    db.settings(turn_acceleration=450)
    db.turn(-3)
    db.straight(410)

    # Change the speed slow so we can get the seed
    db.settings(straight_speed=150)
    db.straight(110)
    
    # Raise the support
    db.turn(50)
    db.settings(straight_speed=150)
    db.straight(72)
    db.turn(26)
    
    # Get ready to drop the keystone species
    db.settings(straight_speed=1080)
    db.straight(-100)
    db.turn(-23)
    db.straight(150)

    amBl.run_angle(130, 130)
    amBl.run_angle(100, -130)

    db.straight(-100)
    db.turn(-45)
    db.straight(-650)


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
