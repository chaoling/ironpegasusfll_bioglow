from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.tools import multitask, wait, StopWatch, run_task

def run6(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.use_gyro(True)
    db.settings(straight_speed=1080)
    db.settings(turn_rate=803)
    db.straight(806)
    amBl.run_angle(600, 540)
    db.straight(-63)
    db.straight(-50)
    amBl.run_angle(500, -550)
    db.turn(-88)
    db.straight(320)
    db.settings(straight_speed=90)
    db.turn(135)
    db.settings(straight_speed=80)
    db.straight(300)
    db.settings(straight_speed=1080)
    db.straight(-80)
    db.turn(93)
    db.straight(800)
    db.turn(45)
    db.straight(250)

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
    run6(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)