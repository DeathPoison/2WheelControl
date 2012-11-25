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

GetAcceleration = namedtuple('Acceleration', ['x', 'y', 'z'])
GetMagneticField = namedtuple('MagneticField', ['x', 'y', 'z'])
GetAngularVelocity = namedtuple('AngularVelocity', ['x', 'y', 'z'])
GetAllData = namedtuple('AllData', ['acc_x', 'acc_y', 'acc_z', 'mag_x', 'mag_y', 'mag_z', 'ang_x', 'ang_y', 'ang_z', 'temperature'])
GetOrientation = namedtuple('Orientation', ['roll', 'pitch', 'yaw'])
GetQuaternion = namedtuple('Quaternion', ['x', 'y', 'z', 'w'])

class IMU(Device):
    """
    Device for sensing acceleration, magnetic field and angular velocity
    """

    CALLBACK_ACCELERATION = 31
    CALLBACK_MAGNETIC_FIELD = 32
    CALLBACK_ANGULAR_VELOCITY = 33
    CALLBACK_ALL_DATA = 34
    CALLBACK_ORIENTATION = 35
    CALLBACK_QUATERNION = 36

    FUNCTION_GET_ACCELERATION = 1
    FUNCTION_GET_MAGNETIC_FIELD = 2
    FUNCTION_GET_ANGULAR_VELOCITY = 3
    FUNCTION_GET_ALL_DATA = 4
    FUNCTION_GET_ORIENTATION = 5
    FUNCTION_GET_QUATERNION = 6
    FUNCTION_GET_IMU_TEMPERATURE = 7
    FUNCTION_LEDS_ON = 8
    FUNCTION_LEDS_OFF = 9
    FUNCTION_ARE_LEDS_ON = 10
    FUNCTION_SET_ACCELERATION_RANGE = 11
    FUNCTION_GET_ACCELERATION_RANGE = 12
    FUNCTION_SET_MAGNETOMETER_RANGE = 13
    FUNCTION_GET_MAGNETOMETER_RANGE = 14
    FUNCTION_SET_CONVERGENCE_SPEED = 15
    FUNCTION_GET_CONVERGENCE_SPEED = 16
    FUNCTION_SET_CALIBRATION = 17
    FUNCTION_GET_CALIBRATION = 18
    FUNCTION_SET_ACCELERATION_PERIOD = 19
    FUNCTION_GET_ACCELERATION_PERIOD = 20
    FUNCTION_SET_MAGNETIC_FIELD_PERIOD = 21
    FUNCTION_GET_MAGNETIC_FIELD_PERIOD = 22
    FUNCTION_SET_ANGULAR_VELOCITY_PERIOD = 23
    FUNCTION_GET_ANGULAR_VELOCITY_PERIOD = 24
    FUNCTION_SET_ALL_DATA_PERIOD = 25
    FUNCTION_GET_ALL_DATA_PERIOD = 26
    FUNCTION_SET_ORIENTATION_PERIOD = 27
    FUNCTION_GET_ORIENTATION_PERIOD = 28
    FUNCTION_SET_QUATERNION_PERIOD = 29
    FUNCTION_GET_QUATERNION_PERIOD = 30
    FUNCTION_RESET = 243
    FUNCTION_GET_CHIP_TEMPERATURE = 242

    def __init__(self, uid):
        """
        Creates an object with the unique device ID *uid*. This object can
        then be added to the IP connection.
        """
        Device.__init__(self, uid)

        self.expected_name = 'IMU Brick'

        self.binding_version = [1, 0, 1]

        self.callback_formats[IMU.CALLBACK_ACCELERATION] = 'h h h'
        self.callback_formats[IMU.CALLBACK_MAGNETIC_FIELD] = 'h h h'
        self.callback_formats[IMU.CALLBACK_ANGULAR_VELOCITY] = 'h h h'
        self.callback_formats[IMU.CALLBACK_ALL_DATA] = 'h h h h h h h h h h'
        self.callback_formats[IMU.CALLBACK_ORIENTATION] = 'h h h'
        self.callback_formats[IMU.CALLBACK_QUATERNION] = 'f f f f'

    def get_acceleration(self):
        """
        Returns the calibrated acceleration from the accelerometer for the 
        x, y and z axis in mG (G/1000, 1G = 9.80605m/s²).
        
        If you want to get the acceleration periodically, it is recommended 
        to use the callback :func:`Acceleration` and set the period with 
        :func:`SetAccelerationPeriod`.
        """
        return GetAcceleration(*self.ipcon.send_request(self, IMU.FUNCTION_GET_ACCELERATION, (), '', 'h h h'))

    def get_magnetic_field(self):
        """
        Returns the calibrated magnetic field from the magnetometer for the 
        x, y and z axis in mG (Milligauss or Nanotesla).
        
        If you want to get the magnetic field periodically, it is recommended 
        to use the callback :func:`MagneticField` and set the period with 
        :func:`SetMagneticFieldPeriod`.
        """
        return GetMagneticField(*self.ipcon.send_request(self, IMU.FUNCTION_GET_MAGNETIC_FIELD, (), '', 'h h h'))

    def get_angular_velocity(self):
        """
        Returns the calibrated angular velocity from the gyroscope for the 
        x, y and z axis in °/17.5s (you have to divide by 17.5 to
        get the value in °/s).
        
        If you want to get the angular velocity periodically, it is recommended 
        to use the callback :func:`AngularVelocity` and set the period with 
        :func:`SetAngularVelocityPeriod`.
        """
        return GetAngularVelocity(*self.ipcon.send_request(self, IMU.FUNCTION_GET_ANGULAR_VELOCITY, (), '', 'h h h'))

    def get_all_data(self):
        """
        Returns the data from :func:`GetAcceleration`, :func:`GetMagneticField` 
        and :func:`GetAngularVelocity` as well as the temperature of the IMU Brick.
        
        The temperature is given in °C/100.
        
        If you want to get the data periodically, it is recommended 
        to use the callback :func:`AllData` and set the period with 
        :func:`SetAllDataPeriod`.
        """
        return GetAllData(*self.ipcon.send_request(self, IMU.FUNCTION_GET_ALL_DATA, (), '', 'h h h h h h h h h h'))

    def get_orientation(self):
        """
        Returns the current orientation (roll, pitch, yaw) of the IMU Brick as Euler
        angles in one-hundredth degree. Note that Euler angles always experience a
        `gimbal lock <http://en.wikipedia.org/wiki/Gimbal_lock>`__.
        
        We recommend that you use quaternions instead.
        
        The order to sequence in which the orientation values should be applied is 
        roll, yaw, pitch. 
        
        If you want to get the orientation periodically, it is recommended 
        to use the callback :func:`Orientation` and set the period with 
        :func:`SetOrientationPeriod`.
        """
        return GetOrientation(*self.ipcon.send_request(self, IMU.FUNCTION_GET_ORIENTATION, (), '', 'h h h'))

    def get_quaternion(self):
        """
        Returns the current orientation (x, y, z, w) of the IMU as 
        `quaternions <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__.
        
        You can go from quaternions to Euler angles with the following formula::
        
         roll  = atan2(2*y*w - 2*x*z, 1 - 2*y*y - 2*z*z)
         pitch = atan2(2*x*w - 2*y*z, 1 - 2*x*x - 2*z*z)
         yaw   =  asin(2*x*y + 2*z*w)
        
        This process is not reversible, because of the 
        `gimbal lock <http://en.wikipedia.org/wiki/Gimbal_lock>`__.
        
        Converting the quaternions to an OpenGL transformation matrix is
        possible with the following formula::
        
         matrix = [[1 - 2*(y*y + z*z),     2*(x*y - w*z),     2*(x*z + w*y), 0],
                   [    2*(x*y + w*z), 1 - 2*(x*x + z*z),     2*(y*z - w*x), 0],
                   [    2*(x*z - w*y),     2*(y*z + w*x), 1 - 2*(x*x + y*y), 0],
                   [                0,                 0,                 0, 1]]
        
        If you want to get the quaternions periodically, it is recommended 
        to use the callback :func:`Quaternion` and set the period with 
        :func:`SetQuaternionPeriod`.
        """
        return GetQuaternion(*self.ipcon.send_request(self, IMU.FUNCTION_GET_QUATERNION, (), '', 'f f f f'))

    def get_imu_temperature(self):
        """
        Returns the temperature of the IMU Brick. The temperature is given in 
        °C/100.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_IMU_TEMPERATURE, (), '', 'h')

    def leds_on(self):
        """
        Turns the orientation and direction LEDs of the IMU Brick on.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_LEDS_ON, (), '', '')

    def leds_off(self):
        """
        Turns the orientation and direction LEDs of the IMU Brick off.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_LEDS_OFF, (), '', '')

    def are_leds_on(self):
        """
        Returns *true* if the orientation and direction LEDs of the IMU Brick
        are on, *false* otherwise.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_ARE_LEDS_ON, (), '', '?')

    def set_acceleration_range(self, range):
        """
        Not implemented yet.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_ACCELERATION_RANGE, (range,), 'B', '')

    def get_acceleration_range(self):
        """
        Not implemented yet.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_ACCELERATION_RANGE, (), '', 'B')

    def set_magnetometer_range(self, range):
        """
        Not implemented yet.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_MAGNETOMETER_RANGE, (range,), 'B', '')

    def get_magnetometer_range(self):
        """
        Not implemented yet.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_MAGNETOMETER_RANGE, (), '', 'B')

    def set_convergence_speed(self, speed):
        """
        Sets the convergence speed of the IMU Brick in °/s. The convergence speed 
        determines how the different sensor measurements are fused.
        
        If the orientation of the IMU Brick is off by 10° and the convergence speed is 
        set to 20°/s, it will take 0.5s until the orientation is corrected. However,
        if the correct orientation is reached and the convergence speed is too high,
        the orientation will fluctuate with the fluctuations of the accelerometer and
        the magnetometer.
        
        If you set the convergence speed to 0, practically only the gyroscope is used
        to calculate the orientation. This gives very smooth movements, but errors of the
        gyroscope will not be corrected. If you set the convergence speed to something
        above 500, practically only the magnetometer and the accelerometer are used to
        calculate the orientation. In this case the movements are abrupt and the values
        will fluctuate, but there won't be any errors that accumulate over time.
        
        In an application with high angular velocities, we recommend a high convergence
        speed, so the errors of the gyroscope can be corrected fast. In applications with
        only slow movements we recommend a low convergence speed. You can change the
        convergence speed on the fly. So it is possible (and recommended) to increase 
        the convergence speed before an abrupt movement and decrease it afterwards 
        again.
        
        You might want to play around with the convergence speed in the Brick Viewer to
        get a feeling for a good value for your application.
        
        The default value is 30.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_CONVERGENCE_SPEED, (speed,), 'H', '')

    def get_convergence_speed(self):
        """
        Returns the convergence speed as set by :func:`SetConvergenceSpeed`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_CONVERGENCE_SPEED, (), '', 'H')

    def set_calibration(self, typ, data):
        """
        There are several different types that can be calibrated:
        
        .. csv-table::
         :header: "Type", "Description",        "Values"
         :widths: 10, 40, 100
        
         "0",    "Accelerometer Gain", "[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]"
         "1",    "Accelerometer Bias", "[bias x, bias y, bias z, 0, 0, 0, 0, 0, 0, 0]"
         "2",    "Magnetometer Gain",  "[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]"
         "3",    "Magnetometer Bias",  "[bias x, bias y, bias z, 0, 0, 0, 0, 0, 0, 0]"
         "4",    "Gyroscope Gain",     "[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]"
         "5",    "Gyroscope Bias",     "[bias xl, bias yl, bias zl, temp l, bias xh, bias yh, bias zh, temp h, 0, 0]"
        
        The calibration via gain and bias is done with the following formula::
        
         new_value = (bias + orig_value) * gain_mul / gain_div
        
        If you really want to write your own calibration software, please keep
        in mind that you first have to undo the old calibration (set bias to 0 and
        gain to 1/1) and that you have to average over several thousand values
        to obtain a usable result in the end.
        
        The gyroscope bias is highly dependent on the temperature, so you have to
        calibrate the bias two times with different temperatures. The values xl, yl, zl 
        and temp l are the bias for x, y, z and the corresponding temperature for a 
        low temperature. The values xh, yh, zh and temp h are the same for a high 
        temperatures. The temperature difference should be at least 5°C. If you have 
        a temperature where the IMU Brick is mostly used, you should use this 
        temperature for one of the sampling points.
        
        .. note::
         We highly recommend that you use the Brick Viewer to calibrate your
         IMU Brick.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_CALIBRATION, (typ, data), 'B 10h', '')

    def get_calibration(self, typ):
        """
        Returns the calibration for a given type as set by :func:`SetCalibration`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_CALIBRATION, (typ,), 'B', '10h')

    def set_acceleration_period(self, period):
        """
        Sets the period in ms with which the :func:`Acceleration` callback is triggered
        periodically. A value of 0 turns the callback off.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_ACCELERATION_PERIOD, (period,), 'I', '')

    def get_acceleration_period(self):
        """
        Returns the period as set by :func:`SetAccelerationPeriod`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_ACCELERATION_PERIOD, (), '', 'I')

    def set_magnetic_field_period(self, period):
        """
        Sets the period in ms with which the :func:`MagneticField` callback is triggered
        periodically. A value of 0 turns the callback off.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_MAGNETIC_FIELD_PERIOD, (period,), 'I', '')

    def get_magnetic_field_period(self):
        """
        Returns the period as set by :func:`SetMagneticFieldPeriod`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_MAGNETIC_FIELD_PERIOD, (), '', 'I')

    def set_angular_velocity_period(self, period):
        """
        Sets the period in ms with which the :func:`AngularVelocity` callback is triggered
        periodically. A value of 0 turns the callback off.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_ANGULAR_VELOCITY_PERIOD, (period,), 'I', '')

    def get_angular_velocity_period(self):
        """
        Returns the period as set by :func:`SetAngularVelocityPeriod`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_ANGULAR_VELOCITY_PERIOD, (), '', 'I')

    def set_all_data_period(self, period):
        """
        Sets the period in ms with which the :func:`AllData` callback is triggered
        periodically. A value of 0 turns the callback off.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_ALL_DATA_PERIOD, (period,), 'I', '')

    def get_all_data_period(self):
        """
        Returns the period as set by :func:`SetAllDataPeriod`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_ALL_DATA_PERIOD, (), '', 'I')

    def set_orientation_period(self, period):
        """
        Sets the period in ms with which the :func:`Orientation` callback is triggered
        periodically. A value of 0 turns the callback off.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_ORIENTATION_PERIOD, (period,), 'I', '')

    def get_orientation_period(self):
        """
        Returns the period as set by :func:`SetOrientationPeriod`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_ORIENTATION_PERIOD, (), '', 'I')

    def set_quaternion_period(self, period):
        """
        Sets the period in ms with which the :func:`Quaternion` callback is triggered
        periodically. A value of 0 turns the callback off.
        """
        self.ipcon.send_request(self, IMU.FUNCTION_SET_QUATERNION_PERIOD, (period,), 'I', '')

    def get_quaternion_period(self):
        """
        Returns the period as set by :func:`SetQuaternionPeriod`.
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_QUATERNION_PERIOD, (), '', 'I')

    def reset(self):
        """
        Calling this function will reset the Brick. Calling this function
        on a Brick inside of a stack will reset the whole stack.
        
        After a reset you have to create new device objects,
        calling functions on the existing ones will result in
        undefined behavior!
        
        .. versionadded:: 1.0.7~(Firmware)
        """
        self.ipcon.send_request(self, IMU.FUNCTION_RESET, (), '', '')

    def get_chip_temperature(self):
        """
        Returns the temperature in °C/10 as measured inside the microcontroller. The
        value returned is not the ambient temperature!
        
        The temperature is only proportional to the real temperature and it has an
        accuracy of +-15%. Practically it is only useful as an indicator for
        temperature changes.
        
        .. versionadded:: 1.0.7~(Firmware)
        """
        return self.ipcon.send_request(self, IMU.FUNCTION_GET_CHIP_TEMPERATURE, (), '', 'h')

    def register_callback(self, id, callback):
        """
        Registers a callback with ID id to the function callback.
        """
        self.registered_callbacks[id] = callback
