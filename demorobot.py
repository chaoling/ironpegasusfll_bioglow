"""Shared hardware setup for the team SPIKE Prime robot."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase


WHEEL_DIAMETER_MM = 62.4
AXLE_TRACK_MM = 130

STRAIGHT_SPEED_MM_S = 250
STRAIGHT_ACCEL_MM_S2 = 500
TURN_RATE_DEG_S = 120
TURN_ACCEL_DEG_S2 = 240


hub = PrimeHub()

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER_MM,
    axle_track=AXLE_TRACK_MM,
)
robot.settings(
    STRAIGHT_SPEED_MM_S,
    STRAIGHT_ACCEL_MM_S2,
    TURN_RATE_DEG_S,
    TURN_ACCEL_DEG_S2,
)
robot.use_gyro(True)

attachment_motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
attachment_motor_front = Motor(Port.B, Direction.CLOCKWISE)
left_color_sensor = ColorSensor(Port.A)
right_color_sensor = ColorSensor(Port.E)
