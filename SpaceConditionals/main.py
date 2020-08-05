from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

#International Space Station (ISS) conditions:
    #Temperature: 18-26 Celsius
    #Pressure: 979-1027 hPa
    #Humidity: 60% 
    
g = (0, 255, 0)
r = (255, 0, 0)
b = (0, 0, 0)
 
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

t = round(t, 0)
p = round(p, 0)
h = round(h, 0)

print(t)
print(p)
print(h)

if(((t >= 18) and (t <= 26)) and ((p >= 979) and (p <= 1027)) and (h == 60)):
  
  smile = [
    b, b, b, b, b, b, b, b, 
    b, b, b, b, b, b, b, b,
    b, b, g, b, g, b, b, b,
    b, b, g, b, g, b, b, b,
    b, g, b, b, b, g, b, b,
    b, g, b, b, b, g, b, b,
    b, b, g, g, g, b, b, b,
    b, b, b, b, b, b, b, b,
  ]
  sense.set_pixels(smile)
  print("Yay, space!")
  
else:
  sad = [
    b, b, b, b, b, b, b, b, 
    b, b, b, b, b, b, b, b,
    b, b, r, b, r, b, b, b,
    b, b, r, b, r, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, r, r, r, b, b, b,
    b, r, b, b, b, r, b, b,
    b, r, b, b, b, r, b, b,
  ] 
  sense.set_pixels(sad)
  print("conditions not met")