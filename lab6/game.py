import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''Рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    global x1, y1, r1
    x1 = randint(100, 1100)
    y1 = randint(100, 900)
    r1 = randint(10, 100)
    color1 = COLORS[randint(0, 5)]
    circle(screen, color1, (x1, y1), r1)
    global x2, y2, r2
    x2 = randint(100, 1100)
    y2 = randint(100, 900)
    r2 = randint(10, 100)
    color2 = COLORS[randint(0, 5)]
    circle(screen, color2, (x2, y2), r2)
        
       
def score(pos):
        if (pos[0] - x)**2 + (pos[1] - y)**2 <= r**2 or (pos[0] - x1)**2 + (pos[1] - y1)**2 <= r1**2 or (pos[0] - x2)**2 + (pos[1] - y2)**2 <= r2**2:
            return 1
        else:
            return 0
points = 0
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            if score(event.pos) == 1:
                points += 1
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
print('Сумма очков:', points)
pygame.quit()


# In[ ]:
