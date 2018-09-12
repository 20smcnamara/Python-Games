import pygame
import random
import time
import math


class Snake:

    def __init__(self, bike_id, pos, snake_color):
        self.x = pos[0]
        self.y = pos[1]
        self.OGX = pos[0]
        self.OGY = pos[1]
        self.color = snake_color
        self.lives = 3
        self.lastKey = ""
        self.score = 0
        self.id = bike_id
        self.wait = 0
        self.affected = [[int(pos[0]/tile_size), int(pos[1]/tile_size)]]
        self.wait = True

    def move(self):
        if self.wait == 0:
            if self.lastKey == "up":
                self.y -= tile_size
            if self.lastKey == "down":
                self.y += tile_size
            if self.lastKey == "left":
                self.x -= tile_size
            if self.lastKey == "right":
                self.x += tile_size
            if self.x > size - 1:
                self.crash("out of bounds")
            if self.x < 0:
                self.crash("out of bounds")
            if self.y > size - 1:
                self.crash("out of bounds")
            if self.y < 0:
                self.crash("out of bounds")
        first_index = 0
        if len(self.affected) == 75:
            first_index = 2
        for p in range(first_index, len(self.affected)-2):
            if not points_2d[self.affected[p][0]][self.affected[p][1]].update():
                if not self.wait:
                    del self.affected[0]

    def update(self):
        if self.wait == 0:
            global points, screen, statuses
            point = points_2d[int(self.x/tile_size)][int(self.y/tile_size)]
            if point.color != [0, 0, 0]:
                self.crash(point.color)
                return
            point.ttd = 75
            point.color = self.color
            self.affected.append(point.indexes)

            statuses[self.id] = 0
        else:
            self.wait -= 1

    def crash(self, reason):
        global statuses, b15
        #b15 = True
        statuses[self.id] = 1
        self.x = self.OGX
        self.y = self.OGY
        self.lastKey = ""
        self.wait = 5
        for cords in self.affected:
            p = points_2d[cords[0]][cords[1]]
            p.ttd = 0
            p.update()
        #self.affected = [[int(self.x/tile_size), int(self.y/tile_size)]]
        self.affected = []

    def get_move(self):
        global P2_key
        b3 = False
        self.lastKey = P2_key
        moves = ["left", "right", "up", "down"]
        for point in points:
            if point.ttd > 0:
                if self.y == point.y:
                    if "right" in moves:
                        if self.x + tile_size == point.x:
                            moves.remove("right")
                    if "left" in moves:
                        if self.x - tile_size == point.x:
                            moves.remove("left")
                if self.x == point.x:
                    if "down" in moves:
                        if self.y + tile_size == point.y:
                            moves.remove("down")
                    if "up" in moves:
                        if self.y - tile_size == point.y:
                            moves.remove("up")
        x_add = 0
        y_add = 0
        if self.lastKey == "up":
            y_add = -tile_size
        if self.lastKey == "down":
            y_add = tile_size
        if self.lastKey == "left":
            x_add = -tile_size
        if self.lastKey == "right":
            x_add = tile_size
        b5 = False
        try:
            if self.x + tile_size > size - 1 and P2_key == "right":
                b5 = True
                moves.remove("right")
            if self.x - tile_size < 0 and P2_key == "left":
                b5 = True
                moves.remove("left")
        except ValueError:
            x = 0
        try:
            if self.y + tile_size > size - 1 and P2_key == "down":
                b5 = True
                moves.remove("down")
            if self.y - tile_size < 0 and P2_key == "up":
                b5 = True
                moves.remove("up")
        except ValueError:
            x = 0
        for point in points:
            if point.x == self.x + x_add and point.y == self.y + y_add and point.ttd > 0:
                b3 = True
        if len(moves) > 0 and (b3 or b5):
            P2_key = random.choice(moves)
            self.lastKey = P2_key


