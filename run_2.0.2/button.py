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
db = DriveBase(dmA, dmE, 62.4, 148)
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


def wait_for_imu(hub):
    """Keep the robot still until the IMU is calibrated and ready."""
    hub.display.char("G")
    while not hub.imu.ready():
        wait(100)


def run_selected(selected):
    if selected in GYRO_RUNS:
        wait_for_imu(prime_hub)
        db.use_gyro(True)
    else:
        db.use_gyro(False)

    RUNS[selected](prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    db.stop()
    db.use_gyro(False)

while True:
    selected = hub_menu(*RUNS.keys())
    run_selected(selected)

