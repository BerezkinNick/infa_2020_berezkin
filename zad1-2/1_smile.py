from pygame import *
from pygame.draw import *
init()
FPS = 30
screen = display.set_mode((400, 400))
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
polygon(screen, BLACK, [[200, 175], [220, 175], [200, 200]])
screen.fill(GREY)
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 2)
circle(screen, (255, 0, 0), (140, 120), 30)
circle(screen, (255, 0, 0), (260, 120), 30)
circle(screen, (0, 0, 0), (140, 120), 10)
circle(screen, (0, 0, 0), (260, 120), 10)
line(screen, (0,0,0),(120, 250), (280, 250), 30)
polygon(screen, (0, 0, 0), [(70,40), (70,60),
                               (170,100), (170,80)])
polygon(screen, (0, 0, 0), [(350,40), (350,60),
                               (230,100), (230,80)])

display.update()
clock = time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in event.get():
        if type == QUIT:
            finished = True

quit()
