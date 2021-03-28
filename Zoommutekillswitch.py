import usb_hid
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

while True:
    if cpx.button_a: #Mute Command
        kbd.send(Keycode.ALT,Keycode.CONTROL,Keycode.SHIFT) 
        kbd.send(Keycode.ALT,Keycode.A) 
        while cpx.button_a: # Wait for button to be released
            pass
    if cpx.button_b: #Killswitch
        kbd.send(Keycode.ALT,Keycode.CONTROL,Keycode.SHIFT) 
        kbd.send(Keycode.ALT,Keycode.Q) 
        kbd.send(Keycode.ENTER)
        while cpx.button_b: # Wait for button to be released
            pass