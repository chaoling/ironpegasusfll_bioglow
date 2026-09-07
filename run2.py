"""Attachment motor and color sensor check."""

from pybricks.parameters import Stop
from pybricks.tools import wait


ATTACHMENT_SPEED_DEG_S = 300
ATTACHMENT_ANGLE_DEG = 90


async def run2(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    """Move both attachments and report readings from both color sensors."""
    from robot import left_color_sensor, right_color_sensor

    print("Run 2: attachment and sensor check")
    await hub.speaker.beep(700, 100)

    await attachment_motor_left.run_angle(
        ATTACHMENT_SPEED_DEG_S,
        ATTACHMENT_ANGLE_DEG,
        then=Stop.HOLD,
    )
    await attachment_motor_left.run_angle(
        ATTACHMENT_SPEED_DEG_S,
        -ATTACHMENT_ANGLE_DEG,
        then=Stop.HOLD,
    )
    await attachment_motor_front.run_angle(
        ATTACHMENT_SPEED_DEG_S,
        ATTACHMENT_ANGLE_DEG,
        then=Stop.HOLD,
    )
    await attachment_motor_front.run_angle(
        ATTACHMENT_SPEED_DEG_S,
        -ATTACHMENT_ANGLE_DEG,
        then=Stop.HOLD,
    )

    print("Left color:", left_color_sensor.color())
    print("Right color:", right_color_sensor.color())
    await wait(500)
    print("Run 2 completed.")
