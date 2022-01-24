
import pygame
import itertools

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
chess_val = {"p":1,"r":5,"n":3,"b":3,"q":9,"k":10000,"P":1,"R":5,"N":3,"B":3,"Q":9,"K":10000}
print(chess_val["p"])
# position valuation method: White's pieces point - black = value of the position
# read through fen string and add up the point

count = 0 # odd number white's turn, even number balck's turn
# apply 50-moves draw rule
if count == 50:
  print("draw") # exit the program


white_pos_val, black_pos_val = (0,0)

def calculatepos(fen,chess_val):
  global white_pos_val,black_pos_val
  for i in fen:
    if i.isupper() == True and i != "8" and i != "/":
      white_pos_val = white_pos_val + chess_val[i]
    if i.isupper() == False and i != "8" and i != "/":
      black_pos_val = black_pos_val + chess_val[i]
      
  total_val = white_pos_val - black_pos_val
  print(total_val,white_pos_val,black_pos_val)


# black is the minimizer and white is the maximizer
print("hello world")
#from Chess import engine
Images = {}
running = True
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
# starting window
#background_colour = (255, 0, 0) # background color white
def main():
  
  global screen
  pygame.display.set_caption('Chess Game')
  #gs = engine.Gamestate()
  # screen.fill((0,0,0))

  
def loadimages():
  pieces = ["p","r","n","b","k","q","P2","R2","N2","B2","K2","Q2"]
  for names in pieces:
    Images[names] = pygame.image.load("Chess_"+pieces+".png")

  return(Images)

def drawsquare(screen):
  color = (255,0,0)
  for x in range(8):
    if x%2 == 0:
      pass
      # next time
      # figure out efficent method to represent the board for user
# drawing 8 by 8 grid


# placing pieces using fen representation
# upper case white pieces
# lower case black pieces
# / next row start from 8th row

while running:
  main()
  drawsquare(screen)
  #loadimages()
  #calculatepos(fen,chess_val)

 
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
pygame.display.update()