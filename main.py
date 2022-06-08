from constant import *
from math import *

import pygame
import sys

pygame.init()
pygame.display.set_caption("PyPool")
display = pygame.display.set_mode((WIDTH, OUTER_HEIGHT))
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y, speed, color, angle, ballNum):
        self.x = x + RADIUS
        self.y = y + RADIUS
        self.color = color
        self.angle = angle
        self.speed = speed
        self.ballNum = ballNum
        self.font = pygame.font.SysFont("Agency FB", 10)

    def draw(self, x, y):
        pygame.draw.ellipse(display, self.color, (x - RADIUS, y - RADIUS, RADIUS*2, RADIUS*2))
        if self.color == BLACK or self.ballNum == "cue":
            ballNo = self.font.render(str(self.ballNum), True, WHITE)
            display.blit(ballNo, (x - 5, y - 5))
        else:
            ballNo = self.font.render(str(self.ballNum), True, BLACK)
            if self.ballNum > 9:
                display.blit(ballNo, (x - 6, y - 5))
            else:
                display.blit(ballNo, (x - 5, y - 5))
                
    def move(self):
        self.speed -= FRICTION
        if self.speed <= 0:
            self.speed = 0
        self.x = self.x + self.speed*cos(radians(self.angle))
        self.y = self.y + self.speed*sin(radians(self.angle))

        if not (self.x < WIDTH - RADIUS - MARGIN):
            self.x = WIDTH - RADIUS - MARGIN
            self.angle = 180 - self.angle
        if not(RADIUS + MARGIN < self.x):
            self.x = RADIUS + MARGIN
            self.angle = 180 - self.angle
        if not (self.y < HEIGHT - RADIUS - MARGIN):
            self.y = HEIGHT - RADIUS - MARGIN
            self.angle = 360 - self.angle
        if not(RADIUS + MARGIN < self.y):
            self.y = RADIUS + MARGIN
            self.angle = 360 - self.angle 

class Holes:
    def __init__(self, x, y, color):
        self.r = MARGIN/2
        self.x = x + self.r + 10
        self.y = y + self.r + 10
        self.color = color

    # Draws the Pockets on Pygame Window
    def draw(self):
        pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

def border():
    pygame.draw.rect(display, BORDER_COLOR, (0, 0, WIDTH, 30))
    pygame.draw.rect(display, BORDER_COLOR, (0, 0, 30, HEIGHT))
    pygame.draw.rect(display, BORDER_COLOR, (WIDTH - 30, 0, WIDTH, HEIGHT))
    pygame.draw.rect(display, BORDER_COLOR, (0, HEIGHT - 30, WIDTH, HEIGHT))

# Cue Stick Class
class CueStick:
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color
        self.tangent = 0
    
    # Draws Cue Stick on Pygame Window
    def draw(self, cuex, cuey):
        self.x, self.y = pygame.mouse.get_pos()
        self.tangent = (degrees(atan2((cuey - self.y), (cuex - self.x))))
        pygame.draw.line(display, WHITE, (cuex + self.length*cos(radians(self.tangent)), cuey + self.length*sin(radians(self.tangent))), (cuex, cuey), 1)
        pygame.draw.line(display, self.color, (self.x, self.y), (cuex, cuey), 3)
    
    def applyForce(self, cueBall, force):
        cueBall.angle = self.tangent
        cueBall.speed = force
        
def collision(ball1, ball2):
    dist = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dist <= RADIUS*2:
        return True
    else:
        return False

