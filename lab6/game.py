import pygame
from pygame.draw import *
from math import *
from random import *
pygame.init()

#Размеры окна:
width = 900
height = 780

FPS = 30
screen = pygame.display.set_mode((width, height))

#Цвета объектов:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0

print('За попадание по шарику начисляется 1 очко\nЗа попадание по квадрату - 2 очка\nЗа попадание по кольцу - 4 очка')
print('Введите имя игрока')
name=input()


def new_ball():
    ''' Функция рисует первый шарик со случайными значениями
        координат центра, радиуса и скорости перемещения '''
    global x, y, r, v, angle, color
    x = randint(100, width - 100)
    y = randint(100, height - 100)
    r = randint(20, 100)
    v = randint(50, 500)
    angle = radians(randint(0, 360))
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def new_ball2():
    ''' Функция рисует второй шарик со случайными значениями
        координат центра, радиуса и скорости перемещения '''
    global x2, y2, r2, v2, angle2, color2
    x2 = randint(100, width - 100)
    y2 = randint(100, height - 100)
    r2 = randint(20, 100)
    v2 = randint(50, 500)
    angle2 = radians(randint(0, 360))
    color2 = COLORS[randint(0, 5)]
    circle(screen, color2, (x2, y2), r2)

  
def new_sqare():
    ''' Функция рисует квадрат со случайными значениями
        координат левого верхнего угла, длины стороны и скорости перемещения '''
    global x3, y3, a, b, v3, angle3, color3
    a=randint(50, 120)
    b=a
    x3 = randint(0, width-a)
    y3 = randint(0, height-a)
    v3 = randint(400, 500)
    angle3 = radians(randint(0, 360))
    color3 = COLORS[randint(0, 5)]
    rect(screen, color3, [x3, y3, a, b])


def new_ring():
    ''' Функция рисует кольцо шириной 10со случайными значениями
        координат центра, радиуса и скорости перемещения  '''
    global x4, y4, r4, v4, angle4, color4
    x4 = randint(100, width - 100)
    y4 = randint(100, height - 100)
    r4 = randint(20, 100)
    v4 = randint(50, 500)
    angle4 = radians(randint(0, 360))
    color4 = COLORS[randint(0, 5)]
    circle(screen, color4, (x4, y4), r4, 10)
    
    
def move_object():
    '''Функция перемещает объекты'''
    global x, y, r, v, angle, color, x2, y2, r2, v2, angle2, color2, x3, y3, a, b, v3, angle3, color3, x4, y4, r4, v4, angle4, color4
    screen.fill(BLACK)
    x += round(v / FPS * cos(angle))
    y -= round(v / FPS * sin(angle))
    x2 += round(v2 / FPS * cos(angle2))
    y2 -= round(v2 / FPS * sin(angle2))
    x3 += round(v3 / FPS * cos(angle3))
    y3 -= round(v3 / FPS * sin(angle3))
    x4 += round(v4 / FPS * cos(angle4))
    y4 -= round(v4 / FPS * sin(angle4))
    circle(screen, color, (x, y), r)
    circle(screen, color2, (x2, y2), r2)
    rect(screen, color3, [x3, y3, a, b])
    circle(screen, color4, (x4, y4), r4, 10)
    pygame.display.update()
    wall()
    wall2()
    wall3()
    wall4()

    

#Функции, меняющие направление движения объектов при столкновении со стенкой:
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
    global x4, y4, r4, angle4
    if x4 + r4 > width:
        angle4 = pi - angle4
    if x4 - r4 < 0:
        angle4 = pi - angle4
    if y4 + r4 > height:
        angle4 = 2 * pi - angle4
    if y4 - r4 < 0:
        angle4 = 2 * pi - angle4

        

#Функции, регистрирующие попадания в объекты щелчком мыши:
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
    if x3 + a > event.pos[0] and event.pos[0] > x3 and y3 + a > event.pos[1] and event.pos[1] > y3:
        score += 2
        print(score)
        return 1
    
def click4(event):
    global score
    if (x4 - event.pos[0]) ** 2 + (y4 - event.pos[1]) ** 2 <= r4 ** 2 and (x4 - event.pos[0]) ** 2 + (y4 - event.pos[1]) ** 2 >= (r4 - 10) ** 2:
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
    flag = True
    while flag:
        clock.tick(FPS)
        move_object()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                flag = False
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
                if click4(event)==1:
                    circle(screen, BLACK, (x4, y4), r4, 10)
                    new_ring()

    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()

#Вывод очков, набранных игроками, в файл:
file = open('RESULTS.txt', 'r')
for line in file:
    Game_Result = line.split()[-1]
    print(Game_Result)
    if score >= int(Game_Result):
        name_line = line + name + '        ' + str(score)
        file = open('RESULTS.txt', 'a')
        file.write(name_line + "\n")
        file.close()
        break
print('Сумма очков:', score)




