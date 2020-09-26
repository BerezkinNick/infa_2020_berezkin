import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))
line(screen, (50, 255, 255), [200, 0], [200, 280], 800)
line(screen, (50, 255, 0), [200, 280], [200, 700], 800)
def tree(k, x, y):
    line(screen, (255, 240, 255), [110+x, 350+y], [110+x, 480+y], 30*k)
    ellipse(screen, (0, 130, 0), [40+x, 270+y, 140*k, 120*k])
    ellipse(screen, (0, 130, 0), [-10+x, 180+y, 250*k, 140*k])
    ellipse(screen, (0, 130, 0), [40+x, 100+y, 140*k, 160*k])
    ellipse(screen, (255, 200, 160), [110+x, 130+y, 44*k, 40*k])
    ellipse(screen, (255, 200, 160), [170+x, 240+y, 44*k, 40*k])
    ellipse(screen, (255, 200, 160), [-15+x, 230+y, 44*k, 40*k])
    ellipse(screen, (255, 200, 160), [120+x, 345+y, 40*k, 40*k])
tree(1, 0, 0)
circle(screen, (255, 220, 20), [580, 80], 110)

ellipse(screen, (220, 220, 255), [250, 600, 55, 20])
ellipse(screen, (255, 200, 255), [240, 590, 55, 20])
ellipse(screen, (255, 255, 200), [230, 610, 49, 10])
ellipse(screen, (220, 220, 255), [250, 620, 55, 20])
ellipse(screen, (255, 220, 255), [257, 615, 55, 20])
ellipse(screen, (255, 255, 200), [255, 575, 49, 10])
ellipse(screen, (255, 220, 200), [270, 610, 55, 20])
ellipse(screen, (255, 220, 200), [235, 575, 55, 20])
ellipse(screen, (220, 200, 255), [225, 580, 49, 10])
ellipse(screen, (255, 255, 220), [230, 620, 55, 15])
ellipse(screen, (220, 200, 255), [265, 590, 49, 16])
circle(screen, (200, 200, 100), [280, 540], 30)
ellipse(screen, (220, 200, 255), [275, 545, 50, 30])
ellipse(screen, (220, 255, 255), [235, 555, 50, 30])
ellipse(screen, (255, 200, 255), [225, 545, 55, 20])
ellipse(screen, (255, 200, 200), [240, 525, 55, 30])
ellipse(screen, (255, 255, 255), [280, 480, 200, 100])
line(screen, (255, 255, 255), [300, 525], [300, 645], 20)
line(screen, (255, 255, 255), [335, 525], [335, 630], 15)
line(screen, (255, 255, 255), [425, 400], [425, 525], 60)
line(screen, (255, 255, 255), [405, 525], [405, 645], 20)
line(screen, (255, 255, 255), [440, 525], [440, 630], 15)

ellipse(screen, (255, 255, 255), [400, 390, 80, 50])
ellipse(screen, (255, 255, 255), [420, 405, 90, 35])

ellipse(screen, (220, 220, 255), [370, 410, 55, 20])
ellipse(screen, (255, 200, 255), [360, 425, 55, 20])
ellipse(screen, (255, 255, 200), [370, 445, 49, 10])
ellipse(screen, (220, 220, 255), [365, 465, 55, 20])
ellipse(screen, (255, 220, 255), [375, 455, 55, 20])
ellipse(screen, (255, 255, 200), [380, 470, 49, 10])

ellipse(screen, (220, 200, 255), [370, 420, 55, 20])
ellipse(screen, (255, 200, 255), [360, 435, 55, 20])
ellipse(screen, (255, 255, 200), [370, 449, 49, 10])
ellipse(screen, (220, 200, 255), [365, 479, 55, 20])
ellipse(screen, (255, 220, 255), [375, 435, 55, 20])
ellipse(screen, (255, 255, 200), [380, 467, 49, 10])

ellipse(screen, (255, 200, 220), [350, 420, 60, 25])
ellipse(screen, (255, 200, 255), [330, 435, 55, 20])
ellipse(screen, (200, 200, 255), [340, 449, 59, 15])
ellipse(screen, (220, 230, 255), [345, 479, 60, 20])
ellipse(screen, (220, 230, 200), [325, 452, 60, 20])
ellipse(screen, (230, 250, 200), [335, 472, 50, 20])
ellipse(screen, (250, 240, 200), [320, 467, 65, 20])

ellipse(screen, (225, 200, 190), [400, 380, 45, 20])
ellipse(screen, (245, 220, 200), [385, 390, 35, 25])
polygon(screen, (225, 200, 190), [[430, 390],[460, 395], [450, 310]])

ellipse(screen, (205, 50, 255), [438, 400, 20, 17])
ellipse(screen, (0, 0, 0), [445, 405, 8, 8])
ellipse(screen, (0, 0, 0), [445, 405, 8, 8])
ellipse(screen, (255, 255, 255), [442, 403, 10, 4])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
