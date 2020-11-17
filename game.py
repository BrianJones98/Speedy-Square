from data import *

pygame.init()
pygame.display.set_caption("Speedy Square")

square = Player(xInitial, yInitial, (0, 255, 255))

def redrawGameWindow():
    window.fill((0, 0, 0))
    square.draw(window)
    pygame.display.update()

running = True
while running:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #movement
    if keys[pygame.K_a]:
        if square.x - square.speed <= 0:
            square.x = 0
        else:
            square.x -= square.speed
    if keys[pygame.K_d]:
        if square.x + square.speed >= screenSize[0] - square.size[0]:
            square.x = screenSize[0] - square.size[0]
        else:
            square.x += square.speed
    if keys[pygame.K_w]:
        if square.y - square.speed <= 0:
            square.y = 0
        else:
            square.y -= square.speed
    if keys[pygame.K_s]:
        if square.y + square.speed >= screenSize[1] - square.size[1]:
            square.y = screenSize[1] - square.size[1]
        else:
            square.y += square.speed

    #dash
    if keys[pygame.K_SPACE] and square.cooldown == 0:
        square.speed *= 4
        square.dashTime = 5
        square.cooldown = 10
    
    #loop end tasks
    if square.cooldown != 0 and square.dashTime > 0:
        square.dashTime -= 1
    if square.dashTime == 0 and square.cooldown != 0:
        square.speed = origSpeed
    if square.cooldown > 0:
        square.cooldown -= 1

    redrawGameWindow()

pygame.quit()