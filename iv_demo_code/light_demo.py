from pybricks.hubs import PrimeHub
from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor, UltrasonicSensor
from pybricks.tools import wait

# Set up.
prime_hub = PrimeHub()
csc = ColorSensor(Port.C)
dse = UltrasonicSensor(Port.E)


# The main program starts here.
csc.lights.off()
while True:
    if dse.distance() < 100:
        csc.lights.on(100)
        while not dse.distance() >= 400:
            wait(0)
        csc.lights.off()
    else:
        pass