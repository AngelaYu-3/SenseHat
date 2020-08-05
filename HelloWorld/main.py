from sense_hat import SenseHat #importing SenseHat library
sense = SenseHat() #creating SenseHat object sense

back_color = (247, 232, 215) #background color variable (RGB values)
text_color = (0,232,255) #text color variable (RGB values)

#infinite loop so message always runs
while (True):
  
  print(":)") #print :) in the terminal in each loop
  
  #first parameter: message
  #second parameter: scroll speed of message--higher the number the slower it scrolls; default is 0.1
  #third parameter: color of the message 
  #fourth parameter: background color
  sense.show_message("Hello, world!", 0.05, text_color, back_color) 
