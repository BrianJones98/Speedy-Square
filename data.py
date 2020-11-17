import pygame

screenSize = [1280, 720]

origSpeed = 20
xInitial = screenSize[0]/4
yInitial = screenSize[1]/2
window = pygame.display.set_mode((screenSize[0], screenSize[1]))

#index corresponds with an obstacle type (0: damage, 1: slow, 2: no dash)
colorList = [(255, 0, 0), (255, 0, 255), (255, 255, 255)]

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = [20, 20]
        self.speed = origSpeed
        self.cooldown = 0
        self.dashTime = 0
        self.color = color
    
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

        if self.cooldown != 0 and self.dashTime > 0:
            self.dashTime -= 1
        if self.dashTime == 0:
            self.speed = origSpeed
        if self.cooldown > 0:
            self.cooldown -= 1

class Obstacle:
    def __init__(self, x, y, speed, objType, shape):
        self.x = x
        self.y = y
        self.speed = speed
        self.objType = objType
        self.color = colorList[objType]
        self.size = [50, 50]
        self.shape = shape

    def draw(self, window):
        if self.shape == 0:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.size[0], self.size[1]))
        else:
            pygame.draw.circle(window, self.color, (self.x, self.y), self.size[0])

square = Player(xInitial, yInitial, (0, 255, 255))
activeObstacles = []

def redrawGameWindow():
    window.fill((0, 0, 0))
    square.draw(window)
    for obstacle in activeObstacles:
        obstacle.draw(window)
    pygame.display.update()