class AIBike(Snake):

    def __init__(self, bike_id, pos, snake_color):
        Snake.__init__(self, bike_id, pos, snake_color)
        self.least = 0

    def get_move(self):
        if self.wait == 0:
            statuses[self.id] = 0
            while statuses[self.id] == 1 or self.id == self.least:
                self.least = random.randint(0, 4)
            moves = ["left", "right", "up", "down"]
            cords = []
            x_cord = int(self.x/tile_size)
            y_cord = int(self.y/tile_size)
            x_cords = [x_cord-1, x_cord, x_cord+1]
            y_cords = [y_cord-1, y_cord, y_cord+1]

            for x in x_cords:
                for y in y_cords:
                    if x != int(self.x/tile_size) or y != int(self.y/tile_size):
                        cords.append([x, y])
            for cord in cords:
                try:
                    point = points_2d[cord[0]][cord[1]]
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
                except IndexError:
                    dsa = 0
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
                    if bikes[self.least].x > self.x and moves.index("right") > -1:
                        primary.append("right")
                        b = False
                    elif bikes[self.least].x < self.x and moves.index("left") > -1:
                        primary.append("left")
                        b = False
                    if bikes[self.least].y > self.y and moves.index("down") > -1:
                        primary.append("down")
                        b = False
                    elif bikes[self.least].y < self.y and moves.index("up") > -1:
                        primary.append("up")
                        b = False
                except ValueError:
                     x = 0
                if b:
                    self.lastKey = random.choice(moves)
                    self.move()
                else:
                    self.lastKey = random.choice(primary)
                    self.move()
                self.update()
            else:
                self.crash("No where to go")
        else:
            self.wait -= 1

    def crash(self, reason):
        statuses[self.id] = 1
        self.x = self.OGX
        self.y = self.OGY
        self.lastKey = ""
        for cords in self.affected:
            p = points_2d[cords[0]][cords[1]]
            p.ttd = 0
            p.update()
        self.least = self.id
        self.wait = 5
        while self.least == self.id:
            self.least = random.randint(0, 4)
        self.affected = []


class Position:

    def __init__(self, x_cord, y_cord, indexes):
        self.indexes = indexes
        self.x = x_cord
        self.y = y_cord
        self.color = [0, 0, 0]
        self.ttd = 0

    def update(self):
        global snake
        if self.ttd > 0:
            self.ttd -= 1
        if self.ttd == 0:
            self.color = [0, 0, 0]
        pygame.draw.rect(screen, self.color, (self.x, self.y, tile_size, tile_size))
        return self.ttd > 0


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
size = 300
screen = pygame.display.set_mode([size, size])
pygame.display.set_caption("Snake")
tile_size = 3
statuses = [0, 0, 0, 0, 0]
P2_key = ""
b15 = False
print("On")
while True:
    points = []
    points_2d = []
    w = 0
    for zyx in range(0, size, tile_size):
        points_2d.append([])
        h = 0
        for xyz in range(0, size, tile_size):
            points.append(Position(zyx, xyz, [w, h]))
            points_2d[w].append(points[len(points)-1])
            h += 1
        w += 1
    start = size/10
    while start % tile_size != 0:
        start -= 1
    snake = Snake(0, [start, start], (0, 255, 0))
    start = size-size/10
    while start % tile_size != 0:
        start -= 1
    bike1 = AIBike(1, [start, start], (0, 0, 255))
    start = size / 2
    while start % tile_size != 0:
        start -= 1
    bike2 = AIBike(2, [start, start], (255, 0, 0))
    start = size/10
    start2 = size-size/10
    while start % tile_size != 0:
        start -= 1
    while start2 % tile_size != 0:
        start2 -= 1
    bike3 = AIBike(3, [start, start2], (255, 0, 255))
    start = size - size/10
    start2 = size/10
    while start % tile_size != 0:
        start -= 1
    while start2 % tile_size != 0:
        start2 -= 1
    bike4 = AIBike(4, [start, start2], (255, 255, 0))
    bikes = [snake, bike1, bike2, bike3, bike4]
    for b in bikes:
        b.crash("Start")
    b10 = False
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.KEYDOWN:
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
                if event.key == pygame.K_SLASH or event.key == pygame.K_q:
                    b10 = not b10
                    if not b10:
                        print("On")
                    else:
                        print("Off")
                if event.key == pygame.K_SLASH or event.key == pygame.K_r:
                    b15 = not b15
        snake.lastKey = P2_key
        for b in bikes:
            if b != snake:
                b.get_move()
            elif not b10:
                b.get_move()
        snake.move()
        snake.update()
        if b15:
            for point in points:
                point.update()
        pygame.display.update()
        time.sleep(.05)
