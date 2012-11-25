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

GetPositionCallbackThreshold = namedtuple('PositionCallbackThreshold', ['option', 'min', 'max'])
GetAnalogValueCallbackThreshold = namedtuple('AnalogValueCallbackThreshold', ['option', 'min', 'max'])

class LinearPoti(Device):
    """
    Device for sensing Linear Potentiometer input
    """

    CALLBACK_POSITION = 13
    CALLBACK_ANALOG_VALUE = 14
    CALLBACK_POSITION_REACHED = 15
    CALLBACK_ANALOG_VALUE_REACHED = 16

    FUNCTION_GET_POSITION = 1
    FUNCTION_GET_ANALOG_VALUE = 2
    FUNCTION_SET_POSITION_CALLBACK_PERIOD = 3
    FUNCTION_GET_POSITION_CALLBACK_PERIOD = 4
    FUNCTION_SET_ANALOG_VALUE_CALLBACK_PERIOD = 5
    FUNCTION_GET_ANALOG_VALUE_CALLBACK_PERIOD = 6
    FUNCTION_SET_POSITION_CALLBACK_THRESHOLD = 7
    FUNCTION_GET_POSITION_CALLBACK_THRESHOLD = 8
    FUNCTION_SET_ANALOG_VALUE_CALLBACK_THRESHOLD = 9
    FUNCTION_GET_ANALOG_VALUE_CALLBACK_THRESHOLD = 10
    FUNCTION_SET_DEBOUNCE_PERIOD = 11
    FUNCTION_GET_DEBOUNCE_PERIOD = 12

    def __init__(self, uid):
        """
        Creates an object with the unique device ID *uid*. This object can
        then be added to the IP connection.
        """
        Device.__init__(self, uid)

        self.expected_name = 'Linear Poti Bricklet'

        self.binding_version = [1, 0, 0]

        self.callback_formats[LinearPoti.CALLBACK_POSITION] = 'H'
        self.callback_formats[LinearPoti.CALLBACK_ANALOG_VALUE] = 'H'
        self.callback_formats[LinearPoti.CALLBACK_POSITION_REACHED] = 'H'
        self.callback_formats[LinearPoti.CALLBACK_ANALOG_VALUE_REACHED] = 'H'

    def get_position(self):
        """
        Returns the position of the Linear Potentiometer. The value is  
        between 0 (slider down) and 100 (slider up).
        
        If you want to get the position periodically, it is recommended to use the
        callback :func:`Position` and set the period with 
        :func:`SetPositionCallbackPeriod`.
        """
        return self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_POSITION, (), '', 'H')

    def get_analog_value(self):
        """
        Returns the value as read by a 12-bit analog-to-digital converter.
        The value is between 0 and 4095.
        
        .. note::
         The value returned by :func:`GetPosition` is averaged over several samples
         to yield less noise, while :func:`GetAnalogValue` gives back raw
         unfiltered analog values. The only reason to use :func:`GetAnalogValue` is,
         if you need the full resolution of the analog-to-digital converter.
        
        If you want the analog value periodically, it is recommended to use the 
        callback :func:`AnalogValue` and set the period with 
        :func:`SetAnalogValueCallbackPeriod`.
        """
        return self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_ANALOG_VALUE, (), '', 'H')

    def set_position_callback_period(self, period):
        """
        Sets the period in ms with which the :func:`Position` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        :func:`Position` is only triggered if the position has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, LinearPoti.FUNCTION_SET_POSITION_CALLBACK_PERIOD, (period,), 'I', '')

    def get_position_callback_period(self):
        """
        Returns the period as set by :func:`SetPositionCallbackPeriod`.
        """
        return self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_POSITION_CALLBACK_PERIOD, (), '', 'I')

    def set_analog_value_callback_period(self, period):
        """
        Sets the period in ms with which the :func:`AnalogValue` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        :func:`AnalogValue` is only triggered if the analog value has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, LinearPoti.FUNCTION_SET_ANALOG_VALUE_CALLBACK_PERIOD, (period,), 'I', '')

    def get_analog_value_callback_period(self):
        """
        Returns the period as set by :func:`SetAnalogValueCallbackPeriod`.
        """
        return self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_ANALOG_VALUE_CALLBACK_PERIOD, (), '', 'I')

    def set_position_callback_threshold(self, option, min, max):
        """
        Sets the thresholds for the :func:`PositionReached` callback. 
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the position is *outside* the min and max values"
         "'i'",    "Callback is triggered when the position is *inside* the min and max values"
         "'<'",    "Callback is triggered when the position is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the position is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, LinearPoti.FUNCTION_SET_POSITION_CALLBACK_THRESHOLD, (option, min, max), 'c h h', '')

    def get_position_callback_threshold(self):
        """
        Returns the threshold as set by :func:`SetPositionCallbackThreshold`.
        """
        return GetPositionCallbackThreshold(*self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_POSITION_CALLBACK_THRESHOLD, (), '', 'c h h'))

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
        self.ipcon.send_request(self, LinearPoti.FUNCTION_SET_ANALOG_VALUE_CALLBACK_THRESHOLD, (option, min, max), 'c H H', '')

    def get_analog_value_callback_threshold(self):
        """
        Returns the threshold as set by :func:`SetAnalogValueCallbackThreshold`.
        """
        return GetAnalogValueCallbackThreshold(*self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_ANALOG_VALUE_CALLBACK_THRESHOLD, (), '', 'c H H'))

    def set_debounce_period(self, debounce):
        """
        Sets the period in ms with which the threshold callbacks
        
         :func:`PositionReached`, :func:`AnalogValueReached`
        
        are triggered, if the thresholds
        
         :func:`SetPositionCallbackThreshold`, :func:`SetAnalogValueCallbackThreshold`
        
        keep being reached.
        
        The default value is 100.
        """
        self.ipcon.send_request(self, LinearPoti.FUNCTION_SET_DEBOUNCE_PERIOD, (debounce,), 'I', '')

    def get_debounce_period(self):
        """
        Returns the debounce period as set by :func:`SetDebouncePeriod`.
        """
        return self.ipcon.send_request(self, LinearPoti.FUNCTION_GET_DEBOUNCE_PERIOD, (), '', 'I')

    def register_callback(self, id, callback):
        """
        Registers a callback with ID id to the function callback.
        """
        self.registered_callbacks[id] = callback
