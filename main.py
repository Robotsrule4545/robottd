#!/usr/bin/env python
import pygame
from pygame.locals import *
import os
import sys
import random
screen_height = 400
screen_width = 320
placing_ready = False
pausedGame = False

main_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(main_dir, "assets", file)
    surface = pygame.image.load(file)
    return surface.convert()


def exit(e):
    if e:
        pygame.quit()
        print("Quitting")
        sys.exit()


class Blaster(pygame.sprite.Sprite):
    images = []

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill((255, 255, 255))
        pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

    def update(self):
        # placeholder
        pos = pygame.mouse.get_pos()
        if abs(pos[0] - self.rect.x) < 20 and abs(pos[1] - self.rect.y) < 20 and pygame.mouse.get_pressed()[0]:
            self.kill()


def main():
    # Init
    pygame.init()
    # Divisible by 80, 10x8 grid of 16x16 squares.
    pygame.display.set_caption('Robot\'s Tower Defense')
    icon = pygame.transform.scale(load_image("icon.png"), (128, 128))
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((800, 640))

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    blaster_group = pygame.sprite.Group()

    # Update loop
    while True:
        global currentMousePos
        currentMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(True)
            if event.type == pygame.MOUSEBUTTONDOWN: # and placing_ready == True:
                blaster = Blaster(currentMousePos)
                blaster_group.add(blaster)
        screen.blit(background, (0, 0))
        pos = pygame.mouse.get_pos()

        blaster_group.draw(screen)
        blaster_group.update(currentMousePos)
        # Might be a problem when the background gets pasted over sprites
        pygame.display.flip()


if __name__ == '__main__':
    main()
