from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task
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
selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "8", "9")

while True:    
    if selected == "1":
        run1(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("2", "3", "4", "5", "6", "7", "8", "9", "1")
    elif selected == "2":
        run2(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("3", "4", "5", "6", "7", "8", "9", "1", "2")
    elif selected == "3":
        run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected=hub_menu("4", "5", "6", "7", "8", "9", "1", "2", "3")
    elif selected == "4":
        run4(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected=hub_menu("5", "6", "7", "8", "9", "1", "2", "3", "4")
    if selected == "5":
        run5(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("6", "7", "8", "9", "1", "2", "3", "4", "5")
    if selected == "6":
        run6(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("7", "8", "9", "1", "2", "3", "4", "5", "6")
    if selected == "7":
        run7(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("8", "9", "1", "2", "3", "4", "5", "6", "7")
    if selected == "8":
        run8(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("9", "1", "2", "3", "4", "5", "6", "7", "8")
    if selected == "9":
        run9(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
        db.use_gyro(False)
        selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "8", "9")

