import pygame
from pygame.locals import *
from scripts.egg import Egg
import sys
pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 600), flags=RESIZABLE)
surf = pygame.surface.Surface((800, 600), flags=RESIZABLE)
egg = Egg(400, 300)
pygame.display.set_caption("Egg Drop")
while 1:
    for event in pygame.event.get():
        window.fill((0, 0, 0))
        window.blit(surf, (0,0))
        
        egg.main(surf)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)