import pygame
from pygame.draw import *

pygame.init()

FPS = 30
k=220
m=310
screen = pygame.display.set_mode((510-k, 650-m))
surf = pygame.Surface((510-k, 650-m))
surf.fill((50, 255, 0))
line(surf, (50, 255, 255), [0, 80], [300, 80], 180)
ellipse(surf, (220, 220, 255), [250-k, 600-m, 55, 20])
ellipse(surf, (255, 200, 255), [240-k, 590-m, 55, 20])
ellipse(surf, (255, 255, 200), [230-k, 610-m, 49, 10])
ellipse(surf, (220, 220, 255), [250-k, 620-m, 55, 20])
ellipse(surf, (255, 220, 255), [257-k, 615-m, 55, 20])
ellipse(surf, (255, 255, 200), [255-k, 575-m, 49, 10])
ellipse(surf, (255, 220, 200), [270-k, 610-m, 55, 20])
ellipse(surf, (255, 220, 200), [235-k, 575-m, 55, 20])
ellipse(surf, (220, 200, 255), [225-k, 580-m, 49, 10])
ellipse(surf, (255, 255, 220), [230-k, 620-m, 55, 15])
ellipse(surf, (220, 200, 255), [265-k, 590-m, 49, 16])
circle(surf, (200, 200, 100), [280-k, 540-m], 30)
ellipse(surf, (220, 200, 255), [275-k, 545-m, 50, 30])
ellipse(surf, (220, 255, 255), [235-k, 555-m, 50, 30])
ellipse(surf, (255, 200, 255), [225-k, 545-m, 55, 20])
ellipse(surf, (255, 200, 200), [240-k, 525-m, 55, 30])
ellipse(surf, (255, 255, 255), [280-k, 480-m, 200, 100])
line(surf, (255, 255, 255), [300-k, 525-m], [300-k, 645-m], 20)
line(surf, (255, 255, 255), [335-k, 525-m], [335-k, 630-m], 15)
line(surf, (255, 255, 255), [425-k, 400-m], [425-k, 525-m], 60)
line(surf, (255, 255, 255), [405-k, 525-m], [405-k, 645-m], 20)
line(surf, (255, 255, 255), [440-k, 525-m], [440-k, 630-m], 15)

ellipse(surf, (255, 255, 255), [400-k, 390-m, 80, 50])
ellipse(surf, (255, 255, 255), [420-k, 405-m, 90, 35])

ellipse(surf, (220, 220, 255), [370-k, 410-m, 55, 20])
ellipse(surf, (255, 200, 255), [360-k, 425-m, 55, 20])
ellipse(surf, (255, 255, 200), [370-k, 445-m, 49, 10])
ellipse(surf, (220, 220, 255), [365-k, 465-m, 55, 20])
ellipse(surf, (255, 220, 255), [375-k, 455-m, 55, 20])
ellipse(surf, (255, 255, 200), [380-k, 470-m, 49, 10])

ellipse(surf, (220, 200, 255), [370-k, 420-m, 55, 20])
ellipse(surf, (255, 200, 255), [360-k, 435-m, 55, 20])
ellipse(surf, (255, 255, 200), [370-k, 449-m, 49, 10])
ellipse(surf, (220, 200, 255), [365-k, 479-m, 55, 20])
ellipse(surf, (255, 220, 255), [375-k, 435-m, 55, 20])
ellipse(surf, (255, 255, 200), [380-k, 467-m, 49, 10])

ellipse(surf, (255, 200, 220), [350-k, 420-m, 60, 25])
ellipse(surf, (255, 200, 255), [330-k, 435-m, 55, 20])
ellipse(surf, (200, 200, 255), [340-k, 449-m, 59, 15])
ellipse(surf, (220, 230, 255), [345-k, 479-m, 60, 20])
ellipse(surf, (220, 230, 200), [325-k, 452-m, 60, 20])
ellipse(surf, (230, 250, 200), [335-k, 472-m, 50, 20])
ellipse(surf, (250, 240, 200), [320-k, 467-m, 65, 20])

ellipse(surf, (225, 200, 190), [400-k, 380-m, 45, 20])
ellipse(surf, (245, 220, 200), [385-k, 390-m, 35, 25])
polygon(surf, (225, 200, 190), [[430-k, 390-m],[460-k, 395-m], [450-k, 310-m]])

ellipse(surf, (205, 50, 255), [438-k, 400-m, 20, 17])
ellipse(surf, (0, 0, 0), [445-k, 405-m, 8, 8])
ellipse(surf, (0, 0, 0), [445-k, 405-m, 8, 8])
ellipse(surf, (255, 255, 255), [442-k, 403-m, 10, 4])
pygame.image.save(surf,'horse3.PNG')
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
