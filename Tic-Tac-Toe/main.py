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
def isHwin(y_val, t):
    if (arr[0][y_val] == t) and (arr[1][y_val] == t) and (arr[2][y_val] == t):
      return True
    else:
      return False

#checking for horizontal wins      
def isXwin(t):
    if (arr[0][0] == t) and (arr[1][1] == t) and (arr[2][2] == t):
      return True
    elif (arr[0][2] == t) and (arr[1][1] == t) and (arr[2][0] == t):
      return True
    else:
      return False

#2d array to track where players are and to check if there's a win
def winner(player, x, y):
  if player is "p1":
    arr[x][y] = 1
    #print(arr)
    if (arr[0] == [1, 1, 1]) or (arr[1] == [1, 1, 1]) or (arr[2] == [1, 1, 1]):
      print("Player 1 (BLUE) wins!")
      exit()
    elif isHwin(y, 1) is True:
      print("Player 1 (BLUE) wins!")
      exit()
    elif isXwin(1) is True:
       print("Player 1 (BLUE) wins!")
       exit()
    elif isTie() is True:
      print("Tie!")
      exit()
      
  else:
    arr[x][y] = 2
    #print(arr)
    if (arr[0] == [2, 2, 2]) or (arr[1] == [2, 2, 2]) or (arr[2] == [2, 2, 2]):
      print("Player 2 (RED) wins!")
      exit()
    elif isHwin(y, 2) is True:
      print("Player 2 (RED) wins!")
      exit()
    elif isXwin(2) is True:
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
      pass
    elif isUnique(p_x, p_y) is False:
      pass
    else:
      if i == 1:
        draw(p_x, p_y, blue)
        winner("p1", p_x, p_y)
        break
      else:
        draw(p_x, p_y, red)
        winner("p2", p_x, p_y)
        break
    
#main method     
def main():
  board()
  print("Player 1 is BLUE, Player 2 is RED. Player 1 will start")
  while True:
    player(1)
    player(2)
  
main()