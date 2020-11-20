from data import *
import random

def level1():
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load('./music/level1.mp3')
    pygame.mixer.music.play(-1)
    loops = 0
    timer = 0
    pause = False
    levelReset()
    
    running = True
    while running:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    timer = pauseGame(timer)

        for obstacle in activeObstacles:
            sqEndX = square.x + square.size[0]
            sqEndY = square.y + square.size[1]
            objEndX = obstacle.x + obstacle.width
            objEndY = obstacle.y + obstacle.height

            if square.x > obstacle.x - square.size[0] and sqEndX < objEndX + square.size[0]:
                if square.y > obstacle.y - square.size[1] and sqEndY < objEndY + square.size[1]:
                    timer = square.hit(obstacle.objType, timer)
            
            if obstacle.x <= screenSize[0] and obstacle.x >= 0:
                if obstacle.y <= screenSize[1] and obstacle.y >= 0:
                    if obstacle.direction == 0:
                        obstacle.x += obstacle.speed
                    else:
                        obstacle.y += obstacle.speed
                else:
                    activeObstacles.pop(activeObstacles.index(obstacle))
            else:
                activeObstacles.pop(activeObstacles.index(obstacle))

        if len(activeObstacles) < 10:
            # 0 right, 1 down, 2 left, 3 up
            objDirection = random.randint(0, 1)
            if objDirection == 0:
                objX = 0
                objY = random.randint(0, screenSize[1])
            else:
                objX = random.randint(0, screenSize[0])
                objY = 0
            
            objSpeed = random.randint(10, 20)
            objType = random.randint(0, 1)
            objWidth = random.randint(5, 100)
            objHeight = random.randint(5, 100)

            activeObstacles.append(Obstacle(objX, objY, objSpeed, objType, objWidth, objHeight, objDirection))

        direction = pygame.key.get_pressed()

        square.move(direction)

        dropTimers()
        checkTimers()
        if timer == -100:
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('./music/main_menu.mp3')
            pygame.mixer.music.play(-1)
            break
        
        loops += 1
        
        if loops >= 15:
            timer += 1
            loops = 0
        if timer >= 60:
            timeColor = (0, 255, 0)
        else:
            timeColor = (255, 255, 255)

        redrawGameWindow(timeColor, timer)

def level2():
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load('./music/level2.mp3')
    pygame.mixer.music.play(-1)
    loops = 0
    timer = 0
    pause = False
    levelReset()
    
    running = True
    while running:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    # pause = True
                    timer = pauseGame(timer)

        for obstacle in activeObstacles:
            sqEndX = square.x + square.size[0]
            sqEndY = square.y + square.size[1]
            objEndX = obstacle.x + obstacle.width
            objEndY = obstacle.y + obstacle.height

            if square.x > obstacle.x - square.size[0] and sqEndX < objEndX + square.size[0]:
                if square.y > obstacle.y - square.size[1] and sqEndY < objEndY + square.size[1]:
                    timer = square.hit(obstacle.objType, timer)
            
            if obstacle.x <= screenSize[0] and obstacle.x >= 0:
                if obstacle.y <= screenSize[1] and obstacle.y >= 0:
                    if obstacle.direction == 0:
                        obstacle.x += obstacle.speed
                    elif obstacle.direction == 1:
                        obstacle.y += obstacle.speed
                    else:
                        obstacle.x -= obstacle.speed
                else:
                    activeObstacles.pop(activeObstacles.index(obstacle))
            else:
                activeObstacles.pop(activeObstacles.index(obstacle))

        if len(activeObstacles) < 15:
            # 0 right, 1 down, 2 left, 3 up
            objDirection = random.randint(0, 2)
            if objDirection == 0:
                objX = 0
                objY = random.randint(0, screenSize[1])
            elif objDirection == 1:
                objX = random.randint(0, screenSize[0])
                objY = 0
            else:
                objX = screenSize[0]
                objY = random.randint(0, screenSize[1])
            
            objSpeed = random.randint(10, 50)
            objType = random.randint(0, 2)
            objWidth = random.randint(10, 125)
            objHeight = random.randint(10, 125)

            activeObstacles.append(Obstacle(objX, objY, objSpeed, objType, objWidth, objHeight, objDirection))

        direction = pygame.key.get_pressed()

        square.move(direction)

        dropTimers()
        checkTimers()
        if timer == -100:
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('./music/main_menu.mp3')
            pygame.mixer.music.play(-1)
            timer = 0
            break
        
        loops += 1
        
        if loops >= 15:
            timer += 1
            loops = 0
        if timer >= 60:
            timeColor = (0, 255, 0)
        else:
            timeColor = (255, 255, 255)

        redrawGameWindow(timeColor, timer)

