
import pygame
import itertools



class Gamestate():
    def __init__(self,startsquarex, startsquarey, endsquarex,endsquarey):
      self.startsquarex = startsquarex
      self.startsquarey = startsquarey
      self.endsquarex = endsquarex
      self.endsquarey = endsquarey
      
      self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["/","/","/","/","/","/","/","/"],
            ["/","/","/","/","/","/","/","/"],
            ["/","/","/","/","/","/","/","/"],
            ["/","/","/","/","/","/","/","/"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],

        ]
    def inboard(self,):
      for x in range(8):
        for y in range(8):
          return self.board[self.startsquarex][self.startsquarey]

a = Gamestate(3,4,4,3)
print(a)






fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
chess_val = {"p":1,"r":5,"n":3,"b":3,"q":9,"k":10000,"P":1,"R":5,"N":3,"B":3,"Q":9,"K":10000}
print(chess_val["p"])
# position valuation method: White's pieces point - black = value of the position
# read through fen string and add up the point

count = 0 # odd number white's turn, even number balck's turn
# apply 50-moves draw rule
if count == 50:
  print("draw") # exit the program

def movepieces(running):
  x,y = (0,0)
  blackturn = False
  whiteturn = False
  ev = pygame.event.get()
  for event in ev:
    if event.type == pygame.MOUSEBUTTONUP:
      x,y = pygame.mouse.get_pos()
      print(x,y)

white_pos_val, black_pos_val = (0,0)

def calculatepos(fen,chess_val):
  global white_pos_val,black_pos_val
  for i in range(len(fen)):
    if fen[i] in chess_val and fen[i].isupper() == True:
      white_pos_val = white_pos_val + chess_val[fen[i]]
    elif fen[i] in chess_val and fen[i].isupper() == False:
      black_pos_val = black_pos_val + chess_val[fen[i]]
    else:
      pass
      
  total_val = white_pos_val - black_pos_val
  print(total_val,white_pos_val,black_pos_val)

  

# black is the minimizer and white is the maximizer
#print("hello world")
#from Chess import engine
Images = {}
running = True
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
squaresize = height // 8

# starting window
#background_colour = (255, 0, 0) # background color white
def main():
  global running
  global screen
  pygame.display.set_caption('Chess Game')
  squareselect = ()
  playerclick = []

  while running:
    
    drawsquare(screen)
    loadimages()
    movepieces(running)
    #calculatepos(fen,chess_val)
    pygame.display.update()

  
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        location = pygame.mouse.get_pos()
        col = location[0]//squaresize
        row = location[1]//squaresize
        if(squareselect == (row,col)):
          squareselect = ()
        else:
          squareselect = (row,col)
          playerclick.append(squareselect)

        if len(playerclick) == 2:
          pass
        #make a move
  pygame.quit()
  
def loadimages():
  chessboard = [
            ["r","n","b","k","q","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            ["/","/","/","/","/","/","/","/"],
            ["/","/","/","/","/","/","/","/"],
            ["/","/","/","/","/","/","/","/"],
            ["/","/","/","/","/","/","/","/"],
            ["P2","P2","P2","P2","P2","P2","P2","P2"],
            ["R2","N2","B2","K2","Q2","B2","N2","R2"],
        ]
  for x in range(8):
    #print("y",x)
    for y in range(8):
      #print("y",y)
      if(chessboard[x][y] != "/"):
        image = pygame.image.load('Chess_'+ chessboard[x][y] +'.png')
        screen.blit(image, pygame.Rect(y * squaresize - 5, squaresize * x - 5, squaresize,squaresize))


  
                                                            
  
  #for x in range(0,len(pieces_white)):
    #image = pygame.image.load('Chess_'+pieces_white[x]+'.png')
    #print(x,'Chess_'+pieces_white[x]+'.png')
    #screen.blit(image, (x * squaresize, positiony))
    #if x>7:
      #screen.blit(image, (200, positiony * squaresize))
    
  
      
      
        

  
  #for names in pieces:
    #Images[names] = pygame.image.load("Chess_"+pieces+".png")

  #return(Images)


white = (255,255,255)
forest_green = (34,139,34) # forest_green
rows = col = 8
def drawsquare(screen):
    screen.fill(white)
    for row in range(rows):
        for col in range(row % 2, rows, 2):
            pygame.draw.rect(screen, forest_green, (col * squaresize, row*squaresize, squaresize, squaresize))

      # next time
      # figure out efficent method to represent the board for user
# drawing 8 by 8 grid


# placing pieces using fen representation
# upper case white pieces
# lower case black pieces
# / next row start from 8th row

#main()
pygame.quit()
