from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.tools import multitask, wait, StopWatch, run_task

def run9(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.settings(straight_speed=1080)
    db.straight(190)
    amBl.run_angle(400, 170)
    amBl.run_angle(300, -130)
    db.straight(50)
    amBl.run_angle(500, 125)
    amBl.run_angle(500, -120)
    amBl.run_angle(500, 125)
    amBl.run_angle(500, -120)
    amBl.run_angle(500, 125)
    amBl.run_angle(500, -120)
    db.straight(-230)

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
    run9(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)