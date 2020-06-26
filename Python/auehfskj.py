#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      No
#
# Created:     20/06/2020
# Copyright:   (c) No 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import time
import random

class ball:
    location = [400, 300]
    bounced = False

    def __init__(self, direction):
        self.direction = direction
        print(self.direction)

    def bounce(self):
        if self.bounced == False:
            if self.location[0] >= 800 or self.location[0] <= 0:
                self.direction[0] *= -1
                self.bounced = True
            if self.location[1] >= 600 or self.location[1] <= 0:
                self.direction[1] *= -1
                self.bounced = True
        elif self.bounced == True:
            if self.location[0] < 800 or self.location[0] > 0:
                self.bounced = False
            if self.location[1] < 600 or self.location[1] > 0:
                self.bounced = False

    def recalcposition(self, time):
        self.location[0] += self.direction[0]*time*25
        self.location[1] += self.direction[1]*time*25

    def draw(self):
        drawposition = [int(self.location[0]), 600-int(self.location[1])]
        pygame.draw.circle(gamedisplay, (0, 0, 0), drawposition, 5)


pygame.init()
gamedisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
lastframetime = time.time()

ball1 = ball([random.randint(-10, 10), random.randint(-10, 10)])
ball2 = ball([random.randint(-10, 10), random.randint(-10, 10)])
#ball3 = ball([random.randint(-10, 10), random.randint(-10, 10)])
#ball4 = ball([random.randint(-10, 10), random.randint(-10, 10)])
#ball5 = ball([random.randint(-10, 10), random.randint(-10, 10)])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gamedisplay.fill((255, 255, 255))

    ball1.draw()
    ball2.draw()
    #ball3.draw()
    #ball4.draw()
    #ball5.draw()

    pygame.display.update()

    ball1.recalcposition(time.time()-lastframetime)
    ball2.recalcposition(time.time()-lastframetime)
    #ball3.recalcposition(time.time()-lastframetime)
    #ball4.recalcposition(time.time()-lastframetime)
    #ball5.recalcposition(time.time()-lastframetime)

    ball1.bounce()
    ball2.bounce()
    #ball3.bounce()
    #ball4.bounce()
    #ball5.bounce()

    lastframetime = time.time()

    if time.time()-lastframetime < 0.007:
        time.sleep(0.007-(time.time()-lastframetime))


pygame.quit()












