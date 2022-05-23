from rotary import Rotary
import utime as time

rotary = Rotary(18,19,20)
val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
    elif change == Rotary.SW_PRESS:
        print('PRESS')
        val=0
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')
        
rotary.add_handler(rotary_changed)

while True:
    time.sleep(0.1)