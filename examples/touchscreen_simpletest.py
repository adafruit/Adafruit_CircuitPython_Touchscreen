import adafruit_touchscreen
import board

# These pins are used as both analog and digital! XR and YU must be analog
# and digital capable. XL and YD just need to be digital
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(320,240))

while True:
    p = ts.touch_point
    if p:
        print(p)
