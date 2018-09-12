import pygame
import random
import time
import math


class Snake:

    def __init__(self, pos, snake_color):
        self.x = pos[0]
        self.y = pos[1]
        self.OGX = pos[0]
        self.OGY = pos[1]
        self.color = snake_color
        self.lives = 3
        self.lastKey = ""
        self.score = 0

    def move(self, key):
        self.lastKey = key
        if self.lastKey == "up":
            self.y -= tile_size
        if self.lastKey == "down":
            self.y += tile_size
        if self.lastKey == "left":
            self.x -= tile_size
        if self.lastKey == "right":
            self.x += tile_size
        if self.x > size - 1:
            self.crash()
        if self.x < 0:
            self.crash()
        if self.y > size - 1:
            self.crash()
        if self.y < 0:
            self.crash()

    def update(self):
        global points, screen
        for point in points:
            if point.x == self.x and point.y == self.y:
                if point.color != [0, 0, 0]:
                    self.crash()
                    return
                point.ttd = 100
                point.color = self.color
        pygame.draw.rect(screen, self.color, (self.x, self.y, tile_size, tile_size))

    def crash(self):
        print(pygame.mouse.get_pos())
        self.x = self.OGX
        self.y = self.OGY
        self.lastKey = ""
        for point in points:
            if point.color == self.color:
                point.ttd = 0

    def get_move(self):
        moves = ["left", "right", "up", "down"]
        '''
        for point in points:
            if point.ttd > 0:
                if self.y == point.y:
                    if self.x + tile_size == point.x:
                        moves.remove("right")
                    if self.x - tile_size == point.x:
                        moves.remove("left")
                if self.x == point.x:
                    if self.y + tile_size == point.y:
                        moves.remove("down")
                    if self.y - tile_size == point.y:
                        moves.remove("up")
        primary = []
        least = pygame.mouse.get_pos()
        try:
            if least[0] > self.x and moves.index("right") > -1:
                primary.append("right")
                b = False
            elif least[0] < self.x and moves.index("left") > -1:
                primary.append("left")
                b = False
            if least[1] > self.y and moves.index("down") > -1:
                primary.append("down")
                b = False
            elif least[1] < self.y and moves.index("up") > -1:
                primary.append("up")
                b = False
        except ValueError:
            x = 0
        if len(primary) != 0:
            self.move(random.choice(primary))
        else:
            try:
                self.move(random.choice(moves))
            finally:
                self.crash()
        '''

class AIBike(Snake):

    def __init__(self, pos, snake_color):
        Snake.__init__(self, pos, snake_color)

    def get_move(self):
        moves = ["left", "right", "up", "down"]
        for point in points:
            if point.ttd > 0:
                if self.y == point.y:
                    if self.x + tile_size == point.x:
                        moves.remove("right")
                    if self.x - tile_size == point.x:
                        moves.remove("left")
                if self.x == point.x:
                    if self.y + tile_size == point.y:
                        moves.remove("down")
                    if self.y - tile_size == point.y:
                        moves.remove("up")
        try:
            if self.lastKey == "up" and moves.index("down") > -1:
                moves.remove("down")
            if self.lastKey == "down" and moves.index("up") > -1:
                moves.remove("up")
            if self.lastKey == "right" and moves.index("left") > -1:
                moves.remove("left")
            if self.lastKey == "left" and moves.index("right") > -1:
                moves.remove("right")

            if self.x+tile_size > size-1 and moves.index("right") > -1:
                moves.remove("right")
            if self.x-tile_size < 0 and moves.index("left") > -1:
                moves.remove("left")
            if self.y+tile_size > size-1 and moves.index("down") > -1:
                moves.remove("down")
            if self.y-tile_size < 0 and moves.index("up") > -1:
                moves.remove("up")
        except:
            x = 0
        if len(moves) > 0:
            primary = []
            b = True
            try:
                if self.least.x > self.x and moves.index("right") > -1:
                    primary.append("right")
                    b = False
                elif self.least.x < self.x and moves.index("left") > -1:
                    primary.append("left")
                    b = False
                if self.least.y > self.y and moves.index("down") > -1:
                    primary.append("down")
                    b = False
                elif self.least.y < self.y and moves.index("up") > -1:
                    primary.append("up")
                    b = False
            except ValueError:
                 x = 0
            if b:
                self.move(random.choice(moves))
            else:
                self.move(random.choice(primary))
            self.update()
        else:
            self.crash()

    def crash(self):
        self.x = self.OGX
        self.y = self.OGY
        self.lastKey = ""
        for point in points:
            if point.color == self.color:
                point.ttd = 0
        self.least = self
        while self.least == self:
            self.least = random.choice(bikes)

