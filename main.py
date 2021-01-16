import pygame

def main():
    pygame.init()

    screenX = 1024
    screenY = 768
    res = (screenX, screenY)

    screen = pygame.display.set_mode(res)

    screen_color = (0,0,20)
    color = (255, 0, 0)

    pos = (512, 384)

    while (True):
        #Busca o evento
        events = pygame.event.get()
        key = pygame.key.get_pressed()

        #Quando é carregada a tecla W
        if key[pygame.K_w]:
            pos = (pos[0], pos[1] - 1)
            if pos[1] < 0:
                pos = (pos[0], 0)

        #Quando é carregada a tecla S
        if key[pygame.K_s]:
            pos = (pos[0], pos[1] + 1)
            if pos[1] > screenY:
                pos = (pos[0], screenY)

        #Quando é carregada a tecla A
        if key[pygame.K_a]:
            pos = (pos[0] - 1, pos[1])
            if pos[0] < 0:
                pos = (0, pos[1])

        #Quando é carregada a tecla D
        if key[pygame.K_d]:
            pos = (pos[0] + 1, pos[1])
            if pos[1] > screenX:
                pos = (pos[0], screenX)
        
            #Quando é carregada a tecla ESC
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                    
            #Quando é carregado o botão para sair do programa
            if event.type == pygame.QUIT:
                exit()


        # Desenha
        screen.fill(screen_color)
        
        pygame.draw.circle(screen, color, pos, 20, 5)

        pygame.display.flip()

main()