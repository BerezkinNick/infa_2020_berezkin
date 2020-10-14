import pygame
from pygame.draw import *
from math import *
from random import *
from os import path
pygame.init()

width = 900
height = 780
FPS = 30
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0

def new_ball():
    global x, y, r, v, angle, color
    x = randint(100, width - 100)
    y = randint(100, height - 100)
    r = randint(20, 100)
    v = randint(10, 500)
    angle = radians(randint(0, 360))
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ball2():
    global x2, y2, r2, v2, angle2, color2
    x2 = randint(100, width - 100)
    y2 = randint(100, height - 100)
    r2 = randint(20, 100)
    v2 = randint(10, 500)
    angle2 = radians(randint(0, 360))
    color2 = COLORS[randint(0, 5)]
    circle(screen, color2, (x2, y2), r2)

def new_ring():
    global x5, y5, r5, v5, angle5, color5
    x5 = randint(100, width - 100)
    y5 = randint(100, height - 100)
    r5 = randint(20, 100)
    v5 = randint(10, 500)
    angle5 = radians(randint(0, 360))
    color5 = COLORS[randint(0, 5)]
    circle(screen, color5, (x5, y5), r5, 10)
    
def new_sqare():
    global x3, y3, a, b, v3, angle3, color3
    a=randint(50, 120)
    b=a
    x3 = randint(0, width-a)
    y3 = randint(0, height-a)
    v3 = randint(400, 500)
    angle3 = radians(randint(0, 360))
    color3 = COLORS[randint(0, 5)]
    rect(screen, color3, [x3, y3, a, b])

def new_sqare2():
    global x4, y4, c, d, f, v4, angle4, color4
    c=randint(50, 120)
    f=randint(20, 40)
    d=c
    x4 = randint(0, width-c)
    y4 = randint(0, height-d)
    v4 = randint(400, 500)
    angle4 = radians(randint(0, 360))
    color4 = COLORS[randint(0, 5)]
    rect(screen, color4, [x4, y4, c, d], f)
    


def move_ball():
    global x, y, r, v, angle, color
    circle(screen, BLACK, (x, y), r)
    x += round(v / 40 * cos(angle))
    y -= round(v / 40 * sin(angle))
    circle(screen, color, (x, y), r)
    pygame.display.update()
    wall()
    
def move_ball2():
    global x2, y2, r2, v2, angle2, color2
    circle(screen, BLACK, (x2, y2), r2)
    x2 += round(v2 / FPS * cos(angle2))
    y2 -= round(v2 / FPS * sin(angle2))
    circle(screen, color2, (x2, y2), r2)
    pygame.display.update()
    wall2()

def move_ring():
    global x5, y5, r5, v5, angle5, color5
    circle(screen, BLACK, (x5, y5), r5)
    x5 += round(v5 / 30 * cos(angle5))
    y5 -= round(v5 / 30 * sin(angle5))
    circle(screen, color5, (x5, y5), r5, 10)
    pygame.display.update()
    wall5()

def move_sqare():
    global x3, y3, a, b, v3, angle3, color3
    rect(screen, BLACK, [x3, y3, a, b])
    x3 += round(v3 / FPS * cos(angle3))
    y3 -= round(v3 / FPS * sin(angle3))
    rect(screen, color3, [x3, y3, a, b])
    pygame.display.update()
    wall3()


def wall():
    global x, y, r, angle
    if x + r > width:
        angle = pi - angle
    if x - r < 0:
        angle = pi - angle
    if y + r > height:
        angle = 2 * pi - angle
    if y - r < 0:
        angle = 2 * pi - angle
    
def wall2():
    global x2, y2, r2, angle2
    if x2 + r2 > width:
        angle2 = pi - angle2
    if x2 - r2 < 0:
        angle2 = pi - angle2
    if y2 + r2 > height:
        angle2 = 2 * pi - angle2
    if y2 - r2 < 0:
        angle2 = 2 * pi - angle2

def wall5():
    global x5, y5, r5, angle5
    if x5 + r5 > width:
        angle5 = pi - angle5
    if x5 - r5 < 0:
        angle5 = pi - angle5
    if y5 + r5 > height:
        angle5 = 2 * pi - angle5
    if y5 - r5 < 0:
        angle5 = 2 * pi - angle5

def wall3():
    global x3, y3, a, angle3
    if x3 + a > width:
        angle3 = pi - angle3
    if x3 < 0:
        angle3 = pi - angle3
    if y3 + a > height:
        angle3 = 2 * pi - angle3
    if y3 < 0:
        angle3 = 2 * pi - angle3

def wall4():
    global x4, y4, c, angle4
    if x4 + c > width:
        angle4 = pi - angle4
    if x4 < 0:
        angle4 = pi - angle4
    if y4 + c > height:
        angle4 = 2 * pi - angle4
    if y4 < 0:
        angle4 = 2 * pi - angle4



def click(event):
    global score
    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
        score += 1
        print(score)
        return 1


def click2(event):
    global score
    if (x2 - event.pos[0]) ** 2 + (y2 - event.pos[1]) ** 2 <= r2 ** 2:
        score += 1
        print(score)
        return 1

def click3(event):
    global score
    if x3 + a > event.pos[0] and event.pos[0]>x3 and y3 + a > event.pos[1] and event.pos[1] > y3:
        score += 2
        print(score)
        return 1
    
def click5(event):
    global score
    if (x5 - event.pos[0]) ** 2 + (y5 - event.pos[1]) ** 2 <= r5 ** 2 and (x5 - event.pos[0]) ** 2 + (y5 - event.pos[1]) ** 2 >= (r5-10) ** 2:
        score += 4
        print(score)
        return 1

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    new_ball()
    new_ball2()
    new_sqare()
    new_ring()
    pygame.display.update()
    while 1:
        clock.tick(FPS)
        move_ball()
        move_ball2()
        move_sqare()
        move_ring()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if click(event)==1:
                    circle(screen, BLACK, (x, y), r)
                    new_ball()
                if click2(event)==1:
                    circle(screen, BLACK, (x2, y2), r2)
                    new_ball2()
                if click3(event)==1:
                    rect(screen, BLACK, [x3, y3, a, b])
                    new_sqare()
                if click5(event)==1:
                    circle(screen, BLACK, (x5, y5), r5, 10)
                    new_ring()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
