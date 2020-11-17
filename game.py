from data import *
import random

pygame.init()
pygame.display.set_caption("Speedy Square")

running = True

while running:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obstacle in activeObstacles:
        if obstacle.x < screenSize[0] and obstacle.x > 0:
            obstacle.x += obstacle.speed
        else:
            activeObstacles.pop(activeObstacles.index(obstacle))

    if len(activeObstacles) < 10:
        objX = random.randint(0, screenSize[0])
        objY = random.randint(0, screenSize[1])
        objSpeed = random.randint(10, 50)
        objType = random.randint(0, 2)
        objShape = random.randint(0, 1)

        activeObstacles.append(Obstacle(objX, objY, objSpeed, objType, objShape))

    direction = pygame.key.get_pressed()
    square.move(direction)

    redrawGameWindow()

pygame.quit()