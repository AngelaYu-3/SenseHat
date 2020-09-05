from sense_hat import SenseHat
from signal import pause
from array import *
import sys

sense = SenseHat()
sense.clear()
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
val = [2 , 5]
arr = [[0] * 3 for i in range(3)]

#implementing board
def board():
  #printing out vert lines
  for i in val:
    x = i
    for y in range(8):
      sense.set_pixel(x, y, white)
      y += 1
  
  #printing out horiz lines    
  for i  in val:
    y = i
    for x in range(8):
      sense.set_pixel(x, y, white)
      x +=1

#inputting boxes
def draw(x, y, color):
  x *= 3
  y *= 3
  #print(x)
  #print(y)
  sense.set_pixel(x, y, color)
  sense.set_pixel(x + 1, y, color)
  sense.set_pixel(x, y + 1, color)
  sense.set_pixel(x + 1, y + 1, color)

#making sure not coordinates are repeated   
def isUnique(x, y):
  if arr[x][y] == 0:
    return True
  else:
    return False

#checking for a tie    
def isTie():
  for i in range(3):
    for j in range(3):
      if arr[i][j] == 0:
        return False
        break
  return True
      

#checking for diagonal wins    
def isHwin(y_val, p):
    if (arr[0][y_val] == p) and (arr[1][y_val] == p) and (arr[2][y_val] == p):
      return True
    else:
      return False

#checking for horizontal wins      
def isXwin(p):
    if (arr[0][0] == p) and (arr[1][1] == p) and (arr[2][2] == p):
      return True
    elif (arr[0][2] == p) and (arr[1][1] == p) and (arr[2][0] == p):
      return True
    else:
      return False

#2d array to track where players are and to check if there's a win
def winner(p, x, y):
    arr[x][y] = p
    #print(arr)
    if (arr[0] == [p, p, p]) or (arr[1] == [p, p, p]) or (arr[2] == [p, p, p]):
      print("Player 1 (BLUE) wins!")
      exit()
    elif isHwin(y, p) is True:
      if p == 1:
          print("Player 1 (BLUE) wins!")
      else:
          print("Player 2 (RED) wins!")
      exit()
    elif isXwin(p) is True:
      if p == 1:
          print("Player 1 (BLUE) wins!")
      else:
          print("Player 2 (RED) wins!")
      exit()
    elif isTie() is True:
       print("Tie!")
       exit()
       
#player method, recieving input, drawing, and deciding if winner    
def player(i):
  while(True):
    p_x = int(input("Player {} enter your X coordinate (0-2): ".format(i)))
    p_y = int(input("Player {} enter your Y coordinate (0-2): ".format(i)))
    print("\n")
    if p_x > 2 or p_y > 2:
      print("Please re-enter player {}".format(i))
      pass
    elif isUnique(p_x, p_y) is False:
      print("Please re-enter player {}".format(i))
      pass
    else:
      if i == 1:
        draw(p_x, p_y, blue)
        winner(1, p_x, p_y)
        break
      else:
        draw(p_x, p_y, red)
        winner(2, p_x, p_y)
        break
    
#main method     
def main():
  board()
  print("Player 1 is BLUE, Player 2 is RED. Player 1 will start")
  while True:
    player(1)
    player(2)
  
main()