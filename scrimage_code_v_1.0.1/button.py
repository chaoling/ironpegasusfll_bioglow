from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Button
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu
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
    "1": run1,
    "2": run2,
    "3": run3,
    "4": run4,
    "5": run5,
    "6": run6,
    "7": run7,
    "8": run8,
    "9": run9,
}
GYRO_RUNS = {"1", "2", "3", "4", "5", "6", "7", "8"}
RUN_ORDER = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


def wait_for_imu(hub):
    """Keep the robot still until the IMU is calibrated and ready."""
    hub.display.char("G")
    while not hub.imu.ready():
        wait(100)


def prepare_run(selected):
    if selected in GYRO_RUNS:
        wait_for_imu(prime_hub)
        db.use_gyro(True)
    else:
        db.use_gyro(False)

    db.reset(distance=0, angle=0)


def run_selected(selected):
    prepare_run(selected)
    RUNS[selected](
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


menu_order = RUN_ORDER

while True:
    selected = hub_menu(*menu_order)
    run_selected(selected)

    # Put the next run first, so it is highlighted when the menu reopens.
    next_index = (RUN_ORDER.index(selected) + 1) % len(RUN_ORDER)
    menu_order = RUN_ORDER[next_index:] + RUN_ORDER[:next_index]
