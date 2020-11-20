import pygame, sys

pygame.init()
pygame.display.set_caption("Speedy Square")

screenSize = [1280, 720]

origSpeed = 20
xInitial = screenSize[0]/4
yInitial = screenSize[1]/2
window = pygame.display.set_mode((screenSize[0], screenSize[1]))
# timer = 0
hitSound = pygame.mixer.Sound('hit.wav')

#fonts
gameFont = pygame.font.SysFont('latin', 30, True)
title_font = pygame.font.SysFont("Impact", 100)
menuItem_font = pygame.font.SysFont("comicsansms", 50, True)

#index corresponds with an obstacle type (0: damage, 1: slow, 2: no dash)
colorList = [(255, 0, 0), (255, 0, 255), (255, 255, 255)]
squareColor = (0, 0, 255)
invincibleColor = (0, 255, 255)

#colors for the box around each menu item
notSelected = (0, 0, 50)
selected = (0, 0, 100)

class MenuItem:
    def __init__(self, centeredY, text, textColor, boxColor, font):
        self.x = 0
        self.y = 0
        self.centeredY = centeredY
        self.text = text
        self.textColor = textColor
        self.boxColor = boxColor
        self.font = font
        self.width = 0
        self.height = 0

    def draw(self, window):
        global screenSize
        renderedText = self.font.render(self.text, 1, self.textColor)
        textRect = renderedText.get_rect()
        trCenter = textRect.center
        self.width = textRect.width + 20
        self.height = textRect.height + 20
        self.x = screenSize[0]/2-trCenter[0]-10
        self.y = self.centeredY - self.height/2
        if self.boxColor != None:
            pygame.draw.rect(window, self.boxColor, (screenSize[0]/2-trCenter[0]-10, self.centeredY-trCenter[1]-10, self.width, self.height))
        
        window.blit(renderedText, (screenSize[0]/2-trCenter[0], self.centeredY-trCenter[1]))

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = [20, 20]
        self.speed = origSpeed
        self.cooldown = 0
        self.dashTime = 0
        self.color = color
        self.health = 5
        self.hitRecovery = 0
        self.invincible = False
        self.debuffTimer = 0
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size[0], self.size[1]))
    
    def move(self, keys):
        if keys[pygame.K_a]:
            if self.x - self.speed <= 0:
                self.x = 0
            else:
                self.x -= self.speed
        if keys[pygame.K_d]:
            if self.x + self.speed >= screenSize[0] - self.size[0]:
                self.x = screenSize[0] - self.size[0]
            else:
                self.x += self.speed
        if keys[pygame.K_w]:
            if self.y - self.speed <= 0:
                self.y = 0
            else:
                self.y -= self.speed
        if keys[pygame.K_s]:
            if self.y + self.speed >= screenSize[1] - self.size[1]:
                self.y = screenSize[1] - self.size[1]
            else:
                self.y += self.speed

        if keys[pygame.K_SPACE] and self.cooldown == 0:
            self.speed *= 4
            self.dashTime = 5
            self.cooldown = 10
    
    def hit(self, hitType, timer):
        if self.invincible == False:
            if hitType == 0:
                self.health -= 1
                self.hitRecovery = 10
            elif hitType == 1:
                self.speed /= 2
                self.debuffTimer = 50
                self.hitRecovery = 10
            else:
                self.cooldown = 50
                self.hitRecovery = 10
            
            hitSound.play()
        
        if self.health <= 0:
            freeze = True
            lossMessage = MenuItem(100, "You Died", (255, 0, 0), None, title_font)
            winMessage = MenuItem(100, "You Win!", (0, 255, 0), None, title_font)
            exitLabel = MenuItem(screenSize[1]/2, "Return to Main Menu", (255, 255, 255), notSelected, menuItem_font)
            playAgainLabel = MenuItem(screenSize[1]/2 + 100, "Play Again!", (255, 255, 255), notSelected, menuItem_font)
            selected_option = 0
            
            while freeze:
                pygame.time.delay(60)
                window.fill((0, 0, 0))
                mx, my = pygame.mouse.get_pos()
                
                if exitLabel.x <= mx <= exitLabel.x + exitLabel.width and exitLabel.y <= my <= exitLabel.y + exitLabel.height:
                    selected_option = 1
                elif playAgainLabel.x <= mx <= playAgainLabel.x + playAgainLabel.width and playAgainLabel.y <= my <= playAgainLabel.y + playAgainLabel.height:
                    selected_option = 2
                else:
                    selected_option = 0

                if selected_option == 1:
                    exitLabel.boxColor = selected
                else:
                    exitLabel.boxColor = notSelected
                if selected_option == 2:
                    playAgainLabel.boxColor = selected
                else:
                    playAgainLabel.boxColor = notSelected

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if selected_option == 1:
                            return -100
                        elif selected_option == 2:
                            timer = levelReset()
                            freeze = False

                if timer < 60:
                    lossMessage.draw(window)
                    exitLabel.draw(window)
                    playAgainLabel.draw(window)
                else:
                    winMessage.draw(window)
                    exitLabel.draw(window)
                    playAgainLabel.draw(window)
                
                pygame.display.update()
        
        return timer

