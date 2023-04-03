import machine
import dht
from machine import Pin
from time import sleep

d = dht.DHT11(Pin(4))
r=machine.Pin(2, machine.Pin.OUT)

while True:
    d.measure()
    print("Temperatura = {}" .format(d.temperature()))
    print("Umidade = {}".format(d.humidity()))
    sleep(5)
    
    