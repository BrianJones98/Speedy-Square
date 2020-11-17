import pygame

screenSize = [1280, 720]

origSpeed = 20
xInitial = screenSize[0]/4
yInitial = screenSize[1]/2
window = pygame.display.set_mode((screenSize[0], screenSize[1]))

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
        if self.dashTime == 0 and self.cooldown != 0:
            self.speed = origSpeed
        if self.cooldown > 0:
            self.cooldown -= 1

square = Player(xInitial, yInitial, (0, 255, 255))

def redrawGameWindow():
    window.fill((0, 0, 0))
    square.draw(window)
    pygame.display.update()