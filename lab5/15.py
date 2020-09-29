from pygame import *
from math import *
from pygame.draw import *

init()

FPS=30
screen = display.set_mode((840, 1080))

#Используемые цвета:
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
WATER=(0, 102, 128) #цвет воды
FISH=(71, 136, 147) #цвет тела рыбы
EYE=(0, 53, 189)    #цвет глаза рыбы
GREY=(102, 99, 112) #цвет плавников


SKYBLUE=(33, 33, 120)
SKYFIOL=(141, 95, 211)
SKYPINK=(205, 135, 222)     #Цвета неба
SKYLILAC=(222, 135, 170)
SKYORANGE=(255, 153, 85)

#Фон:
rect(screen, WATER, (0, 0, 840, 1080))      #вода
rect(screen, SKYBLUE, (0, 0, 840, 110))
rect(screen, SKYFIOL, (0, 110, 840, 57))
rect(screen, SKYPINK, (0, 167, 840, 97))    #небо
rect(screen, SKYLILAC, (0, 264, 840, 138))
rect(screen, SKYORANGE, (0, 402, 840, 118))


def chaika(angle, scale):
    '''
    Функция рисует чайку.
    surface - объект pygame.Surface
    angle - угол поворота поверхности
    scale - масштаб поверхности
    '''
    surface = Surface((340, 1000), SRCALPHA)
    # Крылья:
    arc(surface, WHITE, (10, 100, 180, 120), pi / 10, 3 * pi / 4, 3)
    arc(surface, WHITE, (180, 100, 180, 120), pi / 4, 9 * pi / 10, 3)
    # Поворот и масштабирование поверхности:
    surface = transform.rotozoom(surface, angle, scale)
    rect = surface.get_rect()
    screen.blit(surface, rect)

def fish(scale): 
    '''
    Функция рисует рыбу.
    surface - объект pygame.Surface
    angle - угол поворота поверхности
    scale - масштаб поверхности
    '''
    surface = Surface((840, 1080), SRCALPHA)
    # Тело:
    ellipse(surface, FISH, (500, 759, 180, 60))             
    arc(surface, BLACK, (500, 759, 180, 60), 0, 2 * pi, 1)
    # Глаз:
    circle(surface, EYE, (655, 789), 12)                    
    circle(surface, BLACK, (657, 790), 5)
    # Хвост:
    polygon(surface, FISH, [(509, 789), (470, 819), (470, 759), (509, 789)])
    polygon(surface, BLACK, [(509, 789), (470, 819), (470, 759), (509, 789)], 1)
    # Верхний плавник:
    polygon(surface, GREY, [(515, 740), (595, 740), (615, 760), (555, 760), (515, 740)])
    polygon(surface, BLACK, [(515, 740), (595, 740), (615, 760), (555, 760), (515, 740)], 1)
    # Нижние плавники:
    polygon(surface, GREY, [(515, 835), (545, 835), (550, 814), (530, 810), (515, 835)])
    polygon(surface, BLACK, [(515, 835), (545, 835), (550, 814), (530, 810), (515, 835)], 1)
    
    polygon(surface, GREY, [(595, 839), (630, 834), (615, 816), (600, 816), (595, 839)])
    polygon(surface, BLACK, [(595, 839), (630, 834), (615, 816), (600, 816), (595, 839)], 1)
    # Масштабирование поверхности:
    surface = transform.rotozoom(surface, 0, scale)
    rect = surface.get_rect()
    screen.blit(surface, rect)

