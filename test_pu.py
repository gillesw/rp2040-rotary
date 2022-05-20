from machine import Pin
import time

sw=Pin(18,Pin.IN,Pin.PULL_UP)

while(1):
    print(sw.value())
    time.sleep(0.5)