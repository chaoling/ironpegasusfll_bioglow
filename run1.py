"""Base drive movement run."""

from pybricks.tools import wait


STRAIGHT_DISTANCE_MM = 300
SQUARE_SIDE_MM = 250
PAUSE_MS = 1000


async def announce(hub, message):
    print(message)
    await hub.speaker.beep(600, 100)
    await wait(300)


async def drive_square(hub, robot, side_mm, turn_angle):
    direction_name = "right" if turn_angle > 0 else "left"
    await announce(hub, "Square test: " + direction_name + " turns")

    for side_number in range(1, 5):
        print("Side", side_number)
        await robot.straight(side_mm)
        await robot.turn(turn_angle)

    await wait(PAUSE_MS)


async def run1(hub, robot, left_motor, right_motor, attachment_motor_left, attachment_motor_front):
    """Drive forward and backward, then test both turn directions."""
    await announce(hub, "Straight test: forward")
    await robot.straight(STRAIGHT_DISTANCE_MM)
    await wait(PAUSE_MS)

    await announce(hub, "Straight test: backward")
    await robot.straight(-STRAIGHT_DISTANCE_MM)
    await wait(PAUSE_MS)

    await drive_square(hub, robot, SQUARE_SIDE_MM, 90)
    await drive_square(hub, robot, SQUARE_SIDE_MM, -90)
    print("Run 1 completed.")
