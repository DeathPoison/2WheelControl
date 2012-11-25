# -*- coding: utf-8 -*-
#############################################################
# This file was automatically generated on 2012-10-12.      #
#                                                           #
# If you have a bugfix for this file and want to commit it, #
# please fix the bug in the generator. You can find a link  #
# to the generator git on tinkerforge.com                   #
#############################################################

try:
    from collections import namedtuple
except ImportError:
    from .ip_connection import namedtuple
from .ip_connection import Device, IPConnection, Error

GetAirPressureCallbackThreshold = namedtuple('AirPressureCallbackThreshold', ['option', 'min', 'max'])
GetAltitudeCallbackThreshold = namedtuple('AltitudeCallbackThreshold', ['option', 'min', 'max'])

class Barometer(Device):
    """
    Device for sensing air pressure and altitude changes
    """

    CALLBACK_AIR_PRESSURE = 15
    CALLBACK_ALTITUDE = 16
    CALLBACK_AIR_PRESSURE_REACHED = 17
    CALLBACK_ALTITUDE_REACHED = 18

    FUNCTION_GET_AIR_PRESSURE = 1
    FUNCTION_GET_ALTITUDE = 2
    FUNCTION_SET_AIR_PRESSURE_CALLBACK_PERIOD = 3
    FUNCTION_GET_AIR_PRESSURE_CALLBACK_PERIOD = 4
    FUNCTION_SET_ALTITUDE_CALLBACK_PERIOD = 5
    FUNCTION_GET_ALTITUDE_CALLBACK_PERIOD = 6
    FUNCTION_SET_AIR_PRESSURE_CALLBACK_THRESHOLD = 7
    FUNCTION_GET_AIR_PRESSURE_CALLBACK_THRESHOLD = 8
    FUNCTION_SET_ALTITUDE_CALLBACK_THRESHOLD = 9
    FUNCTION_GET_ALTITUDE_CALLBACK_THRESHOLD = 10
    FUNCTION_SET_DEBOUNCE_PERIOD = 11
    FUNCTION_GET_DEBOUNCE_PERIOD = 12
    FUNCTION_SET_REFERENCE_AIR_PRESSURE = 13
    FUNCTION_GET_CHIP_TEMPERATURE = 14
    FUNCTION_GET_REFERENCE_AIR_PRESSURE = 19

    def __init__(self, uid):
        """
        Creates an object with the unique device ID *uid*. This object can
        then be added to the IP connection.
        """
        Device.__init__(self, uid)

        self.expected_name = 'Barometer Bricklet'

        self.binding_version = [1, 1, 0]

        self.callback_formats[Barometer.CALLBACK_AIR_PRESSURE] = 'i'
        self.callback_formats[Barometer.CALLBACK_ALTITUDE] = 'i'
        self.callback_formats[Barometer.CALLBACK_AIR_PRESSURE_REACHED] = 'i'
        self.callback_formats[Barometer.CALLBACK_ALTITUDE_REACHED] = 'i'

    def get_air_pressure(self):
        """
        Returns the air pressure of the air pressure sensor. The value
        has a range of 10000 to 1200000 and is given in mbar/1000, i.e. a value
        of 1001092 means that an air pressure of 1001.092 mbar is measured.
        
        If you want to get the air pressure periodically, it is recommended to use the
        callback :func:`AirPressure` and set the period with
        :func:`SetAirPressureCallbackPeriod`.
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_AIR_PRESSURE, (), '', 'i')

    def get_altitude(self):
        """
        Returns the relative altitude of the air pressure sensor. The value is given in
        cm and is caluclated based on the difference between the current air pressure
        and the reference air pressure that can be set with :func:`SetReferenceAirPressure`.
        
        If you want to get the altitude periodically, it is recommended to use the
        callback :func:`Altitude` and set the period with
        :func:`SetAltitudeCallbackPeriod`.
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_ALTITUDE, (), '', 'i')

    def set_air_pressure_callback_period(self, period):
        """
        Sets the period in ms with which the :func:`AirPressure` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        :func:`AirPressure` is only triggered if the air pressure has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, Barometer.FUNCTION_SET_AIR_PRESSURE_CALLBACK_PERIOD, (period,), 'I', '')

    def get_air_pressure_callback_period(self):
        """
        Returns the period as set by :func:`SetAirPressureCallbackPeriod`.
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_AIR_PRESSURE_CALLBACK_PERIOD, (), '', 'I')

    def set_altitude_callback_period(self, period):
        """
        Sets the period in ms with which the :func:`Altitude` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        :func:`Altitude` is only triggered if the altitude has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, Barometer.FUNCTION_SET_ALTITUDE_CALLBACK_PERIOD, (period,), 'I', '')

    def get_altitude_callback_period(self):
        """
        Returns the period as set by :func:`SetAltitudeCallbackPeriod`.
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_ALTITUDE_CALLBACK_PERIOD, (), '', 'I')

    def set_air_pressure_callback_threshold(self, option, min, max):
        """
        Sets the thresholds for the :func:`AirPressureReached` callback.
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the air pressure is *outside* the min and max values"
         "'i'",    "Callback is triggered when the air pressure is *inside* the min and max values"
         "'<'",    "Callback is triggered when the air pressure is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the air pressure is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, Barometer.FUNCTION_SET_AIR_PRESSURE_CALLBACK_THRESHOLD, (option, min, max), 'c i i', '')

    def get_air_pressure_callback_threshold(self):
        """
        Returns the threshold as set by :func:`SetAirPressureCallbackThreshold`.
        """
        return GetAirPressureCallbackThreshold(*self.ipcon.send_request(self, Barometer.FUNCTION_GET_AIR_PRESSURE_CALLBACK_THRESHOLD, (), '', 'c i i'))

    def set_altitude_callback_threshold(self, option, min, max):
        """
        Sets the thresholds for the :func:`AltitudeReached` callback.
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the altitude is *outside* the min and max values"
         "'i'",    "Callback is triggered when the altitude is *inside* the min and max values"
         "'<'",    "Callback is triggered when the altitude is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the altitude is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, Barometer.FUNCTION_SET_ALTITUDE_CALLBACK_THRESHOLD, (option, min, max), 'c i i', '')

    def get_altitude_callback_threshold(self):
        """
        Returns the threshold as set by :func:`SetAltitudeCallbackThreshold`.
        """
        return GetAltitudeCallbackThreshold(*self.ipcon.send_request(self, Barometer.FUNCTION_GET_ALTITUDE_CALLBACK_THRESHOLD, (), '', 'c i i'))

    def set_debounce_period(self, debounce):
        """
        Sets the period in ms with which the threshold callbacks
        
         :func:`AirPressureReached`, :func:`AltitudeReached`
        
        are triggered, if the thresholds
        
         :func:`SetAirPressureCallbackThreshold`, :func:`SetAltitudeCallbackThreshold`
        
        keep being reached.
        
        The default value is 100.
        """
        self.ipcon.send_request(self, Barometer.FUNCTION_SET_DEBOUNCE_PERIOD, (debounce,), 'I', '')

    def get_debounce_period(self):
        """
        Returns the debounce period as set by :func:`SetDebouncePeriod`.
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_DEBOUNCE_PERIOD, (), '', 'I')

    def set_reference_air_pressure(self, air_pressure):
        """
        Sets the reference air pressure in mbar/1000 for the altitude calculation.
        Setting the reference to the current air pressure results in a calculated
        altitude of 0cm. Passing 0 is a shortcut for passing the current air pressure as
        reference.
        
        Well known reference values are the Q codes
        `QNH <http://en.wikipedia.org/wiki/QNH>`__ and
        `QFE <http://en.wikipedia.org/wiki/Mean_sea_level_pressure#Mean_sea_level_pressure>`__
        used in aviation.
        
        The default value is 1013.25mbar.
        
        .. versionadded:: 1.1.0~(Plugin)
        """
        self.ipcon.send_request(self, Barometer.FUNCTION_SET_REFERENCE_AIR_PRESSURE, (air_pressure,), 'i', '')

    def get_chip_temperature(self):
        """
        Returns the temperature of the air pressure sensor. The value
        has a range of -4000 to 8500 and is given in °C/100, i.e. a value
        of 2007 means that a temperature of 20.07 °C is measured.
        
        This temperature is used internally for temperature compensation of the air
        pressure measurement. It is not as accurate as the temperature measured by the
        :ref:`temperature_bricklet` or the :ref:`temperature_ir_bricklet`.
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_CHIP_TEMPERATURE, (), '', 'h')

    def get_reference_air_pressure(self):
        """
        Returns the reference air pressure as set by :func:`SetReferenceAirPressure`.
        
        .. versionadded:: 1.1.0~(Plugin)
        """
        return self.ipcon.send_request(self, Barometer.FUNCTION_GET_REFERENCE_AIR_PRESSURE, (), '', 'i')

    def register_callback(self, id, callback):
        """
        Registers a callback with ID id to the function callback.
        """
        self.registered_callbacks[id] = callback
