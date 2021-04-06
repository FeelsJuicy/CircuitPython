from digitalio import DigitalInOut, Direction, Pull
import board
import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_circuitplayground import cp


kbd = Keyboard(usb_hid.devices)


# button setup
button_1 = DigitalInOut(board.A1)
button_1.direction = Direction.INPUT
button_1.pull = Pull.UP

#LED Setup
led = digitalio.DigitalInOut(board.A3)
led.direction = digitalio.Direction.OUTPUT


#Defining Hotkey to Mute Zooma
def key_press(): ##Defining keypress to send mute command
    kbd.send(Keycode.ALT,Keycode.CONTROL,Keycode.SHIFT)
    kbd.send(Keycode.ALT,Keycode.A)

CURRENT_STATE = False ##setting to false for loop

bootuptime = time.monotonic() ##making when you start the time equal to zero
while True:
    buttonv = int(button_1.value)
    if buttonv == 1: ##if button is pressed in
        print('Muted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == False: ##checking current state so key press will only run once
            key_press()
            cp.play_file("Muted.wav") #play file to confirm mutedaa
            CURRENT_STATE = True ##break out of state loop
        led.value = True ##Led
        time.sleep(.5) ##Sleep so doesnt explode lol

    elif buttonv == 0: ##if button is unpressed
        if CURRENT_STATE == True: ##checking current state so key press will only run once
            key_press()
            cp.play_file("Unmuted.wav") ##play sound to confirm unmuted
            CURRENT_STATE = False
        if CURRENT_STATE == True: ##Break statement so button commands are sent close to button press
          break
        led.value = True
        time.sleep(0.5)
        print('Unmuted',time.monotonic()-bootuptime,buttonv)
        if CURRENT_STATE == True: ##Break statement so button commands are sent close to button press
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
