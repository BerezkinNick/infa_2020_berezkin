import pygame as pg
import numpy as np
from random import randint, gauss
pg.init()
pg.font.init()


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

SCREEN_SIZE = (800, 600)


class GameObject:
    pass

class Ball(GameObject):

    def __init__(self, coord, v, r=20):
        self.coord = coord
        self.v = v
        self.color = COLORS[randint(0, 5)]
        self.rad = rad
        self.is_alive = True


    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    
    def move(self, time=2):
        self.v[1] += 10
        for i in range(2):
            self.coord[i] += time * self.v[i]
        self.walls()
        if self.v[0]**2 + self.v[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False


    def walls(self):
        for i in range(2):
            if self.coord[i] < self.r:
                self.coord[i] = self.r
                self.v[i] = -int(self.v[i] * 0.8)
                self.v[1-i] = int(self.v[1-i] * 0.9)
            elif self.coord[i] > SCREEN_SIZE[i] - self.r:
                self.coord[i] = SCREEN_SIZE[i] - self.r
                self.v[i] = -int(self.v[i] * 0.8)
                self.v[1-i] = int(self.v[1-i] * 0.9)

class Cannon(GameObject):

    
    def __init__(self, coord=[0, SCREEN_SIZE[1]//2], angle=0, max_power=50, min_power=10, color=RED):
        self.coord = coord
        self.angle = angle
        self.max_power = max_power
        self.min_power = min_power
        self.color = color
        self.active = False
        self.power = min_power
    
    def get_gain(self):
        self.gain = True

    def shot_power(self):
        if self.gain:
            self.power += 1

    def strike(self):

        v = 2*self.power
        angle = self.angle
        ball = Shell(list(self.coord), [int(v * np.cos(angle)), int(v * np.sin(angle))])
        self.power = self.min_power
        self.gain = False
        return ball
        
    def set_angle(self, target_pos):

        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])

    def move(self, inc):

        if (self.coord[1] > 30 or inc > 0) and (self.coord[1] < SCREEN_SIZE[1] - 30 or inc < 0):
            self.coord[1] += inc

    def draw(self, screen):

        gun_shape = []
        vec_1 = np.array([int(5 * np.cos(self.angle - np.pi/2)), int(5 * np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)

        
class Target(GameObject):

    def __init__(self, coord=None, rad=30):

        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad


        self.color = COLORS[randint(0, 5)]
        

    def check_collision(self, ball):
        
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist

    def draw(self, screen):

        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self):

        pass

class Shell(GameObject):

    def __init__(self, coord, v, rad=20, color=None):
 
        self.coord = coord
        self.v = v
        self.color = COLORS[randint(0, 5)]
        self.rad = rad
        self.is_alive = True

    def check_corners(self, refl_ort=0.8, refl_par=0.9):
        
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.v[i] = -int(self.v[i] * refl_ort)
                self.v[1-i] = int(self.v[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.v[i] = -int(self.v[i] * refl_ort)
                self.v[1-i] = int(self.v[1-i] * refl_par)

    def move(self, time=1, grav=0):
        
        self.v[1] += grav
        for i in range(2):
            self.coord[i] += time * self.v[i]
        self.check_corners()
        if self.v[0]**2 + self.v[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        
class MovingTarget(Target):
    def __init__(self, coord=None, rad=30):
        super().__init__(coord, rad)
        self.vx = randint(-2, +2)
        self.vy = randint(-2, +2)

    def move(self):
        self.coord[0] += self.vx
        self.coord[1] += self.vy

class ScoreTable:

    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("d", 25)

    def score(self):

        return self.t_destr - self.b_used

    def draw(self, screen):
        score_surf = []
        score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr), True, WHITE))
        score_surf.append(self.font.render("Balls used: {}".format(self.b_used), True, WHITE))



class Manager:

    def __init__(self, n_targets=1):
        self.balls = []
        self.gun = Cannon()
        self.targets = []
        self.score_t = ScoreTable()
        self.n_targets = n_targets
        self.new_mission()

        
    def new_mission(self):

        for i in range(self.n_targets):
            self.targets.append(Target(rad=randint(max(1, 30 - 2*max(0, self.score_t.score())),
                30 - max(0, self.score_t.score()))))
        for i in range(self.n_targets):
            self.targets.append(MovingTarget(rad=randint(max(1, 30 - 2 * max(0, self.score_t.score())),
                                                     30 - max(0, self.score_t.score()))))




    def process(self, events, screen):

        done = self.handle_events(events)

        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        
        self.move()
        self.collide()
        self.draw(screen)

        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()

        return done

    def handle_events(self, events):

        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.move(-5)
                elif event.key == pg.K_DOWN:
                    self.gun.move(5)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.get_gain()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
                    self.score_t.b_used += 1
        return done

    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)
        self.gun.draw(screen)
        self.score_t.draw(screen)

    def move(self):

        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move()
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        for i, target in enumerate(self.targets):
            target.move()
        self.gun.get_gain()

    def collide(self):

        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for j in reversed(targets_c):
            self.score_t.t_destr += 1
            self.targets.pop(j)


screen = pg.display.set_mode(SCREEN_SIZE)

done = False
clock = pg.time.Clock()

mgr = Manager(n_targets=3)

while not done:
    clock.tick(15)
    screen.fill(BLACK)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()




            

