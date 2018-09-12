import pygame
import time
import random
 
pygame.init()
UP = False
Down = False
display_width = 975
display_height = 800
ballx = 400
bally = 300
term = 0

def setcolor():
      global term
      global color
      if term == 0:
            color[0]+=10
      elif term == 1:
            color[1]+=10
      elif term == 2:
            color[0]-=10
      elif term == 3:
            color[2]+=10
      elif term == 4:
            color[1]-=10
      elif term == 5:
            color[2]+=10
      elif term == 6:
            color[1]-=10
      elif term == 7:
            color[0]+=10

def termset():
      global term
      global color
      if term == 0 and color[0] > 230:
            term+=1
            return()
      elif term == 1 and color[1]>230:
            term+=1
            return
      elif term == 2 and color[0] < 10:
            color[0] = 10
            term+=1
            return()
      elif term == 3 and color[2]>230:
            term+=1
            return
      elif term == 4 and color[1] < 10:
            color[1] = 10
            term+=1
            return()
      elif term == 5 and color[2]>230:
            term+=1
            return
      elif term == 6 and color[1] < 10:
            color[2] = 10
            term+=1
            return()
      elif term == 7 and color[0]>230:
            term=1
            return

def testcolor():
      termset()
      setcolor()
      
color = [50,0,0]
back = pygame.image.load('colin.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A Pong')
clock = pygame.time.Clock()
moveable = [7,-7]  
ballxadd = random.choice(moveable)
if ballxadd == 0:
      ballxadd = 1
ballyadd = random.choice(moveable)
if ballyadd == 0:
      ballyadd = -1
cpux = 955
cpuy = 453
black = [0,0,0]
white = [255,255,255]
gameDisplay.fill(color)
done = False
playerscore = 0
cpuscore = 0
x_cords = 20
y_cords = 300

def run():
      global ballxadd,ballyadd,ballx,bally,cpux,cpuy,cpuscore,playerscore,y_cords,x_cords,UP,Down
      while True:
            ballx += ballxadd
            bally += ballyadd
            if ballx > (x_cords-5) and ballx < (x_cords+5):
                  if bally > (y_cords-25) and bally < (y_cords+25):
                        ballxadd*=-1
            if ballx > (cpux-5) and ballx < (cpux+5):
                  if bally > (cpuy-30) and bally < (cpuy+30):
                        ballxadd*=-1
            if bally < 895:
                  ballyadd*=-1
            if bally > 5:
                  ballyadd*=-1
            if ballx > 955:
                  score(1)
            if ballx < 10:
                  score(0)
            if bally > cpuy:
                  cpuy+=8
            elif bally < cpuy:
                  cpuy-=8
            pygame.draw.rect(gameDisplay, color, (955, cpuy, 10, 50))
            pygame.draw.rect(gameDisplay, color, (20, y_cords, 10, 50))
            pygame.draw.rect(gameDisplay, color, (ballx, bally, 5, 5))
            pygame.display.update()
            gameDisplay.blit(back,(0,0))
            
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                  if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                              UP = False
                        if event.key == pygame.K_s:
                              Down = False
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                              UP = True
                        if event.key == pygame.K_s:
                              Down = True
                        #time.sleep(.01)
            if UP:
                  if y_cords > 50:
                        y_cords-=9
            if Down:
                  if y_cords < 965:
                        y_cords+=9
            time.sleep(.01)
            testcolor()

def score(scorer):
    
      global playerscore
      global cpuscore
      global ballx
      global bally
      global y_cords
      if scorer == 1:
            cpuscore+=1
      if scorer == 0:
            playerscore+=1
      ballx = 400
      bally = 300
      cpuy = 300
      y_cords = 300
      run()
      print("You", playerscore, "Cpu", cpuscore)
      
def start():
      moveable = [.5,-.5]  
      ballxadd = random.choice(moveable)
      ballyadd = random.choice(moveable)
      run()

start()
