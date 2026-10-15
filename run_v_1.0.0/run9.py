from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

# Set up.
prime_hub = PrimeHub()
ambl = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amfr = Motor(Port.F, Direction.CLOCKWISE)
dma = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dme = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(dma, dme, 62.4, 148)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)

# The main program starts here.
db.settings(straight_speed=1080)
db.straight(190)
ambl.run_angle(400, 170)
ambl.run_angle(300, -130)
db.straight(50)
ambl.run_angle(500, 125)
ambl.run_angle(500, -120)
ambl.run_angle(500, 125)
ambl.run_angle(500, -120)
ambl.run_angle(500, 125)
ambl.run_angle(500, -120)
db.straight(-230)
