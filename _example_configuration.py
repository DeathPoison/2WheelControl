#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "9p19drqHQdS" # Change to your UID

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_dc import DC

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create IP connection to brickd

    dc = DC(UID) # Create device object
    ipcon.add_device(dc) # Add device to IP connection
    # Don't use device before it is added to a connection

    dc.set_pwm_frequency(10000) # Use PWM frequency of 10khz
    dc.set_drive_mode(1) # use 1 = Drive/Coast instead of 0 = Drive/Brake

    dc.enable()
    dc.set_acceleration(5000) # Slow acceleration
    dc.set_velocity(32767) # Full speed forward

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
