"""Physical SPIKE Prime team program and run selector."""

from pybricks.parameters import Button, Color
from pybricks.tools import hub_menu, multitask, run_task, wait

from robot import (
    attachment_motor_front,
    attachment_motor_left,
    hub,
    left_motor,
    right_motor,
    robot,
)
from runs import RUNS


def choose_run():
    """Use the built-in hub menu to select a run from 1 through N."""
    if not RUNS:
        raise ValueError("Add at least one run to runs.py")

    run_number = hub_menu(*range(1, len(RUNS) + 1))
    return run_number, RUNS[run_number - 1]


async def emergency_stop():
    """Stop the robot when the hub Bluetooth button is pressed."""
    while True:
        if Button.BLUETOOTH in hub.buttons.pressed():
            robot.stop()
            hub.light.on(Color.RED)
            await hub.speaker.beep(220, 500)
            return True
        await wait(20)


async def run_selected(run_number, run_program):
    """Run the selected program with an emergency-stop monitor."""
    hub.display.number(run_number)
    stopped = False
    try:
        _, stopped = await multitask(
            run_program(
                hub,
                robot,
                left_motor,
                right_motor,
                attachment_motor_left,
                attachment_motor_front,
            ),
            emergency_stop(),
            race=True,
        )
        if stopped:
            print("Emergency stop pressed.")
    finally:
        robot.stop()
        if not stopped:
            hub.light.on(Color.GREEN)
            await hub.speaker.beep(880, 250)


if __name__ == "__main__":
    hub.light.on(Color.ORANGE)
    selected_run_number, selected_run = choose_run()
    run_task(run_selected(selected_run_number, selected_run))
