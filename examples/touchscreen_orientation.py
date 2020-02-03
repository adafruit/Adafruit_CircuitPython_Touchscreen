import board
import adafruit_touchscreen

# Allign the touchscreen so that the top left corner reads as x=0, y=0
# Uncoment the display setup code for the opropriate touchscreen orientation.

'''
# -------Rotate 0:
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(320, 240))
'''

'''
# -------Rotate 90:
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_YU, board.TOUCH_YD,
                                      board.TOUCH_XL, board.TOUCH_XR,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(240, 320))
'''

'''
# ------Rotate 180:
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XR, board.TOUCH_XL,
                                      board.TOUCH_YU, board.TOUCH_YD,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(320, 240))
'''

# ------Rotate 270:
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_YD, board.TOUCH_YU,
                                      board.TOUCH_XR, board.TOUCH_XL,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(240, 320))

while True:
    p = ts.touch_point
    if p:
        print(p)