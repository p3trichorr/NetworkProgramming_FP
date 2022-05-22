from constant import *
from math import *

import pygame
import sys

pygame.display.set_caption("PyPool")
display = pygame.display.set_mode((WIDTH, OUTER_HEIGHT))

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

    h1 = Holes(0, 0, DARK)
    h2 = Holes(WIDTH/2 - h1.r*2, 0, DARK)
    h3 = Holes(WIDTH - h1.r - MARGIN - 5, 0, DARK)
    h4 = Holes(0, HEIGHT - MARGIN - 5 - h1.r, DARK)
    h5 = Holes(WIDTH/2 - h1.r*2, HEIGHT - MARGIN - 5 - h1.r, DARK)
    h6 = Holes(WIDTH - h1.r - MARGIN - 5, HEIGHT - MARGIN - 5 - h1.r, DARK)

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

        border()

        for i in range(noHoles):
            holes[i].draw()

        scoreBar()
        pygame.display.update()

Table()
