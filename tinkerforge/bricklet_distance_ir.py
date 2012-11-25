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

GetDistanceCallbackThreshold = namedtuple('DistanceCallbackThreshold', ['option', 'min', 'max'])
GetAnalogValueCallbackThreshold = namedtuple('AnalogValueCallbackThreshold', ['option', 'min', 'max'])

class DistanceIR(Device):
    """
    Device for sensing distance via infrared
    """

    CALLBACK_DISTANCE = 15
    CALLBACK_ANALOG_VALUE = 16
    CALLBACK_DISTANCE_REACHED = 17
    CALLBACK_ANALOG_VALUE_REACHED = 18

    FUNCTION_GET_DISTANCE = 1
    FUNCTION_GET_ANALOG_VALUE = 2
    FUNCTION_SET_SAMPLING_POINT = 3
    FUNCTION_GET_SAMPLING_POINT = 4
    FUNCTION_SET_DISTANCE_CALLBACK_PERIOD = 5
    FUNCTION_GET_DISTANCE_CALLBACK_PERIOD = 6
    FUNCTION_SET_ANALOG_VALUE_CALLBACK_PERIOD = 7
    FUNCTION_GET_ANALOG_VALUE_CALLBACK_PERIOD = 8
    FUNCTION_SET_DISTANCE_CALLBACK_THRESHOLD = 9
    FUNCTION_GET_DISTANCE_CALLBACK_THRESHOLD = 10
    FUNCTION_SET_ANALOG_VALUE_CALLBACK_THRESHOLD = 11
    FUNCTION_GET_ANALOG_VALUE_CALLBACK_THRESHOLD = 12
    FUNCTION_SET_DEBOUNCE_PERIOD = 13
    FUNCTION_GET_DEBOUNCE_PERIOD = 14

    def __init__(self, uid):
        """
        Creates an object with the unique device ID *uid*. This object can
        then be added to the IP connection.
        """
        Device.__init__(self, uid)

        self.expected_name = 'Distance IR Bricklet'

        self.binding_version = [1, 0, 0]

        self.callback_formats[DistanceIR.CALLBACK_DISTANCE] = 'H'
        self.callback_formats[DistanceIR.CALLBACK_ANALOG_VALUE] = 'H'
        self.callback_formats[DistanceIR.CALLBACK_DISTANCE_REACHED] = 'H'
        self.callback_formats[DistanceIR.CALLBACK_ANALOG_VALUE_REACHED] = 'H'

    def get_distance(self):
        """
        Returns the distance measured by the sensor. The value is in mm and possible
        distance ranges are 40 to 300, 100 to 800 and 200 to 1500, depending on the
        selected IR sensor.
        
        If you want to get the distance periodically, it is recommended to use the
        callback :func:`Distance` and set the period with 
        :func:`SetDistanceCallbackPeriod`.
        """
        return self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_DISTANCE, (), '', 'H')

    def get_analog_value(self):
        """
        Returns the value as read by a 12-bit analog-to-digital converter.
        The value is between 0 and 4095.
        
        .. note::
         The value returned by :func:`GetDistance` is averaged over several samples
         to yield less noise, while :func:`GetAnalogValue` gives back raw
         unfiltered analog values. The only reason to use :func:`GetAnalogValue` is,
         if you need the full resolution of the analog-to-digital converter.
        
        If you want the analog value periodically, it is recommended to use the 
        callback :func:`AnalogValue` and set the period with 
        :func:`SetAnalogValueCallbackPeriod`.
        """
        return self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_ANALOG_VALUE, (), '', 'H')

    def set_sampling_point(self, position, distance):
        """
        Sets a sampling point value to a specific position of the lookup table.
        The lookup table comprises 128 equidistant analog values with
        corresponding distances.
        
        If you measure a distance of 50cm at the analog value 2048, you
        should call this function with (64, 5000). The utilized analog-to-digital
        converter has a resolution of 12 bit. With 128 sampling points on the
        whole range, this means that every sampling point has a size of 32
        analog values. Thus the analog value 2048 has the corresponding sampling
        point 64 = 2048/32.
        
        Sampling points are saved on the EEPROM of the Distance IR Bricklet and
        loaded again on startup.
        
        .. note::
         An easy way to calibrate the sampling points of the Distance IR Bricklet is
         implemented in the Brick Viewer. If you want to calibrate your Bricklet it is
         highly recommended to use this implementation.
        """
        self.ipcon.send_request(self, DistanceIR.FUNCTION_SET_SAMPLING_POINT, (position, distance), 'B H', '')

    def get_sampling_point(self, position):
        """
        Returns the distance to a sampling point position as set by
        :func:`SetSamplingPoint`.
        """
        return self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_SAMPLING_POINT, (position,), 'B', 'H')

    def set_distance_callback_period(self, period):
        """
        Sets the period in ms with which the :func:`Distance` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        :func:`Distance` is only triggered if the distance has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, DistanceIR.FUNCTION_SET_DISTANCE_CALLBACK_PERIOD, (period,), 'I', '')

    def get_distance_callback_period(self):
        """
        Returns the period as set by :func:`SetDistanceCallbackPeriod`.
        """
        return self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_DISTANCE_CALLBACK_PERIOD, (), '', 'I')

    def set_analog_value_callback_period(self, period):
        """
        Sets the period in ms with which the :func:`AnalogValue` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        :func:`AnalogValue` is only triggered if the analog value has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, DistanceIR.FUNCTION_SET_ANALOG_VALUE_CALLBACK_PERIOD, (period,), 'I', '')

    def get_analog_value_callback_period(self):
        """
        Returns the period as set by :func:`SetAnalogValueCallbackPeriod`.
        """
        return self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_ANALOG_VALUE_CALLBACK_PERIOD, (), '', 'I')

    def set_distance_callback_threshold(self, option, min, max):
        """
        Sets the thresholds for the :func:`DistanceReached` callback. 
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the distance is *outside* the min and max values"
         "'i'",    "Callback is triggered when the distance is *inside* the min and max values"
         "'<'",    "Callback is triggered when the distance is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the distance is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, DistanceIR.FUNCTION_SET_DISTANCE_CALLBACK_THRESHOLD, (option, min, max), 'c h h', '')

    def get_distance_callback_threshold(self):
        """
        Returns the threshold as set by :func:`SetDistanceCallbackThreshold`.
        """
        return GetDistanceCallbackThreshold(*self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_DISTANCE_CALLBACK_THRESHOLD, (), '', 'c h h'))

    def set_analog_value_callback_threshold(self, option, min, max):
        """
        Sets the thresholds for the :func:`AnalogValueReached` callback. 
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the analog value is *outside* the min and max values"
         "'i'",    "Callback is triggered when the analog value is *inside* the min and max values"
         "'<'",    "Callback is triggered when the analog value is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the analog value is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, DistanceIR.FUNCTION_SET_ANALOG_VALUE_CALLBACK_THRESHOLD, (option, min, max), 'c H H', '')

    def get_analog_value_callback_threshold(self):
        """
        Returns the threshold as set by :func:`SetAnalogValueCallbackThreshold`.
        """
        return GetAnalogValueCallbackThreshold(*self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_ANALOG_VALUE_CALLBACK_THRESHOLD, (), '', 'c H H'))

    def set_debounce_period(self, debounce):
        """
        Sets the period in ms with which the threshold callbacks
        
         :func:`DistanceReached`, :func:`AnalogValueReached`
        
        are triggered, if the thresholds
        
         :func:`SetDistanceCallbackThreshold`, :func:`SetAnalogValueCallbackThreshold`
        
        keep being reached.
        
        The default value is 100.
        """
        self.ipcon.send_request(self, DistanceIR.FUNCTION_SET_DEBOUNCE_PERIOD, (debounce,), 'I', '')

    def get_debounce_period(self):
        """
        Returns the debounce period as set by :func:`SetDebouncePeriod`.
        """
        return self.ipcon.send_request(self, DistanceIR.FUNCTION_GET_DEBOUNCE_PERIOD, (), '', 'I')

    def register_callback(self, id, callback):
        """
        Registers a callback with ID id to the function callback.
        """
        self.registered_callbacks[id] = callback