class DumbAIBike(Snake):

    def __init__(self, pos, snake_color):
        Snake.__init__(self, pos, snake_color)

    def get_move(self):
        moves = ["left", "right", "up", "down"]
        for point in points:
            if point.ttd > 0:
                if self.y == point.y:
                    if self.x + tile_size == point.x:
                        moves.remove("right")
                    if self.x - tile_size == point.x:
                        moves.remove("left")
                if self.x == point.x:
                    if self.y + tile_size == point.y:
                        moves.remove("down")
                    if self.y - tile_size == point.y:
                        moves.remove("up")

        if self.lastKey == "up" and moves.index("down") > -1:
            moves.remove("down")
        if self.lastKey == "down" and moves.index("up") > -1:
            moves.remove("up")
        if self.lastKey == "right" and moves.index("left") > -1:
            moves.remove("left")
        if self.lastKey == "left" and moves.index("right") > -1:
            moves.remove("right")

        if self.x+tile_size > size-1 and moves.index("right") > -1:
            moves.remove("right")
        if self.x-tile_size < 0 and moves.index("left") > -1:
            moves.remove("left")
        if self.y+tile_size > size-1 and moves.index("down") > -1:
            moves.remove("down")
        if self.y-tile_size < 0 and moves.index("up") > -1:
            moves.remove("up")
        if len(moves) > 0:
            self.move(random.choice(moves))
            self.update()
        else:
            self.crash()


class Position:

    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord
        self.color = [0, 0, 0]
        self.ttd = 0

    def update(self):
        global snake, food_color
        if self.ttd > 0:
            self.ttd -= 1
        if self.ttd == 0:
            self.color = [0, 0, 0]
        pygame.draw.rect(screen, self.color, (self.x, self.y, tile_size, tile_size))


class Color:

    def __init__(self, increase=50, start_color=[255, 0, 0, 4], ind=5):
        self.index = ind
        self.increase = increase
        self.color = start_color
        self.b = False
        if ind == 2:
            self.b = True
        self.check_index()

    def check_index(self):
        if self.index == 1 and self.color[1] > 254 - self.increase:
            self.index += 1
            self.color[1] = 255
        if self.index == 2 and self.color[0] < self.increase + 1:
            self.index += 1
            self.color[0] = 0
        if self.index == 3 and self.color[2] > 254 - self.increase:
            self.index += 1
            self.color[2] = 255
        if self.index == 4 and self.color[1] < self.increase + 1:
            self.index += 1
            self.color[1] = 0
        if self.index == 5 and self.color[0] > 254 - self.increase:
            self.index += 1
            self.color[0] = 255
        if self.index == 6 and self.color[2] < self.increase + 1:
            self.index = 1
            self.color[2] = 0

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


def play():
    global loading
    loading = False
    pygame.quit()


def end():
    global loading, looping
    loading = False
    looping = False
    pygame.quit()

def find_dist(one, two, three):
    t1 = (math.fabs(one.x - two.x) ** 2 + math.fabs(one.y - two.y) ** 2) ** .5
    t2 = (math.fabs(one.x - three.x) ** 2 + math.fabs(one.y - three.y) ** 2) ** .5
    return t1 < t2


pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
size = 500
screen = pygame.display.set_mode([size, size])
pygame.display.set_caption("Snake")
food_color = (255, 0, 0)
color = Color()
tile_size = 5

def update_game():
    global sda
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
        if event.type == pygame.KEYDOWN and event.key != last_event:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                quit(0)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if P2_key != "left":
                    P2_key = "right"
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if P2_key != "right":
                    P2_key = "left"
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if P2_key != "down":
                    P2_key = "up"
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if P2_key != "up":
                    P2_key = "down"
            last_event = event.key
    snake.move(P2_key)
    snake.update()
    for b in bikes:
        b.get_move()
    pygame.display.update()
    food_color = color.adjust()
    for p in points:
        p.update()
    sda += 1
    time.sleep(.05)


sda = 0
points = []
for zyx in range(0, size, tile_size):
    for xyz in range(0, size, tile_size):
        points.append(Position(zyx, xyz))
start = 100
while start % tile_size != 0:
    start -= 1
snake = Snake([start, start], (0, 255, 0))
start = size-100
while start % tile_size != 0:
    start -= 1
bike1 = AIBike([start, start], (0, 0, 255))
start = size / 2
while start % tile_size != 0:
    start -= 1
bike2 = AIBike([start, start], (255, 0, 0))
start = 100
start2 = size-100
while start % tile_size != 0:
    start -= 1
while start2 % tile_size != 0:
    start2 -= 1
bike3 = AIBike([start, start2], (255, 0, 255))
start = size - 100
start2 = 100
while start % tile_size != 0:
    start -= 1
while start2 % tile_size != 0:
    start2 -= 1
bike4 = AIBike([start, start2], (255, 255, 0))
bikes = [bike1, bike2, bike3, bike4, snake]
for b in bikes:
    b.crash()
time.sleep(.01)
P2_key = ""
delay = .015
playing = True
y = 0
last_event = ""
