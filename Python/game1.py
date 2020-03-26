#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      No
#
# Created:     23/03/2020
# Copyright:   (c) No 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import sys
import time
import random
import keyboard

pygame.init()

screen = pygame.display.set_mode((960, 540))

boxes = []
hi = 0
timefromjump = -1

def boxdimension(timefromstart):
    dimensions = 960-timefromstart
    return dimensions

def drawboxes(boxes):
    newboxes = []
    for i in boxes:
        pygame.draw.rect(screen, (0, 0, 0), (960-(2*i), 500, 20, 40), 0)
        i += 1
        if 2*i < 1010:
            newboxes.append(i)
    return newboxes

def draw(boxes):
    screen.fill((255, 255, 255))
    boxes = drawboxes(boxes)
    return boxes

def randboxes(hi):
    if hi == 0:
        hi = random.randint(75, 200)
    hi -= 1
    return hi

def createboxes(hi, boxes):
    if hi == 0:
        boxes.append(0)
    return (boxes)

def jump(timefromjump):
    height = 1+int(-0.1*(timefromjump-27.38)**2+75)
    if timefromjump == -1:
        pygame.draw.circle(screen, (0, 0, 0), (160, 515), 25, 0)
    else:
        pygame.draw.circle(screen, (0, 0, 0), (160, 515-height), 25, 0)
        print(height)
    if timefromjump != -1:
        timefromjump += 1
    if height <= 0:
        timefromjump = -1
    return timefromjump

while True:
    begindraw = time.time()
    boxes = createboxes(hi, boxes)
    hi = randboxes(hi)
    boxes = draw(boxes)
    timefromjump = jump(timefromjump)
    print(timefromjump)
    if timefromjump == -1:
        if keyboard.is_pressed('space'):
            timefromjump = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
    pygame.display.update()
    while True:
        enddraw = time.time()
        if enddraw >= (begindraw + (1/60)):
            break
