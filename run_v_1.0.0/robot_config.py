from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase


class RobotConfig:
    def __init__(self):
        self.hub = PrimeHub()
        self.left_drive_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_drive_motor = Motor(Port.E, Direction.CLOCKWISE)
        self.drive_base = DriveBase(
            self.left_drive_motor,
            self.right_drive_motor,
            62.4,
            148,
        )
        self.back_attachment_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.front_attachment_motor = Motor(Port.F, Direction.CLOCKWISE)
        self.left_color_sensor = ColorSensor(Port.C)
        self.right_color_sensor = ColorSensor(Port.D)
