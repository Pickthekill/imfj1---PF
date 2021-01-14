import pygame

def input(pos, screen, key):

    if (key[pygame.K_w]):
        pos = (pos[0], pos[1] - 1)
        if (pos[1] < 0):
            pos = (pos[0], 0)
    
    if (key[pygame.K_s]):
        pos = (pos[0], pos[1] + 1)
        if (pos[1] > screen[1]):
            pos = (pos[0], screen[1])

    if (key[pygame.K_a]):
        pos = (pos[0]- 1, pos[1])
        if (pos[0] < 0):
            pos = (0, pos[1])
    
    if (key[pygame.K_d]):
        pos = (pos[0] + 1, pos[1])
        if (pos[1] > screen[0]):
            pos = (pos[0], screen[0])

    