def ytka(scale):
    '''
    Функция рисует утку.
    surface - объект pygame.Surface
    angle - угол поворота поверхности
    scale - масштаб поверхности
    '''
    surface = Surface((840, 1080), SRCALPHA)
    # Задняя лапа
    polygon(surface, (255, 255, 255), [(340, 530), (370, 610), (395, 600), (385, 500), (340, 530)])
    polygon(surface, (255, 255, 255), [(370, 610), (420, 620), (425, 610), (390, 599), (370, 610)])
    polygon(surface, (255, 211, 85), [(445, 615), (465, 620), (445, 625), (445, 640), (435, 630), (435, 640), (425, 620), (415, 630), (425, 610), (445, 615)])
    polygon(surface, (0, 0, 0), [(445, 615), (465, 620), (445, 625), (445, 640), (435, 630), (435, 640), (425, 620), (415, 630), (425, 610), (445, 615)], 1)
    # Заднее крыло
    polygon(surface, (255, 255, 255), [(390, 460), (380, 420), (350, 390), (140, 340), (105, 330), (130, 360), (145, 370), (160, 380), (190, 390), (240, 405), (270, 420), (280, 480), (390, 460)])
    polygon(surface, (0, 0, 0), [(390, 460), (380, 420), (350, 390), (140, 340), (105, 330), (130, 360), (145, 370), (160, 380), (190, 390), (240, 405), (270, 420), (280, 480), (390, 460)], 1)
    # Тело
    ellipse(surface, (255, 255, 255), (200, 450, 250, 125))
    ellipse(surface, (255, 255, 255), (400, 465, 130, 50))
    # Голова
    ellipse(surface, (255, 255, 255), (500, 450, 85, 60))
    ellipse(surface, (0, 0, 0), (557, 470, 15, 9))
    # Клюв
    polygon(surface, (255, 221, 85), [(580, 477), (580, 472), (630, 463), (645, 477), (580, 477)])
    polygon(surface, (255, 221, 85), [(580, 477), (580, 482), (630, 491), (645, 477), (580, 477)])
    polygon(surface, (0, 0, 0), [(580, 477), (580, 472), (630, 463), (645, 477), (580, 477)], 1)
    polygon(surface, (0, 0, 0), [(580, 477), (580, 482), (630, 491), (645, 477), (580, 477)], 1)
    # Передняя лапа
    polygon(surface, (255, 255, 255), [(290, 550), (320, 630), (355, 620), (345, 520), (290, 550)])
    polygon(surface, (255, 255, 255), [(320, 630), (390, 640), (395, 630), (350, 615), (320, 630)])
    polygon(surface, (255, 211, 85), [(415, 635), (435, 640), (415, 645), (415, 660), (405, 650), (405, 660), (395, 640), (385, 650), (395, 630), (415, 635)])
    polygon(surface, (0, 0, 0), [(415, 635), (435, 640), (415, 645), (415, 660), (405, 650), (405, 660), (395, 640), (385, 650), (395, 630), (415, 635)], 1)
    # Хвост
    polygon(surface, (255, 255, 255), [(230, 540), (205, 539), (170, 530), (180, 440), (215, 480), (240, 500), (230, 540)])
    polygon(surface, (0, 0, 0), [(230, 540), (205, 539), (170, 530), (180, 440), (215, 480), (240, 500), (230, 540)], 1)
    # Переднее крыло
    polygon(surface, (255, 255, 255), [(380, 500), (370, 460), (340, 430), (130, 400), (95, 390), (120, 420), (135, 430), (150, 440), (180, 450), (230, 465), (260, 480), (270, 520), (380, 500)])
    polygon(surface, (0, 0, 0), [(380, 500), (370, 460), (340, 430), (130, 400), (95, 390), (120, 420), (135, 430), (150, 440), (180, 450), (230, 465), (260, 480), (270, 520), (380, 500)], 1)
    # Масштабирование поверхности:
    surface = transform.rotozoom(surface, 0, scale)
    rect = surface.get_rect()
    screen.blit(surface, rect)

fish(1)
fish(0.8)
chaika(0, 1)
chaika(10, 0.5)
chaika(-30, 1)
chaika(-25, 0.8)
ytka(360, 0.4)
ytka(0, 0.9)





display.update()
clock = time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in event.get():
        if event.type == QUIT:
            finished = True
quit()
