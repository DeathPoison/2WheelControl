#!/usr/bin/env python
#1;2802;0c -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UIDdpl = "9ew"
UIDmaster = "a4JritBT6h5" # Master
UIDdc0 = "ayURiS85oZy" # DC Brick 0
UIDdc1 = "a4LCLTVzFbs" # DC Brick 1

end = 10
i = 1

#ALTE BINDINGS
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_20x4 import LCD20x4
from tinkerforge.brick_dc import DC
from tinkerforge.brick_master import Master

#NEW BINDINGS für GET_CHIP_TEMPERATURE
#from ip_connection import IPConnection
#from bricklet_lcd_20x4 import LCD20x4
#from brick_dc import DC

from time import sleep
import subprocess


# Callback function for position callback (parameter has range -150 to 150)
def cb_position(position):
    print('Position: ' + str(position))
    
# Callback functions for button status
def cb_pressed(i):
    #print('Pressed: ' + str(i))
    if lcd.is_backlight_on():
        lcd.backlight_off()
        if master_slider.get_value() < 100:
            master_slider.set_value(master_slider.get_value() + 1)
    else:
        lcd.backlight_on()

def cb_released(i):
    print('Released: ' + str(i))
   
def DisplayClear():
    lcd.write_line(0, 0, '                    ')
    lcd.write_line(1, 0, '                    ')
    lcd.write_line(2, 0, '                    ')
    lcd.write_line(3, 0, '                    ')

   
if __name__ == "__main__":
    
    # Create IP connection to brickd
    ipcon = IPConnection(HOST, PORT)
    
    # Create device objects
    dc0 = DC(UIDdc0) 
    dc1 = DC(UIDdc1) 
    lcd = LCD20x4(UIDdpl) 
    mst = Master(UIDmaster)

    # Connect to devices
    ipcon.add_device(dc0) 
    ipcon.add_device(dc1) 
    ipcon.add_device(lcd) 
    ipcon.add_device(mst)
    
    while i <= end:

        # Reset Display
        lcd.write_line(0, 8, '              ')
        lcd.write_line(1, 8, '              ')
        lcd.write_line(2, 8, '              ')
        lcd.write_line(3, 10, '            ')

        mstStVol = mst.get_stack_voltage()
        mstTemp = mst.get_chip_temperature()
        dc0InVol = dc0.get_external_input_voltage()
        dc0Temp = dc0.get_chip_temperature()
        dc1InVol = dc1.get_external_input_voltage()
        dc1Temp = dc1.get_chip_temperature()

        # Write to Variables before Display
        lcdline0 = "Master: " + str(mstStVol) + " V // " + str(mstTemp/10) + " °C"
        lcdline1 = "DC #0 : " + str(dc0InVol) + " V // " + str(dc0Temp/10) + " °C"
        lcdline2 = "DC #1 : " + str(dc1InVol) + " V // " + str(dc1Temp/10) + " °C"

        # Write to display
        lcd.write_line(0, 0, lcdline0)
        lcd.write_line(1, 0, lcdline1)
        lcd.write_line(2, 0, lcdline2)
       # lcd.write_line(2, 0, str(aamb))

        print(lcdline0)
        print(lcdline1)
        print(lcdline2)


        lcd.register_callback(lcd.CALLBACK_BUTTON_PRESSED, cb_pressed)

        sleep(1)
        i = i + 1

	#Display off
    DisplayClear()
    lcd.backlight_off()
    #raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()