class Obstacle:
    def __init__(self, x, y, speed, objType, height, width, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.objType = objType
        self.color = colorList[objType]
        self.height = height
        self.width = width
        self.direction = direction

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

square = Player(xInitial, yInitial, squareColor)
activeObstacles = []

def redrawGameWindow(timeColor=(255,255,255), timer=0):
    window.fill((0, 0, 0))
    #Health Bar
    pygame.draw.rect(window, (255, 0, 0), (10, 10, 150, 20))
    pygame.draw.rect(window, (0, 128, 0), (10, 10, 150 - 30*(5 - square.health), 20))
    #Cooldown Bar
    pygame.draw.rect(window, (255, 255, 255), (10, 50, 150 - 3*(50 - square.cooldown), 20))
    #Status Bar
    pygame.draw.rect(window, (255, 0, 255), (200, 10, 100 - 2*(50 - square.debuffTimer), 20))
    timeDisplay = gameFont.render(f"Time: {timer}", 1, timeColor)
    window.blit(timeDisplay, (screenSize[0] - 115, 10))
    square.draw(window)
    for obstacle in activeObstacles:
        obstacle.draw(window)
    pygame.display.update()

def dropTimers():
    if square.debuffTimer > 0:
        square.debuffTimer -= 1
    if square.cooldown > 0:
        square.cooldown -= 1
    if square.dashTime > 0:
        square.dashTime -= 1
    if square.hitRecovery > 0:
        square.hitRecovery -= 1

def checkTimers():
    if square.debuffTimer == 0 and square.dashTime == 0:
        square.speed = origSpeed
    if square.dashTime > 0 or square.hitRecovery > 0:
        square.invincible = True
    else:
        square.invincible = False
    if square.invincible:
        square.color = invincibleColor
    else:
        square.color = squareColor

def levelReset():
    square.x = xInitial
    square.y = yInitial
    activeObstacles.clear()
    square.health = 5
    square.cooldown = 0
    square.dashTime = 0
    square.debuffTimer = 0
    return 0

def pauseGame(timer):
    pauseMessage = MenuItem(100, "Game Paused", (255, 255, 255), None, title_font)
    resumeLabel = MenuItem(screenSize[1]/2, "Resume", (255, 255, 255), notSelected, menuItem_font)
    restartLabel = MenuItem(screenSize[1]/2 + 100, "Restart Level", (255, 255, 255), notSelected, menuItem_font)
    mainMenuLabel = MenuItem(screenSize[1]/2 + 200, "Return to Main Menu", (255, 255, 255), notSelected, menuItem_font)
    
    selected_option = 0
    pause = True
    
    while pause:
        pygame.time.delay(60)
        mx, my = pygame.mouse.get_pos()
        window.fill((0, 0, 0))

        pauseMessage.draw(window)
        resumeLabel.draw(window)
        restartLabel.draw(window)
        mainMenuLabel.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_option == 1:
                    pause = False
                elif selected_option == 2:
                    timer = levelReset()
                    pause = False
                elif selected_option == 3:
                    return -100

        if resumeLabel.x <= mx <= resumeLabel.x + resumeLabel.width and resumeLabel.y <= my <= resumeLabel.y + resumeLabel.height:
            selected_option = 1
        elif restartLabel.x <= mx <= restartLabel.x + restartLabel.width and restartLabel.y <= my <= restartLabel.y + restartLabel.height:
            selected_option = 2
        elif mainMenuLabel.x <= mx <= mainMenuLabel.x + mainMenuLabel.width and mainMenuLabel.y <= my <= mainMenuLabel.y + mainMenuLabel.height:
            selected_option = 3
        else:
            selected_option = 0

        if selected_option == 1:
            resumeLabel.boxColor = selected
        else:
            resumeLabel.boxColor = notSelected
        if selected_option == 2:
            restartLabel.boxColor = selected
        else:
            restartLabel.boxColor = notSelected
        if selected_option == 3:
            mainMenuLabel.boxColor = selected
        else:
            mainMenuLabel.boxColor = notSelected

        pygame.display.update()
    
    return timer