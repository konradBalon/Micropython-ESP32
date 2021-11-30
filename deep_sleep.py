

import machine
from machine import Pin
from time import sleep


def main():

    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print('woke from a deep sleep')

    # set base clock to 240 MHz
    machine.freq(240000000)

    # set internal blue led
    led = Pin (2, Pin.OUT)

    # put your main code here:
    #blink LED
    led.value(1)
    sleep(2)
    led.value(0)
    sleep(1)

    # wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
    # you should remove this sleep line in your final script
    sleep(5)

    print('Im awake, but Im going to sleep')

    #sleep for 10 seconds (10 seconds)
    machine.deepsleep(10000)

