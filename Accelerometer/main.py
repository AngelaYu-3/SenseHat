from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

from sense_hat import SenseHat

sense = SenseHat()
blue = (0, 0, 255)

sense.show_letter('J', blue)

while True:
	#get_accelerometer_raw gives intensity of the axes in Gs while get_accelerometer gives the angle from the axes in degrees
	#get_accelerometer first calls set_imu_config to disable the magnometer and gyroscope if those are running
	#both get_acceleromter_raw and get_accelerometer are of type dictionary
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	#rounding accelerometer values to the first digits as values are given as floats
	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)

	print("x={0}, y={1}, z={2}".format(x, y, z))
	
	# Update the rotation of the display depending on which way up the Sense HAT is
	if x  == -1:
	  sense.set_rotation(180)
	elif y == 1:
	  sense.set_rotation(90)
	elif y == -1:
	  sense.set_rotation(270)
	else:
	  sense.set_rotation(0)
