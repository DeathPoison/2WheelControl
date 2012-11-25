#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UIDm = "9p19drqHQdS" # Change to your UID

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_master import Master
#from tinkerforge.brick_dc import DC
#from tinkerforge.bricklet_lcd_20x4 import LCD20x4

ipcon = IPConnection(HOST, PORT) # Create IP connection to brickd

master = Master(UIDm) # Create device object

ipcon.add_device(master) # Add device to IP connection

# Get voltage and current from stack (in mV/mA)
voltage = master.get_stack_voltage()
current = master.get_stack_current()
tempera = master.get_chip_temperature()

# Print Voltage, Current and Temperature from Master
print('Stack Voltage: ' + str(voltage/1000.0) + ' V')
print('Stack Current: ' + str(current/1000.0) + ' A')
print('Stack Tempera: ' + str(tempera/10) + ' °C')
