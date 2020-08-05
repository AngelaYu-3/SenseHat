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

def draw(x, y, color):
  x *= 3
  y *= 3
  #print(x)
  #print(y)
  sense.set_pixel(x, y, color)
  sense.set_pixel(x + 1, y, color)
  sense.set_pixel(x, y + 1, color)
  sense.set_pixel(x + 1, y + 1, color)
    
def player1():
  while(True):
    p1_x = int(input('Player 1 enter your coordinate in your X coordinate: '))
    p1_y = int(input('Player 1 enter your coordinate in your Y coordinate:'))
    print("")
    if p1_x > 2 or p1_y > 2:
      pass
    else:
      draw(p1_x, p1_y, blue)
      winner("p1", p1_x, p1_y)
      break
    
def player2():
  while(True):
    p2_x = int(input('Player 2 enter your coordinate in your X coordinate: '))
    p2_y = int(input('Player 2 enter your coordinate in your Y coordinate: '))
    print("\n")
    if p2_x > 2 or p2_y > 2:
      pass
    else:
      draw(p2_x, p2_y, red)
      #winner()
      break

#stopping the game when one player gets three in a row
#using a 2d array to track where players are and to check if there's a win
#still in the process of programming
#if this is too difficult for students, can give them code with winner() already implemented
#or just not have them code winner at all as game can still be played w/o winner()
def winner(player, x, y):
  rows, cols = (3, 3) 
  global arr 
  arr = [[0 for x in range(3)] for y in range(3)] 
  #arrPrint(arr)
  arr[0][0] = 1
  #arrPrint(arr)
  #print("")
  arr[0][1] = 1
  #arrPrint(arr)
  #print("")
  arr[0][2] = 1
  #arrPrint(arr)
  
  if arr[0] == [1, 1, 1]:
    print(":)")
 
#used for debugging winner()     
def arrPrint(array):
  for i in range(3):
    for j in range(3):
      print(array[i][j])
    
#user interface      
def main():
  board()
  print("Player 1 is blue, Player 2 is red. Player 1 will start")
  while True:
    player1()
    player2()
  
main()
  


  