def level3():
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load('./music/level3.mp3')
    pygame.mixer.music.play(-1)
    loops = 0
    timer = 0
    pause = False
    levelReset()
    
    running = True
    while running:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    # pause = True
                    timer = pauseGame(timer)

        for obstacle in activeObstacles:
            sqEndX = square.x + square.size[0]
            sqEndY = square.y + square.size[1]
            objEndX = obstacle.x + obstacle.width
            objEndY = obstacle.y + obstacle.height

            if square.x > obstacle.x - square.size[0] and sqEndX < objEndX + square.size[0]:
                if square.y > obstacle.y - square.size[1] and sqEndY < objEndY + square.size[1]:
                    timer = square.hit(obstacle.objType, timer)
            
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

        if len(activeObstacles) < 12:
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
            
            objSpeed = random.randint(10, 75)
            objType = random.randint(0, 2)
            objWidth = random.randint(10, 150)
            objHeight = random.randint(10, 150)

            activeObstacles.append(Obstacle(objX, objY, objSpeed, objType, objWidth, objHeight, objDirection))

        direction = pygame.key.get_pressed()

        square.move(direction)

        dropTimers()
        checkTimers()
        if timer == -100:
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('./music/main_menu.mp3')
            pygame.mixer.music.play(-1)
            timer = 0
            break
        
        loops += 1
        
        if loops >= 15:
            timer += 1
            loops = 0
        if timer >= 60:
            timeColor = (0, 255, 0)
        else:
            timeColor = (255, 255, 255)

        redrawGameWindow(timeColor, timer)

def level4():
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load('./music/level4.mp3')
    pygame.mixer.music.play(-1)
    loops = 0
    timer = 0
    pause = False
    levelReset()
    
    running = True
    while running:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    timer = pauseGame(timer)

        for obstacle in activeObstacles:
            sqEndX = square.x + square.size[0]
            sqEndY = square.y + square.size[1]
            objEndX = obstacle.x + obstacle.width
            objEndY = obstacle.y + obstacle.height

            if square.x > obstacle.x - square.size[0] and sqEndX < objEndX + square.size[0]:
                if square.y > obstacle.y - square.size[1] and sqEndY < objEndY + square.size[1]:
                    timer = square.hit(obstacle.objType, timer)
            
            if obstacle.x <= screenSize[0] and obstacle.x >= 0:
                if obstacle.y <= screenSize[1] and obstacle.y >= 0:
                    if obstacle.direction == 0:
                        obstacle.x += obstacle.speed
                    elif obstacle.direction == 1:
                        obstacle.y += obstacle.speed
                    elif obstacle.direction == 2:
                        obstacle.x -= obstacle.speed
                    elif obstacle.direction == 3:
                        obstacle.y -= obstacle.speed
                    elif obstacle.direction == 4:
                        obstacle.x += obstacle.speed
                        obstacle.y += obstacle.speed
                    elif obstacle.direction == 5:
                        obstacle.x -= obstacle.speed
                        obstacle.y += obstacle.speed
                    elif obstacle.direction == 6:
                        obstacle.x -= obstacle.speed
                        obstacle.y -= obstacle.speed
                    else:
                        obstacle.x += obstacle.speed
                        obstacle.y -= obstacle.speed
                else:
                    activeObstacles.pop(activeObstacles.index(obstacle))
            else:
                activeObstacles.pop(activeObstacles.index(obstacle))

        if len(activeObstacles) < 15:
            # 0 right, 1 down, 2 left, 3 up
            objDirection = random.randint(0, 7)
            if objDirection == 0:
                objX = 0
                objY = random.randint(0, screenSize[1])
            elif objDirection == 1:
                objX = random.randint(0, screenSize[0])
                objY = 0
            elif objDirection == 2:
                objX = screenSize[0]
                objY = random.randint(0, screenSize[1])
            elif objDirection == 3:
                objX = random.randint(0, screenSize[0])
                objY = screenSize[1]
            elif objDirection == 4:
                objX = 0
                objY = 0
            elif objDirection == 5:
                objX = screenSize[0]
                objY = 0
            elif objDirection == 6:
                objX = screenSize[0]
                objY = screenSize[1]
            else:
                objX = 0
                objY = screenSize[1]
            
            objSpeed = random.randint(10, 100)
            objType = random.randint(0, 2)
            objWidth = random.randint(10, 100)
            objHeight = random.randint(10, 100)

            activeObstacles.append(Obstacle(objX, objY, objSpeed, objType, objWidth, objHeight, objDirection))

        direction = pygame.key.get_pressed()

        square.move(direction)

        dropTimers()
        checkTimers()
        if timer == -100:
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('./music/main_menu.mp3')
            pygame.mixer.music.play(-1)
            timer = 0
            break
        
        loops += 1
        
        if loops >= 15:
            timer += 1
            loops = 0
        if timer >= 60:
            timeColor = (0, 255, 0)
        else:
            timeColor = (255, 255, 255)

        redrawGameWindow(timeColor, timer)