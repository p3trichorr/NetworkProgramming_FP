from constant import *
from math import *

import pygame
import sys

pygame.display.set_caption("PyPool")
display = pygame.display.set_mode((WIDTH, OUTER_HEIGHT))

class Ball:
    def __init__(self, x, y, speed, color, angle, ballNum):
        self.x = x + RADIUS
        self.y = y + RADIUS
        self.color = color
        self.angle = angle
        self.speed = speed
        self.ballNum = ballNum

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

def initial_state():
    global BALLS
    BALLS = []

    s = 70

    b1 = Ball(s, HEIGHT/2 - 4*RADIUS, 0, BLACK, 0, 1)
    b2 = Ball(s + 2*RADIUS, HEIGHT/2 - 3*RADIUS, 0, WHITE, 0, 2)
    b3 = Ball(s, HEIGHT/2 - 2*RADIUS, 0, BLACK, 0, 3)
    b4 = Ball(s + 4*RADIUS, HEIGHT/2 - 2*RADIUS, 0, WHITE, 0, 4)
    b5 = Ball(s + 2*RADIUS, HEIGHT/2 - 1*RADIUS, 0, BLACK, 0, 5)
    b6 = Ball(s, HEIGHT/2, 0, WHITE, 0, 6)
    b7 = Ball(s + 6*RADIUS, HEIGHT/2 - 1*RADIUS, 0, BLACK, 0, 7)
    b8 = Ball(s + 4*RADIUS, HEIGHT/2, 0, WHITE, 0, 8)
    b9 = Ball(s + 8*RADIUS, HEIGHT/2, 0, BLACK, 0, 9)
    b10 = Ball(s + 6*RADIUS, HEIGHT/2 + 1*RADIUS, 0, WHITE, 0, 10)
    b11 = Ball(s + 2*RADIUS, HEIGHT/2 + 1*RADIUS, 0, BLACK, 0, 11)
    b12 = Ball(s, HEIGHT/2 + 2*RADIUS, 0, WHITE, 0, 12)
    b13 = Ball(s + 4*RADIUS, HEIGHT/2 + 2*RADIUS, 0, BLACK, 0, 13)
    b14 = Ball(s + 2*RADIUS, HEIGHT/2 + 3*RADIUS, 0, WHITE, 0, 14)
    b15 = Ball(s, HEIGHT/2 + 4*RADIUS, 0, BLACK, 0, 15)

    BALLS.append(b1)
    BALLS.append(b2)
    BALLS.append(b3)
    BALLS.append(b4)
    BALLS.append(b5)
    BALLS.append(b6)
    BALLS.append(b7)
    BALLS.append(b8)
    BALLS.append(b9)
    BALLS.append(b10)
    BALLS.append(b11)
    BALLS.append(b12)
    BALLS.append(b13)
    BALLS.append(b14)
    BALLS.append(b15)

def scoreBar():
    pygame.draw.rect(display, (51, 51, 51), (0, HEIGHT, WIDTH, OUTER_HEIGHT))

def close():
    pygame.quit()
    sys.exit()

# Main Function
def Table():
    loop = True

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

        for i in range(len(BALLS)):
            BALLS[i].draw(BALLS[i].x, BALLS[i].y)

        border()

        for i in range(noHoles):
            holes[i].draw()

        scoreBar()
        pygame.display.update()

Table()
