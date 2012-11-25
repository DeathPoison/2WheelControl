#!/usr/bin/env python
#1;2802;0c -*- coding: utf-8 -*-  
# Version 1.7 David Crimi @ deathpoison.dc@gmail.com
#
# Script for drive an 2-DC-Motor Vehicle based on Tinkerforge over SSH
#
# Changelog
# .0 Initial Version, only Drive :P           - key: arrow up/down
# .1 Added Velocontrol
# .2 Added PyGame Control
# .3 Added Critical Batterie Shutdown
# .4 Added custom Hz / acceleration settings  - only enable
# .5 Added left/right control                 - key: arrow left/ight
# .6 Added reset for left/right control       - key: r
# .7 Added enable / disable power             - key: e, esc for exit

HOST = "localhost"
PORT = 4223
UIDdpl = "9ew" # Display
UIDmaster = "9p19drqHQdS" # Master
UIDdc0 = "ayURiS85oZy" # DC Brick 0
UIDdc1 = "a4LCLTVzFbs" # DC Brick 1

#ALTE BINDINGS fuer Tinkerforge - die neuen scheinen nicht zu gehen
# Sollte ich mal wieder ausprobieren
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_20x4 import LCD20x4
from tinkerforge.brick_dc import DC
from tinkerforge.brick_master import Master

#import fuer die steuerung
import pygame, sys
from pygame.locals import *

#import thread um 2 schleifen parallel laufen zu lassen
import thread

#import fuer sleep
from time import sleep
import subprocess

# Erstelle Funktion fuer den ersten Thread
# Er kuemmert sich um das Display und die Statusabfragen
def startStatus():
    thread.start_new_thread(status, ())

# Callback function for position callback (parameter has range -150 to 150)
def cb_position(position):
    print('Position: ' + str(position))
    
# Callback functions for button status
def cb_pressed(i):
    print('Pressed: ' + str(i))
    if lcd.is_backlight_on():
        lcd.backlight_off()
        if master_slider.get_value() < 100:
            master_slider.set_value(master_slider.get_value() + 1)
    else:
        lcd.backlight_on()

def cb_released(i):
    print('Released: ' + str(i))

# Hier wird das Display gesaeubert ;)   
def DisplayClear():
    lcd.write_line(0, 0, '                    ')
    lcd.write_line(1, 0, '                    ')
    lcd.write_line(2, 0, '                    ')
    lcd.write_line(3, 0, '                    ')

# Hier werden sonderwuensche entgegen genommen
def getVars(velol,velor,hz,acc):

    velo = raw_input("Velocity?     std:     0")
    hz   = raw_input("Hz?           std: 18000")
    acc  = raw_input("Acceleration? std: 10000")

    # Hole moeglieche optionen
    if str(velo) >= 1:
        # Übertrage Velo
        velol = velo
        velor = velo
    elif str(velo) == 0:
        # Uebertrage std Wert 0
        velol = 0
        velor = 0

    if hz >= 1:
        # Übertrage hz
        hz = hz
    elif hz == 0:
        # Uebertrage std Wert: 18000
        hz = 18000

    if acc >= 1:
        # Übertrage acc
        acc = acc
    elif acc == 0:
        # Uebertrage std Wert: 10000
        acc = 10000

    return velol,velor,hz,acc


# Hier beginnt die Statusabfrage, aktualisiert sich nur alle 2 sek.
def status():
    while 1:
        # Reset Display
        lcd.write_line(0, 4, '                  ')
        lcd.write_line(1, 4, '                  ')
        lcd.write_line(2, 4, '                  ')
        lcd.write_line(3, 4, '                  ')

        # Hole Stack Informationen
        mstStVol = mst.get_stack_voltage()
        mstTemp = mst.get_chip_temperature()
        dc0Temp = dc0.get_chip_temperature() 
        dc1Temp = dc1.get_chip_temperature()
        dc0InVol = dc0.get_external_input_voltage()
        dc1InVol = dc1.get_external_input_voltage()
        dc0cVelo = dc0.get_current_velocity()
       # dc1cVelo = dc1.get_current_velocity()

        # Get more DC Brick informations
        dc0Con = dc0.get_current_consumption()
        dc1Con = dc1.get_current_consumption()
        dc0Hz = dc0.get_pwm_frequency()
        dc1Hz = dc1.get_pwm_frequency()

        # Shutdown if Batterie is kritical
        if mstStVol >= 5600 or dc0InVol >= 5600 or dc1InVol >= 5600:
                print "Batterie is kritical, stopping this Script!!"
                print "Stopping both DC Bricks!"
                dc0.disable()
                dc1.disable()
                sys.exit()
                DisplayClear()
                lcd.backlight_off()
                sleep(1)
                ipcon.destroy()
        

        # Give me some more informations of DC Bricks!
        lcdline0 = "Mst: " + str(mstStVol) + " V  / " + str(mstTemp/10) + " 'C"
        lcdline1 = "DC0: " + str(dc0Con) + " mA / " + str(dc0Temp/10) + " 'C"
        lcdline2 = "DC1: " + str(dc1Con) + " mA / " + str(dc1Temp/10) + " 'C"
        lcdline3 = "DC0: " + str(dc0InVol) + " V  / " + str(dc0Hz) + " Hz"


