from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

def map_range(x, in_min, in_max, out_min, out_max):
    """
    Maps a number from one range to another.
    Note: This implementation handles values < in_min differently than arduino's map function does.
    :return: Returns value mapped to new range
    :rtype: float
    """
    mapped = (x-in_min) * (out_max - out_min) / (in_max-in_min) + out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)

class Touchscreen:

    def __init__(self, x1_pin, x2_pin, y1_pin, y2_pin, *,
                 x_resistance=None, samples=4, z_threshhold=10000,
                 calibration=None, size=None):
        """Since we use the pins as both analog and digital, they must be pins
        not DigitalInOuts!"""
        self._xm_pin = x1_pin
        self._xp_pin = x2_pin
        self._ym_pin = y1_pin
        self._yp_pin = y2_pin
        self._rx_plate = x_resistance
        self._xsamples = [0] * samples
        self._ysamples = [0] * samples
        if not calibration:
            calibration = ((0, 65535), (0, 65535))
        self._calib = calibration
        self._size = size
        self._zthresh = z_threshhold

    @property
    def touch_point(self):
        with DigitalInOut(self._yp_pin) as yp:
            with DigitalInOut(self._ym_pin) as ym:
                with AnalogIn(self._xp_pin) as xp:
                    yp.switch_to_output(True)
                    ym.switch_to_output(False)
                    for i in range(len(self._xsamples)):
                        self._xsamples[i] = xp.value
        x = sum(self._xsamples) / len(self._xsamples)
        x_size = 65535
        if self._size:
            x_size = self._size[0]
        x = int(map_range(x, self._calib[0][0], self._calib[0][1], 0, x_size))

        with DigitalInOut(self._xp_pin) as xp:
            with DigitalInOut(self._xm_pin) as xm:
                with AnalogIn(self._yp_pin) as yp:
                    xp.switch_to_output(True)
                    xm.switch_to_output(False)
                    for i in range(len(self._ysamples)):
                        self._ysamples[i] = yp.value
        y = sum(self._ysamples) / len(self._ysamples)
        y_size = 65535
        if self._size:
            y_size = self._size[1]
        y = int(map_range(y, self._calib[1][0], self._calib[1][1], 0, y_size))

        z1 = z2 = z = None
        with DigitalInOut(self._xp_pin) as xp:
            xp.switch_to_output(False)
            with DigitalInOut(self._ym_pin) as ym:
                ym.switch_to_output(True)
                with AnalogIn(self._xm_pin) as xm:
                    z1 = xm.value
                with AnalogIn(self._yp_pin) as yp:
                    z2 = yp.value
        #print(z1, z2)
        z = 65535 - (z2-z1)
        if z > self._zthresh:
            return (x, y, z)
        return None
