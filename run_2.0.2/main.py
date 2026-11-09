from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop, Color, Button
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, wait, StopWatch, run_task
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

# The main program starts here.
"""
Assign values for colors
red = 0
yellow = 1
green = 2
blue = 3
magenta = 4

Assign Values for runs
       L,R
run1 = 0,0
run2 = 0,1
run3 = 0,2
run4 = 0,3
run5 = 0,4
run6 = 1,0
run7 = 1,1
run8 = 1,2
run9 = 1,3
"""

prime_hub.system.set_stop_button(Button.BLUETOOTH)
while True:
    if csCl.color() == Color.RED and csDr.color() == Color.RED: #00, 1
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(01)
        run1(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.RED and csDr.color() == Color.YELLOW: #01, 2
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(02)
        run2(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.RED and csDr.color() == Color.GREEN: #02, 3
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(03)
        run3(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.YELLOW and csDr.color() == Color.YELLOW: #11, 4
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(04)
        run4(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.YELLOW and csDr.color() == Color.GREEN: #12, 5
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(05)
        run5(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.YELLOW and csDr.color() == Color.BLUE: #13, 6
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(06)
        run6(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.YELLOW and csDr.color() == Color.MAGENTA: #14, 7
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(07)
        run7(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.GREEN and csDr.color() == Color.GREEN: #22, 8
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(08)
        run8(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)
    elif csCl.color() == Color.GREEN and csDr.color() == Color.BLUE: #23, 9
        while not Button.CENTER in prime_hub.buttons.pressed():
            wait(0)
        prime_hub.display.number(09)
        run9(prime_hub, dmA, dmE, db, amBl, amFr, csCl, csDr)