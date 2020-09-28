import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 800))
line(screen, (50, 255, 255), [200, 0], [200, 780], 800)
line(screen, (50, 255, 0), [200, 380], [200, 800], 800)

image = pygame.image.load('horse2.png').convert_alpha()
new_image = pygame.transform.scale(image, (180, 235))
screen.blit(new_image, (450, 420))
image = pygame.image.load('horse1.png').convert_alpha()
new_image = pygame.transform.scale(image, (250, 300))
screen.blit(new_image, (190, 500))
image = pygame.image.load('horse3.png').convert_alpha()
new_image = pygame.transform.scale(image, (130, 170))
screen.blit(new_image, (280, 294))
image = pygame.image.load('horse5.png').convert_alpha()
new_image = pygame.transform.scale(image, (90, 115))
screen.blit(new_image, (450, 290))

k=1
while k<50:
    circle(screen, (50+k*4, 255, 255-5*k), (450, 125), 3*(50-k))
    k+=1
    
line(screen, (245, 220, 255), [180, 350], [180, 480], 25)
ellipse(screen, (0, 130, 0), [100, 40, 160, 160])
ellipse(screen, (50, 255, 0), [100, 40, 160, 160], 5)
ellipse(screen, (220, 180, 180), [180, 70, 60, 40])
ellipse(screen, (50, 255, 0), [180, 70, 60, 40], 5)
ellipse(screen, (0, 130, 0), [30, 120, 300, 160])
ellipse(screen, (50, 255, 0), [30, 120, 300, 160], 5)
ellipse(screen, (220, 180, 180), [230, 200, 60, 40])
ellipse(screen, (50, 255, 0), [230, 200, 60, 40], 5)
ellipse(screen, (220, 180, 180), [90, 170, 60, 40])
ellipse(screen, (50, 255, 0), [90, 170, 60, 40], 5)
ellipse(screen, (0, 130, 0), [0, 100, 120, 300])
ellipse(screen, (0, 255, 0), [0, 100, 120, 300], 5)
ellipse(screen, (220, 180, 180), [60, 155, 30, 60])
ellipse(screen, (50, 255, 0), [60, 155, 30, 60], 5)
ellipse(screen, (0, 130, 0), [90, 230, 180, 120])
ellipse(screen, (0, 255, 0), [90, 230, 180, 120], 5)
ellipse(screen, (0, 130, 0), [0, 300, 170, 150])
ellipse(screen, (0, 255, 0), [0, 300, 170, 150], 5)
ellipse(screen, (220, 180, 180), [100, 370, 30, 50])
ellipse(screen, (50, 255, 0), [100, 370, 30, 50], 5)
ellipse(screen, (0, 130, 0), [140, 300, 120, 90])
ellipse(screen, (0, 255, 0), [140, 300, 120, 90], 5)
line(screen, (245, 220, 255), [65, 470], [65, 580], 25)
ellipse(screen, (0, 130, 0), [0, 350, 120, 180])
ellipse(screen, (0, 255, 0), [0, 350, 120, 180], 5)
ellipse(screen, (220, 180, 180), [190, 330, 50, 30])
ellipse(screen, (50, 255, 0), [190, 330, 50, 30], 5)
ellipse(screen, (0, 130, 0), [110, 360, 180, 100])
ellipse(screen, (0, 255, 0), [110, 360, 180, 100], 5)
ellipse(screen, (220, 180, 180), [230, 395, 30, 30])
ellipse(screen, (50, 255, 0), [230, 395, 30, 30], 5)
line(screen, (245, 220, 255), [200, 500], [200, 600], 25)
ellipse(screen, (0, 130, 0), [120, 430, 160, 120])
ellipse(screen, (0, 255, 0), [120, 430, 160, 120], 5)
ellipse(screen, (220, 180, 180), [210, 490, 50, 25])
ellipse(screen, (50, 255, 0), [210, 490, 50, 25], 5)
ellipse(screen, (220, 180, 180), [20, 415, 30, 20])
ellipse(screen, (50, 255, 0), [20, 415, 30, 20], 5)
line(screen, (245, 220, 255), [110, 650], [110, 780], 25)
ellipse(screen, (0, 130, 0), [60, 500, 100, 100])
ellipse(screen, (0, 255, 0), [60, 500, 100, 100], 5)
ellipse(screen, (0, 130, 0), [30, 570, 150, 100])
ellipse(screen, (0, 255, 0), [30, 570, 150, 100], 5)
ellipse(screen, (0, 130, 0), [40, 640, 130, 90])
ellipse(screen, (0, 255, 0), [40, 640, 130, 90], 5)
ellipse(screen, (220, 180, 180), [130, 610, 40, 30])
ellipse(screen, (50, 255, 0), [130, 610, 40, 30], 5)
ellipse(screen, (220, 180, 180), [110, 520, 30, 34])
ellipse(screen, (50, 255, 0), [110, 520, 30, 34], 5)
ellipse(screen, (220, 180, 180), [120, 700, 25, 25])
ellipse(screen, (50, 255, 0), [120, 700, 25, 25], 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
