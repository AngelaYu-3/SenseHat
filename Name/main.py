from sense_hat import SenseHat
from time import sleep 
from random import choice
sense = SenseHat()

#color variables defined (RGB)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
purple = (186, 157, 245)

color = [red, blue, green, white, yellow, purple]

#method for letter
#picks random color from color list, shows letter, and pauses for 1 sec before next letter
def letter(input):
  randColor = choice(color)
  sense.show_letter(input, randColor)
  sleep(1)

while(True):
  letter('A')
  letter('n')
  letter('g')
  letter('e')
  letter('l')
  letter('a')


