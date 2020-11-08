import pygame
pygame.init()


#definir color
BLACK  = (   0,   0,   0)
WHITE  = (   255,   255,   255)
GREEN  = (   0,   255,   0)
RED  = (   255,   0,   0)
BLUE = (0,   0,   255)


size = (800,500)

# Crear ventana
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

#color de fondo
    screen.fill(WHITE)
### zona de dibujo
    pygame.draw.line(screen, GREEN, [0,100], [100,100],5)
    pygame.draw.rect(screen,BLACK, (10,100,80,80))
    pygame.draw.circle(screen, BLACK, (200,200,), 30)
   
    pygame.display.flip()
