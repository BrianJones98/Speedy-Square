from data import *
import random

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    # surface.blit(textobj, textrect)

click = False
font = pygame.font.SysFont("comicsans", 70)
def main_menu():
    run = True
    while run:
        
        window.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screenSize, 20, 20)
        
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        pygame.draw.rect(window, (255, 0, 0), button_2)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.update()

def game():
    running = True

    while running:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obstacle in activeObstacles:
            sqEndX = square.x + square.size[0]
            sqEndY = square.y + square.size[1]
            objEndX = obstacle.x + obstacle.width
            objEndY = obstacle.y + obstacle.height

            if square.x > obstacle.x - square.size[0] and sqEndX < objEndX + square.size[0]:
                if square.y > obstacle.y - square.size[1] and sqEndY < objEndY + square.size[1]:
                    square.hit(obstacle.objType)
            
            if obstacle.x <= screenSize[0] and obstacle.x >= 0:
                if obstacle.y <= screenSize[1] and obstacle.y >= 0:
                    if obstacle.direction == 0:
                        obstacle.x += obstacle.speed
                    elif obstacle.direction == 1:
                        obstacle.y += obstacle.speed
                    elif obstacle.direction == 2:
                        obstacle.x -= obstacle.speed
                    else:
                        obstacle.y -= obstacle.speed
                else:
                    activeObstacles.pop(activeObstacles.index(obstacle))
            else:
                activeObstacles.pop(activeObstacles.index(obstacle))

        if len(activeObstacles) < 10:
            # 0 right, 1 down, 2 left, 3 up
            objDirection = random.randint(0, 3)
            if objDirection == 0:
                objX = 0
                objY = random.randint(0, screenSize[1])
            elif objDirection == 1:
                objX = random.randint(0, screenSize[0])
                objY = 0
            elif objDirection == 2:
                objX = screenSize[0]
                objY = random.randint(0, screenSize[1])
            else:
                objX = random.randint(0, screenSize[0])
                objY = screenSize[1]
            
            objSpeed = random.randint(10, 50)
            objType = random.randint(0, 2)
            objWidth = random.randint(10, 100)
            objHeight = random.randint(10, 100)

            activeObstacles.append(Obstacle(objX, objY, objSpeed, objType, objWidth, objHeight, objDirection))

        direction = pygame.key.get_pressed()
        square.move(direction)

        dropTimers()
        checkTimers()

        redrawGameWindow()

    pygame.quit()

def options():
    running = True
    while running:
        draw_text('Options', font, (255, 255, 255), screenSize, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()

main_menu()