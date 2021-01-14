import pygame
from inputs import input

def main():
    pygame.init()

    key = pygame.key.get_pressed()

    res = (1024, 768)

    screen = pygame.display.set_mode(res)

    screen_color = (0,0,20)
    color = (255, 0, 0)

    pos = (512, 384)

    while (True):
        #Busca o evento
        events = pygame.event.get()

        for event in events:
            if (event.type == pygame.QUIT):
                exit()

        input(pos, res, key)
        
        if (key[pygame.K_ESCAPE]):
            break

        # Desenha
        screen.fill(screen_color)
        
        pygame.draw.circle(screen, color, pos, 20, 5)

        pygame.display.flip()

main()