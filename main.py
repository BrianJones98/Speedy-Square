from levels import *

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)

font = pygame.font.SysFont("comicsans", 70)
WIDTH = 1280
HEIGHT = 780
title_font = pygame.font.SysFont("comicsans", 100)
options_font = pygame.font.SysFont("comicsans", 70)
start_font = pygame.font.SysFont("comicsans", 70)

def main_menu():
    click = False
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load('./music/main_menu.mp3')
    pygame.mixer.music.play(-1)

    run = True
    while run:
        pygame.time.delay(60)
        mx, my = pygame.mouse.get_pos()
        window.fill((0,0,0))
        title_label = title_font.render("Speedy Square", 1, (255,255,255))
        window.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 50))
        start_label = start_font.render("Start Game -- Click Mouse", 1, (255,255,255))
        window.blit(start_label, (WIDTH/2 - start_label.get_width()/2, 250))
        options_label = options_font.render("Options -- Press W", 1, (255,255,255))
        window.blit(options_label, (WIDTH/2 - options_label.get_width()/2, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                level1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    options()
                
        pygame.display.update()
    pygame.quit()

def options():
    running = True
    while running:
        pygame.time.delay(60)
        window.fill((0,0,0))
        title_label = title_font.render("Options", 1, (255,255,255))
        window.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()

main_menu()