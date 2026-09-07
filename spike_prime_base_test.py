"""Standalone base test for the team SPIKE Prime robot."""

from pybricks.parameters import Color
from pybricks.tools import wait

from demorobot import (
    hub,
    left_motor,
    right_motor,
    robot,
)


STRAIGHT_DISTANCE_MM = 300
SQUARE_SIDE_MM = 250
PAUSE_MS = 1000


def announce(message):
    print(message)
    hub.speaker.beep(600, 100)
    wait(300)


def test_straight_back_and_forth(distance_mm=STRAIGHT_DISTANCE_MM):
    announce("Straight test: forward")
    robot.straight(distance_mm)
    wait(PAUSE_MS)
    announce("Straight test: backward")
    robot.straight(-distance_mm)
    wait(PAUSE_MS)


def drive_square(side_mm=SQUARE_SIDE_MM, turn_angle=90):
    direction_name = "right" if turn_angle > 0 else "left"
    announce("Square test: " + direction_name + " turns")
    for side_number in range(1, 5):
        print("Side", side_number)
        robot.straight(side_mm)
        robot.turn(turn_angle)
    wait(PAUSE_MS)


def main():
    hub.light.on(Color.ORANGE)
    test_straight_back_and_forth()
    drive_square(turn_angle=90)
    drive_square(turn_angle=-90)
    robot.stop()
    hub.light.on(Color.GREEN)
    hub.speaker.beep(880, 250)
    print("All base robot tests completed.")


if __name__ == "__main__":
    main()
