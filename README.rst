Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-touchscreen/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/touchscreen/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Touchscreen/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Touchscreen/actions/
    :alt: Build Status

CircuitPython library for 4-wire resistive touchscreens


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-touchscreen/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-touchscreen

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-touchscreen

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-touchscreen

Usage Example
=============

.. code-block:: python

	import board
	import adafruit_touchscreen

	# These pins are used as both analog and digital! 
	# XR, XL and YU must be analog and digital capable. 
	# YD just needs to be digital.
	ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
					      board.TOUCH_YD, board.TOUCH_YU)

	while True:
	    p = ts.touch_point
	    if p:
		print(p)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Touchscreen/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
