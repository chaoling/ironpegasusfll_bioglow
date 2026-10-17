from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up.
prime_hub = PrimeHub()
dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dmE = Motor(Port.E, Direction.CLOCKWISE)
drive_base = DriveBase(dmA, dmE, 62.4, 148)
amBl = Motor(Port.B, Direction.CLOCKWISE)
amFr = Motor(Port.F, Direction.COUNTERCLOCKWISE)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)


# The main program starts here.
drive_base.use_gyro(True)
prime_hub.imu.reset_heading(0)
while not prime_hub.imu.ready():
    wait(0)
drive_base.settings(straight_speed=800)
drive_base.straight(775)
prime_hub.display.number(1)
amFr.dc(100)
amFr.run_angle(600, 60)
prime_hub.display.number(2)
wait(100)
amFr.run_angle(400, -35)
wait(20)
amFr.run_angle(1050, 100)
wait(10)
drive_base.turn(-32)
wait(1000)
drive_base.straight(130)
amBl.dc(50)
amBl.run_angle(800, -360)
drive_base.straight(-150)
drive_base.turn(34)
drive_base.straight(-760)