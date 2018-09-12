import pygame
import random
import time


class Snake:

        def __init__(self, pos, snake_color):
            self.x = pos[0]
            self.y = pos[1]
            self.OGX = pos[0]
            self.OGY = pos[1]
            self.ttd = 50
            self.color = snake_color
            self.lives = 3
            self.lastKey = ""
            self.score = 0

        def move(self, key):
            last_key = key
            if last_key == "up":
                self.y -= tile_size
            if last_key == "down":
                self.y += tile_size
            if last_key == "left":
                self.x -= tile_size
            if last_key == "right":
                self.x += tile_size
            if self.x > size-1:
                self.crash()
            if self.x < 0:
                self.crash()
            if self.y > size-1:
                self.crash()
            if self.y < 0:
                self.crash()

        def update(self):
            global points, screen
            for point in points:
                if point.x == self.x and point.y == self.y:
                    if point.color != [0, 0, 0] and point.color != food_color:
                        self.crash()
                        return
                    point.ttd = self.ttd
                    point.color = self.color
            if self.x == currentFood.x and self.y == currentFood.y:
                self.ttd += 1
            pygame.draw.rect(screen, [0, 255, 180], (self.x, self.y, tile_size, tile_size))
            if self.ttd >= size*size:
                self.crash()

        def crash(self):
            print("Score,", self.ttd)
            self.color = [0, 255, 0]
            self.x = self.OGX
            self.y = self.OGY
            self.lastKey = ""
            self.ttd = 1
            for point in points:
                point.ttd = 0


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
                self.color = [0, 255, 180]
            if self.ttd == 0:
                self.color = [0, 0, 0]
            if self.ttd == -1:
                self.color = food_color
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


class Food:

        def __init__(self):
            global points
            self.square = random.choice(points)
            self.x = self.square.x
            self.y = self.square.y
            self.square.ttd = -1
            self.square.color = (255, 0, 0)

        def update(self):
            if self.square.ttd != -1:
                self.reset()

        def reset(self):
            global points
            self.square = random.choice(points)
            while self.square.color == (0, 255, 0):
                self.square = random.choice(points)
            self.x = self.square.x
            self.y = self.square.y
            self.square.ttd = -1
            self.square.color = (255, 0, 0)


pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
size = 500
screen = pygame.display.set_mode([size, size])
pygame.display.set_caption("Snake")
food_color = (255, 0, 0)
color = Color()
tile_size = 10

while True:
    points = []
    for zyx in range(0, size, tile_size):
        for xyz in range(0, size, tile_size):
            points.append(Position(zyx, xyz))
    currentFood = Food()
    start = size/2
    while start % tile_size != 0:
        start -= 1
    snake = Snake([start, start], (0, 255, 180))
    time.sleep(.01)
    P2_key = ""
    delay = .015
    playing = True
    y = 0
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    quit(0)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if P2_key != "left" or snake.ttd == 1:
                        P2_key = "right"
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if P2_key != "right" or snake.ttd == 1:
                        P2_key = "left"
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if P2_key != "down" or snake.ttd == 1:
                        P2_key = "up"
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if P2_key != "up" or snake.ttd == 1:
                        P2_key = "down"
        snake.move(P2_key)
        snake.update()
        pygame.display.update()
        food_color = color.adjust()
        for p in points:
            p.update()
        currentFood.update()
        time.sleep(.05)
