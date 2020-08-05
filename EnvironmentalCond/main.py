from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

#printing pressure (hecto Pascals) 
#sea level: 1013 hPa
pressure = sense.get_pressure()
print "Pressure: {} hPa\n".format(pressure)

#printing temperature
temp = sense.get_temperature()
print "Temperature: {} degrees Celsius\n".format(temp)

#printing humidity
#capacity of air to hold water relative to maximum humidity at same temp
humidity = sense.get_humidity()
print "Humidity: {}%".format(humidity)

#try changing the pressure, temperature, and humidity values!

