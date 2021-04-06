from digitalio import DigitalInOut, Direction, Pull
import board
import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


kbd = Keyboard(usb_hid.devices)


# button
button_1 = DigitalInOut(board.A1)
button_1.direction = Direction.INPUT
button_1.pull = Pull.UP


led = digitalio.DigitalInOut(board.A3)
led.direction = digitalio.Direction.OUTPUT

def key_press():
    print('Sending shit to Zoom')
    kbd.send(Keycode.ALT,Keycode.CONTROL,Keycode.SHIFT)
    kbd.send(Keycode.ALT,Keycode.A)

CURRENT_STATE = False

bootuptime = time.monotonic()
while True:
    buttonv = int(button_1.value)
    if buttonv == 1:
        print('Muted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == False:
            print('We have just unmuted the button')
            key_press()
            CURRENT_STATE = True
        led.value = True
        time.sleep(.5)

    elif buttonv == 0:
        if CURRENT_STATE == True:
            print('We have just muted the button')
            key_press()
            CURRENT_STATE = False
        led.value = True
        time.sleep(0.5)
        print('Unmuted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == True:
          break  
        led.value = False
        time.sleep(0.5)
        print('Unmuted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == True:
          break
        led.value = True
        time.sleep(0.5)
        print('Unmuted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == True:
          break
        led.value = False
        time.sleep(0.5)
        print('Unmuted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == True:
          break