def checkCueCollision(cueBall):
    for i in range(len(balls)):
        if collision(cueBall, balls[i]):
            if balls[i].x == cueBall.x:
                angleIncline = 2*90
            else:
                u1 = balls[i].speed
                u2 = cueBall.speed

                balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(cueBall.angle)))**2)**0.5
                cueBall.speed = ((u2*cos(radians(cueBall.angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                tangent = degrees((atan((balls[i].y - cueBall.y)/(balls[i].x - cueBall.x)))) + 90
                angle = tangent + 90

                balls[i].angle = (2*tangent - balls[i].angle)
                cueBall.angle = (2*tangent - cueBall.angle)

                balls[i].x += (balls[i].speed)*sin(radians(angle))
                balls[i].y -= (balls[i].speed)*cos(radians(angle))
                cueBall.x -= (cueBall.speed)*sin(radians(angle))
                cueBall.y += (cueBall.speed)*cos(radians(angle))

def checkCollision():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            if collision(balls[i], balls[j]):
                if balls[i].x == balls[j].x:
                    angleIncline = 2*90
                else:
                    u1 = balls[i].speed
                    u2 = balls[j].speed

                    balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(balls[j].angle)))**2)**0.5
                    balls[j].speed = ((u2*cos(radians(balls[j].angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                    tangent = degrees((atan((balls[i].y - balls[j].y)/(balls[i].x - balls[j].x)))) + 90
                    angle = tangent + 90

                    balls[i].angle = (2*tangent - balls[i].angle)
                    balls[j].angle = (2*tangent - balls[j].angle)

                    balls[i].x += (balls[i].speed)*sin(radians(angle))
                    balls[i].y -= (balls[i].speed)*cos(radians(angle))
                    balls[j].x -= (balls[j].speed)*sin(radians(angle))
                    balls[j].y += (balls[j].speed)*cos(radians(angle))
    
def initial_state():
    global balls
    balls = []

    s = 70

    b1 = Ball(s, HEIGHT/2 - 4*RADIUS, 0, colors[0], 0, 1)
    b2 = Ball(s + 2*RADIUS, HEIGHT/2 - 3*RADIUS, 0, colors[1], 0, 2)
    b3 = Ball(s, HEIGHT/2 - 2*RADIUS, 0, colors[2], 0, 3)
    b4 = Ball(s + 4*RADIUS, HEIGHT/2 - 2*RADIUS, 0, colors[3], 0, 4)
    b5 = Ball(s + 2*RADIUS, HEIGHT/2 - 1*RADIUS, 0, colors[4], 0, 5)
    b6 = Ball(s, HEIGHT/2, 0, colors[5], 0, 6)
    b7 = Ball(s + 6*RADIUS, HEIGHT/2 - 1*RADIUS, 0, colors[6], 0, 7)
    b8 = Ball(s + 4*RADIUS, HEIGHT/2, 0, colors[7], 0, 8)
    b9 = Ball(s + 8*RADIUS, HEIGHT/2, 0, colors[8], 0, 9)
    b10 = Ball(s + 6*RADIUS, HEIGHT/2 + 1*RADIUS, 0, colors[9], 0, 10)
    b11 = Ball(s + 2*RADIUS, HEIGHT/2 + 1*RADIUS, 0, colors[10], 0, 11)
    b12 = Ball(s, HEIGHT/2 + 2*RADIUS, 0, colors[11], 0, 12)
    b13 = Ball(s + 4*RADIUS, HEIGHT/2 + 2*RADIUS, 0, colors[12], 0, 13)
    b14 = Ball(s + 2*RADIUS, HEIGHT/2 + 3*RADIUS, 0, colors[13], 0, 14)
    b15 = Ball(s, HEIGHT/2 + 4*RADIUS, 0, colors[14], 0, 15)

    balls.append(b1)
    balls.append(b2)
    balls.append(b3)
    balls.append(b4)
    balls.append(b5)
    balls.append(b6)
    balls.append(b7)
    balls.append(b8)
    balls.append(b9)
    balls.append(b10)
    balls.append(b11)
    balls.append(b12)
    balls.append(b13)
    balls.append(b14)
    balls.append(b15)

def scoreBar():
    pygame.draw.rect(display, (51, 51, 51), (0, HEIGHT, WIDTH, OUTER_HEIGHT))

def close():
    pygame.quit()
    sys.exit()

# Main Function
def Table():
    loop = True
    initial_state()

    noHoles = 6
    holes = []

    h1 = Holes(0, 0, BLACK)
    h2 = Holes(WIDTH/2 - h1.r*2, 0, BLACK)
    h3 = Holes(WIDTH - h1.r - MARGIN - 5, 0, BLACK)
    h4 = Holes(0, HEIGHT - MARGIN - 5 - h1.r, BLACK)
    h5 = Holes(WIDTH/2 - h1.r*2, HEIGHT - MARGIN - 5 - h1.r, BLACK)
    h6 = Holes(WIDTH - h1.r - MARGIN - 5, HEIGHT - MARGIN - 5 - h1.r, BLACK)

    holes.append(h1)
    holes.append(h2)
    holes.append(h3)
    holes.append(h4)
    holes.append(h5)
    holes.append(h6)

    cueBall = Ball(WIDTH/2, HEIGHT/2, 0, WHITE, 0, "cue")
    cueStick = CueStick(0, 0, 100, STICK_COLOR)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_r:
                    Table()

        display.fill(BACK_COLOR)

        for i in range(len(balls)):
            balls[i].draw(balls[i].x, balls[i].y)

        cueBall.draw(cueBall.x, cueBall.y)

        if not (cueBall.speed > 0):

            cueStick.draw(cueBall.x, cueBall.y)
            
        border()
        
        for i in range(noHoles):
            holes[i].draw()
        
        scoreBar()
        pygame.display.update()

Table()
