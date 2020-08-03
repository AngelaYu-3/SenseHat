from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

g = (0, 255, 0)
o = (255, 132, 66)
b = (0, 0, 0)


#set up where the color will display pixels 
pumpkin_pixels = [
    b, b, b, b, g, g, b, b, 
    b, b, b, g, g, b, b, b,
    b, o, o, o, o, o, o, b,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    b, o, o, o, o, o, o, b,
  ]

#display colors on LED matrix  
sense.set_pixels(pumpkin_pixels)

while(True):
  choice = randint(0,4)
  if choice == 0:
    sense.set_rotation(0) #set_rotation() only takes 0, 90, 180, or 270 degrees
    choice = randint(0,4)
    sleep(0.5)
  elif choice == 1:
    sense.set_rotation(90)
    choice = randint(0,4)
    sleep(0.5)
  elif choice == 2:
    sense.set_rotation(270)
    choice = randint(0,4)
    sleep(0.5)
  elif choice == 3:
    sense.flip_v()
    choice = randint(0,4)
    sleep(0.5)
  else:
    sense.flip_h()
    choice = randint(0,4)
    sleep(0.5)

 
  
