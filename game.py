from data import *

pygame.init()
pygame.display.set_caption("Speedy Square")

running = True

while running:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    square.move(keys)

    redrawGameWindow()

pygame.quit()