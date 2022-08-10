import pygame

class Egg():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("assets\gfx\player\egg.png")

    def main(self, surf):
        surf.blit(pygame.transform.scale(self.img, (32, 32)), (self.x, self.y))