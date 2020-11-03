import pygame
from pygame.draw import *
from random import randint, choice
import math
from pygame.mixer import *
pygame.init()

FPS = 30
SCREEN_SIZE=(1000, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (100, 60, 20)
ORANGE = (255, 100, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Game_Pushka:
    pass

class ball(Game_Pushka):
    ''' Класс пули '''
    
    def __init__(self, vx, vy):
        ''' Конструктор класса пули '''
        
        self.x = 40
        self.y = 450
        self.r = 15
        self.vx = vx
        self.vy = vy
        self.color = COLORS[randint(0, 5)]
        self.livetime = FPS*3

    def move(self, grav=2, refl_ort=0.8, refl_par=0.9):
        ''' Перемещение пули '''
        self.x += self.vx
        self.y -= self.vy
        if self.x < (0 + self.r):
            self.vx = - self.vx
            self.x = (0 + self.r)
            self.vx = int(self.vx*refl_ort)
            self.vy = int(self.vy*refl_par)
        if self.x > (1000 - self.r):
            self.vx = - self.vx
            self.x = (1000 - self.r)
            self.vx = int(self.vx*refl_ort)
            self.vy = int(self.vy*refl_par)
        if self.y < (0 + self.r):
            self.vy = - self.vy
            self.y = (0 + self.r)
            self.vx = int(self.vx*refl_ort)
            self.vy = int(self.vy*refl_par)
        if self.y > (600 - self.r):
            self.vy = - self.vy
            self.y = (600 - self.r)
            self.vx = int(self.vx*refl_ort)
            self.vy = int(self.vy*refl_par)
        self.vy -= grav
        self.livetime -= 1
        if self.livetime > 0:
            circle(screen, self.color, (self.x, self.y), self.r)
            circle(screen, BLACK, (self.x, self.y), self.r, 2)

    def check_collisions(self, obj):
        ''' Регистрация столкновений пули с целями '''
        return (obj.x - self.x)*(obj.x - self.x)+\
                    (obj.y - self.y)*(obj.y - self.y) <\
                    (obj.r + self.r)*(obj.r + self.r)


class gun(Game_Pushka):
    def __init__(self):
        """ Конструктор класса пушки """
        self.gun_power = 10
        self.active = False
        self.an = 1
    
    def activate(self):
        """Активация пушки"""
        self.active = True

    def strike(self, event, balls, bullet):
        bullet += 1
        self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 40))
        new_ball = ball(int(self.gun_power * math.cos(self.an)), - int(self.gun_power * math.sin(self.an)))
        balls.append(new_ball)
        self.active = False
        self.gun_power = 10
        return balls, bullet

    def targetting(self, mouse):
        """ Функция прицеливания """
        self.an = math.atan((mouse.get_pos()[1]-450) / (mouse.get_pos()[0]-20))
        line (screen, RED, (20, 450),
                    (20 + int(max(self.gun_power, 20) * math.cos(self.an)),
                    450 + int(max(self.gun_power, 20) * math.sin(self.an))),
                    7)
    def regulate_power(self, max_power=100):
        if self.active and self.gun_power < max_power:
                self.gun_power += 1


class target(Game_Pushka):
    def __init__(self):
        self.score = 0
        self.livetime = 1
        x=self.x = randint(600, 880)
        y=self.y = randint(100, 400)
        r=self.r = randint(20, 60)
        self.vx = randint(-30, 30)
        self.vy = randint(-30, 30)
        color=self.color = COLORS[randint(0, 5)]

    def move_targets(self):
        self.x += self.vx
        self.y -= self.vy
        if self.x < (0 + self.r):
            k=randint(1, 20)
            self.vx = - int(k*self.vx/10)
            self.x = (0 + self.r)
        if self.x > (1000 - self.r):
            k=randint(1, 20)
            self.vx = - int(k*self.vx/10)
            self.x = (1000 - self.r)
        if self.y < (0 + self.r):
            k=randint(1, 20)
            self.vy = - int(k*self.vy/10)
            self.y = (0 + self.r)
        if self.y > (600 - self.r):
            k=randint(1, 20)
            self.vy = - int(k*self.vy/10)
            self.y = (600 - self.r)
        if self.livetime == 1:
            circle(screen, self.color, (self.x, self.y), self.r)
            circle(screen, BLACK, (self.x, self.y), self.r, 1)
   
    def shooting(self, score=1):
        """Попадание шарика в цель."""
        self.x = randint(600, 780) 
        self.y = randint(300, 550)
        self.r = randint(20, 50)
        self.score += score

music.load('music.mp3')
music.play()
gun = gun()
targ1 = target()
targ2 = target()
targ3 = target()
targ4 = target()
targ5 = target()
bullet = 0
balls = []
pygame.display.update()
clock = pygame.time.Clock()
finished = False

background='background.jpg'

def restart_game():
    bullet = 0
    balls = []
    targ1.livetime = 1
    targ2.livetime = 1
    targ3.livetime = 1
    targ4.livetime = 1
    targ5.livetime = 1
    while targ1.livetime or targ2.livetime or targ3.livetime or targ4.livetime or targ5.livetime:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.activate()
            if event.type == pygame.MOUSEBUTTONUP:
                balls, bullet = gun.strike(event, balls, bullet)
        for ball in balls:
            ball.move()
            for targ in [targ1, targ2, targ3, targ4, targ5]:
                if ball.check_collisions(targ) and targ.livetime:
                    targ.livetime = 0
                    targ.shooting()
        clock.tick(FPS)
        pygame.display.update()
        background_surface = pygame.image.load(background)
        background_surface = pygame.transform.scale(background_surface, SCREEN_SIZE)
        background_rect = background_surface.get_rect(topleft = (0, 0))
        screen.blit(background_surface, background_rect)
        targ1.move_targets()
        targ2.move_targets()
        targ3.move_targets()
        targ4.move_targets()
        targ5.move_targets()
        screen.blit(pygame.font.Font(None, 40).render('Целей уничтожено:', 1, BLACK), (20, 20))
        screen.blit(pygame.font.Font(None, 40).render(str(targ1.score+targ2.score+targ3.score+targ4.score+targ5.score), 1, BLACK), (300, 20))
        pygame.display.set_caption(str(targ1.score+targ2.score+targ3.score+targ4.score+targ5.score))
        gun.regulate_power()
        gun.targetting(pygame.mouse)

    screen.fill(WHITE)
    clock.tick(FPS)

    
while not finished:
    finished = restart_game()

pygame.quit()

