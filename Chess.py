

import pygame




fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
chess_val = {"p":1,"r":5,"n":3,"b":3,"q":9,"k":10000,"P":1,"R":5,"N":3,"B":3,"Q":9,"K":10000}
print(chess_val["p"])

def movepieces(running):
  movetracking = []
  recorder = (0,0)
  start_pos = []
  destination_pos = []
  ev = pygame.event.get()
  for event in ev:
    if event.type == pygame.MOUSEBUTTONUP:
      recorder = pygame.mouse.get_pos()
      print(recorder)
      movetracking.append(recorder)
  # in this for loop. I am trying to seperate user's mouse buttonclick, in to seperate list  
  for i in range(len(movetracking)):
    if i%2 != 0:
      start_pos.append(movetracking[i])
    else:
      destination_pos.append(movetracking[i])
    print(movetracking,start_pos,destination_pos)

white_pos_val, black_pos_val = (0,0)

def redraw():
  pass

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

Images = {}
running = True
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
squaresize = height // 8

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
    for y in range(8):
      if(chessboard[x][y] != "/"):
        image = pygame.image.load('Chess_'+ chessboard[x][y] +'.png')
        screen.blit(image, pygame.Rect(y * squaresize - 5, squaresize * x - 5, squaresize,squaresize))

white = (255,255,255)
forest_green = (34,139,34) # forest_green
rows = col = 8
def drawsquare(screen):
    screen.fill(white)
    for row in range(rows):
        for col in range(row % 2, rows, 2):
            pygame.draw.rect(screen, forest_green, (col * squaresize, row*squaresize, squaresize, squaresize))

main()
pygame.quit()
