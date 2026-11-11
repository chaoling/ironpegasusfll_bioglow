from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Color, Button
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from run1 import run1
from run2 import run2
from run3 import run3
from run4 import run4
from run5 import run5
from run6 import run6
from run7 import run7
from run8 import run8
from run9 import run9

prime_hub = PrimeHub()
dmA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
dmE = Motor(Port.E, Direction.CLOCKWISE)
db = DriveBase(
    left_motor=dmA,
    right_motor=dmE,
    wheel_diameter=62.4,
    axle_track=148,
)
amBl = Motor(Port.B, Direction.COUNTERCLOCKWISE)
amFr = Motor(Port.F, Direction.CLOCKWISE)
csCl = ColorSensor(Port.C)
csDr = ColorSensor(Port.D)

prime_hub.system.set_stop_button(Button.BLUETOOTH)

RUNS = {
    (Color.RED, Color.RED): (1, run1),
    (Color.RED, Color.YELLOW): (2, run2),
    (Color.RED, Color.GREEN): (3, run3),
    (Color.YELLOW, Color.YELLOW): (4, run4),
    (Color.YELLOW, Color.GREEN): (5, run5),
    (Color.YELLOW, Color.BLUE): (6, run6),
    (Color.YELLOW, Color.MAGENTA): (7, run7),
    (Color.GREEN, Color.GREEN): (8, run8),
    (Color.GREEN, Color.BLUE): (9, run9),
}
GYRO_RUNS = {1, 2, 3, 4, 5, 6, 7, 8}


def read_run_selection():
    """Return a run selection only when both sensors show a known pair."""
    return RUNS.get((csCl.color(), csDr.color()))


def wait_for_stable_selection():
    """Require the same valid sensor pair for three consecutive reads."""
    previous = None
    stable_count = 0

    while True:
        selection = read_run_selection()
        if selection is None:
            previous = None
            stable_count = 0
            prime_hub.display.char("-")
        elif selection == previous:
            stable_count += 1
            if stable_count >= 3:
                return selection
        else:
            previous = selection
            stable_count = 1

        wait(50)


def wait_for_center_press():
    while Button.CENTER not in prime_hub.buttons.pressed():
        wait(10)

    # Release the button before starting the run so it cannot trigger again.
    while Button.CENTER in prime_hub.buttons.pressed():
        wait(10)


def wait_for_imu():
    prime_hub.display.char("G")
    while not prime_hub.imu.ready():
        wait(100)


def prepare_run(run_number):
    """Reset state so each run starts from a known drive-base reference."""
    if run_number in GYRO_RUNS:
        wait_for_imu()
        db.use_gyro(True)
    else:
        db.use_gyro(False)

    db.reset(distance=0, angle=0)


while True:
    run_number, run_function = wait_for_stable_selection()
    prime_hub.display.number(run_number)
    wait_for_center_press()

    prepare_run(run_number)
    run_function(
        prime_hub=prime_hub,
        dmA=dmA,
        dmE=dmE,
        db=db,
        amBl=amBl,
        amFr=amFr,
        csCl=csCl,
        csDr=csDr,
    )
    db.stop()
    db.use_gyro(False)
