from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.tools import multitask, wait, StopWatch, run_task

def run1(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr):
    db.use_gyro(True)
    db.settings(straight_speed=1000)
    db.settings(turn_rate=800)
    db.settings(turn_acceleration=450)
    db.straight(300)
    db.straight(-200)
    db.turn(60)
    db.straight(285)
    db.turn(-60)
    amBl.run_angle(700,-150)
    db.straight(415)
    wait(200)
    amBl.run_angle(500,80)
    amBl.run_angle(500,-70)
    amBl.run_angle(1800,200)
    db.straight(-300)
    db.turn(55)
    db.straight(350)
    amBl.run_angle(500,-200)
    db.turn(-55)
    db.straight(85)
    amBl.run_angle(1000,80)
    db.straight(-100)
    db.turn(45)
    db.straight(-800)
    



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
    run2(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)