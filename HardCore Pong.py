import pygame
import time
import random
import math
 
pygame.init()
UP = False
Down = False
str123 = ""
size = [750, 500]
while str123 != "small" and str123 != "large":
        str123 = input("Larger screen or small screen ")

if str123 == "large":
        size = [975, 915]
        
display_width = size[0]
display_height = size[1]
ball_width = 15
ball_x = math.ceil(display_width / 2)
bally = random.randint(ball_width, display_width - ball_width)
term = 0


class Color:
        
        def __init__(self, increase=25, start_color=[255, 0, 0, 4], ind=5):
                self.index = ind
                self.increase = increase
                self.color = start_color
                self.b = False
                if ind == 2:
                        self.b = True
                self.check_index()

        def check_index(self):
                if self.index == 1 and self.color[1] > 254-self.increase:
                        self.index += 1
                        self.color[1] = 255
                if self.index == 2 and self.color[0] < self.increase+150:
                        self.index += 1
                        self.color[0] = 150
                if self.index == 3 and self.color[2] > 254-self.increase:
                        self.index += 1
                        self.color[2] = 255
                if self.index == 4 and self.color[1] < self.increase+150:
                        self.index += 1
                        self.color[1] = 150
                if self.index == 5 and self.color[0] > 254-self.increase:
                        self.index += 1
                        self.color[0] = 255
                if self.index == 6 and self.color[2] < self.increase+150:
                        self.index = 1
                        self.color[2] = 150

        def adjust(self):
                self.check_index()
                if self.index == 1:
                        self.color[1] += self.increase
                if self.index == 2:
                        self.color[0] -= self.increase
                if self.index == 3:
                        self.color[2] += self.increase
                if self.index == 4:
                        self.color[1] -= self.increase
                if self.index == 5:
                        self.color[0] += self.increase
                if self.index == 6:
                        self.color[2] -= self.increase
                self.check_index()
                return self.color


class Bar:

        def __init__(self, x, w, start_color, ind):
                self.x = x
                self.color = Color(5, start_color, ind)
                self.w = w

        def draw(self):
                global display_height, display_width
                c = self.color.adjust()
                pygame.draw.rect(gameDisplay, c, (self.x, 0, self.w, display_height))


def bar_maker():
        global display_width, bars
        width_of_bar = 10
#       width of a bar
        for x in range(0, int(display_width), width_of_bar):
                c = [display_width/width_of_bar*(x+1)/1000, 0, 0, 5]

                while c[0] > 255*3:
                        c[0] -= 255*3
                if c[0] < 255:
                        c = c
                elif c[0] < 255*2:
                        c = [255, c[0]-255, 0, 1]
                else:
                        c = [255-(c[0]-255*2), 255, 0, 2]
                bars.append(Bar(x, width_of_bar, c, c[3]))


def if_neg(x):
        if x < 0:
                return x*-1
        return x


def bar_helper():
        global bars
        for b in bars:
                b.draw()


color = Color(1)
back = pygame.image.load('colin.png')
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Pong')
clock = pygame.time.Clock()
movable = [6, -6]

ball_x_add = random.choice(movable)
ball_y_add = random.choice(movable)
cpu_x = display_width - 20
cpu_y = display_width / 2
black = [0, 0, 0]
white = [255, 255, 255]
gameDisplay.fill(color.adjust())
done = False
player_score = 0
cpu_score = 0
x_cords = 20
width = 75
y_cords = display_height/2-(width/2)
bars = []
bar_maker()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
paddy = if_neg(ball_x_add*.9)
wi = 15
speed = .0001
if str123 == "small":
        width = 75
        ball_width = 15
        wi = 15

        speed = .001
        ball_x_add = int(ball_x_add / 4)
        ball_y_add = int(ball_y_add / 4)
        paddy = if_neg(ball_x_add)*.6
        

class Button:
        def __init__(self, x, y, w, h, text):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.text = text
                self.color = Color(50)

        def draw(self):
                global my_font
                pygame.draw.rect(gameDisplay, self.color.adjust(), (self.x-self.w/4, self.y, self.w, self.h))
                gameDisplay.blit(my_font.render(self.text, False, (0, 0, 0)), (self.x, self.y))

        def is_pressed(self):
                mouse = pygame.mouse.get_pos()
                b = self.x < mouse[0] < self.x+self.w and self.y < mouse[1] < self.y+self.h
                return pygame.mouse.get_pressed()[0] == 1 and b
        

def start_screen():
        global size
        b1 = Button(size[0]/2-110, size[1]/2-25, 100, 50, "Play")
        b2 = Button(size[0]/2+10, size[1]/2-25, 100, 50, "Quit")
        c = Color(3, [255, 255, 0, 4], 2)
        while True:
                pygame.draw.rect(gameDisplay, c.adjust(), (0, 0, display_width, display_height))
                b1.draw()
                b2.draw()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                if b1.is_pressed():
                        start()
                        return
                if b2.is_pressed():
                        pygame.quit()
                        return
                pygame.display.update()
                time.sleep(.1)
        

def run():
    global back, ball_x_add, my_font, ball_y_add, size, paddy, speed, str123, ball_x, bally, wi, cpu_x, cpu_y
    global cpu_score, player_score, y_cords, x_cords, ball_width, UP, Down, width, display_width, display_height
    delay = 0
    ball_x = display_width / 2
    bally = random.randint(ball_width + 5, display_height - ball_width - 5)
    while True:
        if delay > 0:
            delay -= 1
        ball_x += ball_x_add
        bally += ball_y_add
        if ball_x < x_cords+wi:
            if bally < y_cords+width and bally+ball_width > y_cords:
                if delay == 0:
                    ball_x_add *= -1
                    delay = 10

        if ball_x+ball_width > cpu_x:
            if bally < cpu_y + width:
                if bally+ball_width > cpu_y:
                    if delay == 0:
                        ball_x_add *= -1
                        delay = 10
        if bally > display_height-ball_width:
            ball_y_add *= -1
        if bally <= 0:
            ball_y_add *= -1
        if ball_x > display_width-1:
            score(1)
        if ball_x < 1:
            score(0)
        if bally > cpu_y and cpu_y < display_height-width:
            cpu_y += paddy
        elif bally < cpu_y and cpu_y > 0:
            cpu_y -= paddy
        c = color.adjust()
        pygame.draw.rect(gameDisplay, c, (display_width - 50, cpu_y, wi, width))
        pygame.draw.rect(gameDisplay, c, (20, y_cords, wi, width))
        f = my_font.render(("You " + str(player_score) + " Cpu " + str(cpu_score)), False, (255, 255, 255))
        gameDisplay.blit(f, (size[0] / 2 - 75, 10))
        pygame.draw.rect(gameDisplay, c, (ball_x, bally, ball_width, ball_width))
        pygame.display.update()
#        barHelper()
#        pygame.draw.rect(gameDisplay, color.adjust(), (0, 0, display_width, display_height))
        gameDisplay.blit(back, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
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
        if UP:
            if y_cords >= 0:
                y_cords -= paddy
        if Down:
            if y_cords <= display_height-width:
                y_cords += paddy
        time.sleep(speed)


def score(scorer):
    global player_score, cpu_score, ball_x, bally, y_cords, width, cpu_y
    if scorer == 1:
        player_score += 1
    if scorer == 0:
        cpu_score += 1
    ball_x = display_width / 2
    bally = random.randint(ball_width + 5, display_height - ball_width - 5)
    cpu_y = display_height/2-(width/2)
    y_cords = display_height/2-(width/2)
    print("You", player_score, "Cpu", cpu_score)
    run()


def start():
    run()


start_screen()
