from machine import Pin
import utime as time
import micropython

clk=18
dt=19
sw=20

clk_pin=Pin(clk,Pin.IN,Pin.PULL_UP)
dt_pin=Pin(dt,Pin.IN,Pin.PULL_UP)
sw_pin=Pin(sw,Pin.IN,Pin.PULL_UP)

while(1):
    print(bin((dt_pin.value() << 1)|clk_pin.value()))
    time.sleep(0.1)