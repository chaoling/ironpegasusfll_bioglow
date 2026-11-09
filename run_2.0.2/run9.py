def run9(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.settings(straight_speed=1080)
    db.straight(290)
    amBl.run_angle(500, 200)
    amBl.run_angle(500, -200)
    db.straight(-250)

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
    run9(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
