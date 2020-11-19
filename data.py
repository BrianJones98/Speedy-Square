import pygame, sys

pygame.init()
pygame.display.set_caption("Speedy Square")

screenSize = [1280, 720]

origSpeed = 20
xInitial = screenSize[0]/4
yInitial = screenSize[1]/2
window = pygame.display.set_mode((screenSize[0], screenSize[1]))

gameFont = pygame.font.SysFont('latin', 30, True)
pauseFont = pygame.font.SysFont('impact', 100)
timer = 0

hitSound = pygame.mixer.Sound('hit.wav')

#index corresponds with an obstacle type (0: damage, 1: slow, 2: no dash)
colorList = [(255, 0, 0), (255, 0, 255), (255, 255, 255)]
squareColor = (0, 0, 255)
invincibleColor = (0, 255, 255)

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
            while freeze:
                pygame.time.delay(60)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            timer = levelReset()
                            freeze = False
                        if event.key == pygame.K_ESCAPE:
                            return -100

                if timer < 60:
                    lossMessage = pauseFont.render("You Died", 1, (255, 0, 0))
                    subMessage1 = gameFont.render("Press Space to play again", 1, (255, 255, 255))
                    subMessage2 = gameFont.render("Press Escape to return to main menu", 1, (255, 255, 255))
                    window.fill((0, 0, 0))
                    window.blit(lossMessage, (screenSize[0]/3, 100))
                    window.blit(subMessage1, (screenSize[0]/3, screenSize[1]/2))
                    window.blit(subMessage2, (screenSize[0]/3, screenSize[1]/2 + 50))
                    checkInput = pygame.key.get_pressed()
                else:
                    winMessage = pauseFont.render("You Win!", 1, (0, 255, 0))
                    subMessage1 = gameFont.render("Press Space to play again", 1, (255, 255, 255))
                    subMessage2 = gameFont.render("Press Escape to return to main menu", 1, (255, 255, 255))
                    window.fill((0, 0, 0))
                    window.blit(winMessage, (screenSize[0]/3, 100))
                    window.blit(subMessage1, (screenSize[0]/3, screenSize[1]/2))
                    window.blit(subMessage2, (screenSize[0]/3, screenSize[1]/2 + 50))
                    checkInput = pygame.key.get_pressed()
                
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
    healthDisplay = gameFont.render(f"Health: {square.health}", 1, (255, 255, 255))
    timeDisplay = gameFont.render(f"Time: {timer}", 1, timeColor)
    window.blit(healthDisplay, (10, 10))
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