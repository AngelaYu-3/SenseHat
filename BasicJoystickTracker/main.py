from sense_hat import SenseHat
sense = SenseHat()

while True:
  #event loop--runs only when a certain event is completed
  #for joystick, get_events() outputs a tuple
  #tuple--data structure whose elements are unchangeable thus using less memory than a list or array
  for event in sense.stick.get_events():
    print(event.timestamp, event.direction, event.action)