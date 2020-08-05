from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#IMU (Inertial Measurement Unit)
    #gyroscope (orientation) , accelerometer (movement), magnetometer (magnetic fields)
    
#All objects have three axes around which they can rotate:
    #pitch, roll, and yaw
    
#can just use this line to print all three axes values 
o = sense.get_orientation()
while(True):
  pitch = o["pitch"]
  roll = o["roll"]
  yaw = o["yaw"]
  print "Pitch: {} Roll: {} Yaw: {}".format(pitch, roll, yaw)
  sleep(1)