from sense_hat import SenseHat, ACTION_RELEASED
from signal import pause

sense = SenseHat()
sense.clear()

#pixel starting point
x = 4
y = 4
white = (255, 255, 255)
sense.set_pixel(x, y, white)

#updates x and y values accordingly
#how do these two lines handle unique cases of reaching all four borders of the LED display?
def track(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushedUp(event):
  #global--necessary in order to update x and y values from inside the function
  #global allows user to modify variable outside of the current scope (the function)
  #global is not needed for printing or accessing from ourside of the current scope
      #ex: print(x + y) is fine but NOT 
      
           #x = x + 5 
           #print(x)
  global y
  #allows pixel to move up continuously while held
  if event.action != ACTION_RELEASED:
    y = track(y - 1)
    
def pushedDown(event):
  global y
  if event.action != ACTION_RELEASED:
    y = track(y + 1)
    
def pushedLeft(event):
  global x
  if event.action != ACTION_RELEASED:
    x = track(x - 1)
    
def pushedRight(event):
  global x
  if event.action != ACTION_RELEASED:
    x = track(x + 1)
    
def refresh():
  sense.clear()
  sense.set_pixel(x, y, white)
  
#assigning functions above to be called whenever Joystick is pushed in the appropriate direction
sense.stick.direction_up = pushedUp
sense.stick.direction_down = pushedDown
sense.stick.direction_left = pushedLeft
sense.stick.direction_right = pushedRight

#this call means that no matter what key is pressed for any direction, the display will always refresh
#thus allowing the pixel to move to its new spot each time
sense.stick.direction_any = refresh
#needs this refresh() call after to actually call the refresh method as refresh() is not event based
refresh()

#pause() ensure that the program will not get to the end and terminate
#keeps the state of the objects constantly active--waiting for events to occur
pause()
