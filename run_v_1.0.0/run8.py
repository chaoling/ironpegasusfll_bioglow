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
color_sensor = ColorSensor(Port.C)
color_sensor_2 = ColorSensor(Port.D)


# The main program starts here.
db.use_gyro(True)
db.settings(straight_speed=1080)
db.settings(turn_rate=820)
db.straight(730)
db.turn(55)
db.straight(230)
ambl.run_angle(500, 150)
ambl.run_angle(500, -150)
db.straight(-150)
db.turn(-55)
db.straight(-750)
