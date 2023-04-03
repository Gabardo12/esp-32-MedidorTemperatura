import machine
from time import sleep
r=machine.Pin(2, machine.Pin.OUT)
i= 0
    
while (i <= 5):
    print("ciclo: " + str(i+1))
    r.value(1)
    sleep(.5)
    r.value(0)
    sleep(.1)
    r.value(1)
    sleep(.5)
    r.value(0)
    sleep(.1)
    r.value(1)
    sleep(.5)
    r.value(0)

    i += 1
    