#        # Write to Variables before Display
#        lcdline0 = "Master: " + str(mstStVol) + " V // " + str(mstTemp/10) + " °C"
#        lcdline1 = "DC 0  : " + str(dc0InVol) + " V // " + str(dc0Temp/10) + " °C"
#        lcdline2 = "DC 1  : " + str(dc1InVol) + " V // " + str(dc1Temp/10) + " °C"
#        lcdline3 = "Velo DC0: " + str(dc0cVelo) + " // DC1: " + str(dc1cVelo)

        # Write to display
        lcd.write_line(0, 0, lcdline0)
        lcd.write_line(1, 0, lcdline1)
        lcd.write_line(2, 0, lcdline2)
        lcd.write_line(3, 0, lcdline3)

        # Zur sicherheit nochmal in die Konsole
        print(lcdline0)
        print(lcdline1)
        print(lcdline2)
        print(lcdline3)

        # Heisst: Schleife startet alle 2sek.
        sleep(2)

# Hier beginnt die Haupt-Steuer-Funktion!!!!! Laeuft deutlich schneller als Statusabfrage!
def Control(velol,velor,hz,acc):

    # uebernimmt jetzt getVars()
    # Setze velor und velol zurueck
    #velol = 0
    #velor = 0

    # Erstelle Pruefprogramm ob der maxwert erreicht und positiv ist
    def posVelo(vl, vr):
        if vl >= 31000 and vr <= -31000:
            return "false"
        elif vl <= 31000 and vr >= -31000:
            return "true"

    # Erstelle Pruefprogramm ob der maxwert erreicht und negativ ist
    def negVelo(vl, vr):
        if vr >= 31000 and vl <= -31000:
            return "false"
        elif vr <= 31000 and vl >= -31000:
            return "true"


    while 1:

        # Registriert Callbacks... button vom Display gedrueckt? 
        lcd.register_callback(lcd.CALLBACK_BUTTON_PRESSED, cb_pressed)

        # Setze Starndartwert fuer Steuerung
        # clock 5 fuer einzelschritte, 30 fuer fluessige wiederholung
        clock.tick(30)

        #################################################################
        # Der Begin der Steuerung
        # Ermittle gedrueckte Tasten
        key = pygame.key.get_pressed()

        # Move object in 4 directons, with shift turbo
        # Verschiedene Actionen fuer die einzelnden Tasten
        if key[pygame.K_RIGHT]:
            if posVelo(velol, velor) == "true" and negVelo(velol, velor) == "true":
                velol = velol + 100
                velor = velor + 100
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            else:
                print "Max of one DC Brick reached!"
            print "RIGHT is being pressed"

        if key[pygame.K_LEFT]:
            if posVelo(velol, velor) == "true" and negVelo(velol, velor) == "true":
                velol = velol - 100
                velor = velor - 100
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            else:
                print "Max of one DC Brick reached!"
            print "LEFT is being pressed"

        if key[pygame.K_LSHIFT] and key[pygame.K_RIGHT]:
            if posVelo(velol, velor) == "true" and negVelo(velol, velor) == "true":
                velol = velol + 500
                velor = velor + 500
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            else:
                print "Max of one DC Brick reached!"
            print "TURBORIGHT is being pressed"

        if key[pygame.K_LSHIFT] and key[pygame.K_LEFT]:
            if posVelo(velol, velor) == "true" and negVelo(velol, velor) == "true":
                velol = velol - 500
                velor = velor - 500
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            else:
                print "Max of one DC Brick reached!"
            print "TURBOLEFT is being pressed"

        if key[pygame.K_UP]:
            if velol == 0 and velor == 0:
                velol = 15000
                velor = -15000
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            elif posVelo(velol, velor) == "false":
                print "Max Velocity reached!"
            elif posVelo(velol, velor) == "true":
                velol = velol + 100
                velor = velor - 100
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            print "UP is being pressed"

        if key[pygame.K_LSHIFT] and key[pygame.K_UP]:
            if velol == 0 and velor == 0:
                velol = 15000
                velor = -15000
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            elif posVelo(velol, velor) == "false":
                print "Max Velocity reached!"
            elif posVelo(velol, velor) == "true":
                velol = velol + 500
                velor = velor - 500
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            print "TURBOUP is being pressed"

            print "TURBORIGHT is being pressed"

        if key[pygame.K_DOWN]:
            if velol == 0 and velor == 0:
                velol = -15000
                velor = 15000
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            elif negVelo(velol, velor) == "false":
                print "Min Velocity reached!"
            elif posVelo(velol, velor) == "true" or negVelo(velol, velor) == "true":
                velol = velol - 100
                velor = velor + 100
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            print "DOWN is being pressed"

        if key[pygame.K_LSHIFT] and key[pygame.K_DOWN]:
            if velol == 0 and velor == 0:
                velol = -15000
                velor = 15000
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            elif negVelo(velol, velor) == "false":
                print "Min Velocity reached!"
            elif posVelo(velol, velor) == "true" or negVelo(velol, velor) == "true":
                velol = velol - 500
                velor = velor + 500
                dc0.set_velocity(velol)
                dc1.set_velocity(velor)
                print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            print "TURBODOWN is being pressed"

        if key[pygame.K_r]:
            if posVelo(velol, velor) == "true" and negVelo(velol, velor) == "true":
                if velol >= 12000 and velor <= -12000:
                    velol = 13000
                    velor = -13000
                    dc0.set_velocity(velol)
                    dc1.set_velocity(velor)
                    print "Set Positive Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
                elif velol <= 12000 and velor >= -12000:
                    velol = -13000
                    velor = 13000
                    dc0.set_velocity(velol)
                    dc1.set_velocity(velor)
                    print "Set Negative Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            else:
                print "Max of one DC Brick reached!"
            print "LEFT is being pressed"

        if key[pygame.K_e]:
            if dc0.is_enabled() == True or dc1.is_enabled() == True:
                dc0.disable()
                dc1.disable()
                print "DC Bricks will disabled!"
            elif dc0.is_enabled() == False or dc1.is_enabled() == False:
                # Set strong frequency to both DC Bricks range 0 - 20000 default is 15000
                dc0.set_pwm_frequency(hz)
                dc1.set_pwm_frequency(hz)
                # Set acceleration to default, set to 1600 for 10sek acceleration to 16000
                dc0.set_acceleration(acc)
                dc1.set_acceleration(acc)

                # Enable both DC Bricks
                dc0.enable()
                dc1.enable()
                print "DC Bricks will enabled!"
            else:
                print "Cannot find State of DC Bricks - Enabled?"

        if key[pygame.K_SPACE]:
            velol = 0
            velor = 0
            dc0.set_velocity(velol)
            dc1.set_velocity(velor)
            dc0.disable()
            dc1.disable()
            print "Set Velocity to: DC0: %s // DC1: %s" % ( velol, velor)
            print "DC Bricks disabled!"
            print "SPACE is being pressed"

        # Mit ESC wird PyGame beendet - hier muss die Beendung der Schleife und des Programmes folgen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
                DisplayClear()
                lcd.backlight_off()
                sleep(1)
                ipcon.destroy()

   
if __name__ == "__main__":
    
    # Initialisiere PyGame um die Steuerung zu realisieren
    pygame.init()
    # Defeniere die groesse des unnoetigen PyGame fensters, 
    # hier soll spaeter die Webcam gezeigt werden
    screen = pygame.display.set_mode((200,200))
    # Wird benoetigt um die KeyWiederholung zu realisieren
    clock = pygame.time.Clock()

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

    # Hier wird ein Initial Program gestartet um eventuelle sonderwuensche entgegenzunehmen
    velol = 0
    velor = 0
    hz = 0
    acc = 0
    getVars(velol, velor, hz, acc)
    
    #Hier wird der erste Thread gestartet, er kuemmert sich ums Display
    startStatus()

    #Hier der zweite thread der sich um die Steuerung kuemmert, er laueft deutlich schneller!
    Control(velol, velor, hz, acc)

    #Display off - hier doof weil das display staendig resetet wird und am ende gehts nicht aus
    # DisplayClear()
    #lcd.backlight_off()
    #raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()

