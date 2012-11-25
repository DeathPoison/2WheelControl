#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UIDm = "a4JritBT6h5" # Change to your UID
UIDdc0 = "ayURiS85oZy"
UIDlcd = "9ew"

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_master import Master
from tinkerforge.brick_dc import DC
from tinkerforge.bricklet_lcd_20x4 import LCD20x4

# Wegen neuen Bindings jetzt ohne das tinkerforge.
#from ip_connection import IPConnection
#from brick_master import Master
#from brick_dc import DC
#from bricklet_lcd_20x4 import LCD20x4

ipcon = IPConnection(HOST, PORT) # Create IP connection to brickd

master = Master(UIDm) # Create device object
dc0 = DC(UIDdc0)
lcd = LCD20x4(UIDlcd)

ipcon.add_device(master) # Add device to IP connection
ipcon.add_device(dc0)
ipcon.add_device(lcd)

# Get voltage and current from stack (in mV/mA)
voltage = master.get_stack_voltage()
current = master.get_stack_current()
tempera = master.get_chip_temperature()

# Print Voltage, Current and Temperature from Master
print('Stack Voltage: ' + str(voltage/1000.0) + ' V')
print('Stack Current: ' + str(current/1000.0) + ' A')
print('Stack Tempera: ' + str(tempera/10) + ' °C')

# Auslesen des DriveModes und der Temperatur
drive = dc0.get_drive_mode()
temp = dc0.get_chip_temperature()

print('DC Drive Mode: ' + str(drive) + 'Mode')
print('DC Temperature: ' + str(temp/10) + ' °C')
