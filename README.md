2WheelControl
=============

!Note: this is one of my first Python Projects, plz bare with me!

2WheelControl in Python

This application was writen to Controll a two Wheel Robot based on Tinkerforge!

# Requirements

You need the following Tinkerforge Bricks to run this Python Script:

	- 1x Master Brick
	- 2x DC Brick
	- 1x LCD 20x4 Display


Python needs the PyGame Package to run correctly!

And the actually Tinkerforge Python Bindings!

# Start the Robot 

use control.py
python control.py

use Arrow-keys to navigate robot through your Room!

# Changelog v1.8:

 - 0 Initial Version, only Drive :P           - key: arrow up/down
 - 1 Added Velocontrol
 - 2 Added PyGame Control
 - 3 Added Critical Batterie Shutdown
 - 4 Added custom Hz / acceleration settings  - only enable
 - 5 Added left/right control                 - key: arrow left/ight
 - 6 Added reset for left/right control       - key: r
 - 7 Added enable / disable power             - key: e, esc for exit
 - 8 Merged threads! Add Counter for Status   - not Tested!
