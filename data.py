import pygame

screenSize = [1280, 720]

origSpeed = 20
xInitial = screenSize[0]/4
yInitial = screenSize[1]/2

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



window = pygame.display.set_mode((screenSize[0], screenSize[1]))