from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)
red = (255, 0, 0)
g = (0, 255, 0)
o = (255, 132, 66)
b = (0, 0, 0)

#setting corner pixels to blue and red
sense.set_pixel(0, 0, blue)
sense.set_pixel(7, 7, blue)
sense.set_pixel(7, 0, red)
sense.set_pixel(0, 7, red)

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