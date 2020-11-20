from levels import *

def main_menu():
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load('./music/main_menu.mp3')
    pygame.mixer.music.play(-1)
    selected_option = 0

    #define menu items
    title = MenuItem(100, "Speedy Square", (255, 255, 255), None, title_font)
    start_label = MenuItem(screenSize[1]/2, "Level Select", (255, 255, 255), notSelected, menuItem_font)
    options_label = MenuItem(screenSize[1]/2 + 100, "Options", (255, 255, 255), notSelected, menuItem_font)

    menuObstacle_1 = Obstacle(50, 560, 0, 0, 20, 50, 0)
    menuObstacle_2 = Obstacle(1000, 600, 0, 1, 50, 100, 0)
    menuObstacle_3 = Obstacle(1200, 700, 0, 2, 10, 150, 0)
    menuObstacle_4 = Obstacle(100, 60, 0, 0, 50, 125, 0)
    menuObstacle_5 = Obstacle(850, 200, 0, 1, 70, 60, 0)
    menuObstacle_6 = Obstacle(900, 240, 0, 2, 20, 30, 0)
    menuObstacle_7 = Obstacle(1000, 123, 0, 0, 25, 100, 0)
    menuObstacle_8 = Obstacle(1000, 157, 0, 1, 50, 50, 0)
    menuObstacle_9 = Obstacle(400, 550, 0, 2, 100, 150, 0)
    menuObstacle_10 = Obstacle(300, 270, 0, 0, 120, 50, 0)

    menuPlayer = Player(640, 200, squareColor)

    run = True
    while run:
        pygame.time.delay(60)
        mx, my = pygame.mouse.get_pos()
        window.fill((0,0,0))

        #draw menu items on the screen
        title.draw(window)
        start_label.draw(window)
        options_label.draw(window)

        #draw menu decorations
        menuObstacle_1.draw(window)
        menuObstacle_2.draw(window)
        menuObstacle_3.draw(window)
        menuObstacle_4.draw(window)
        menuObstacle_5.draw(window)
        menuObstacle_6.draw(window)
        menuObstacle_7.draw(window)
        menuObstacle_8.draw(window)
        menuObstacle_9.draw(window)
        menuObstacle_10.draw(window)
        menuPlayer.draw(window)

        #check position of the mouse cursor, and see if it falls within a menu item
        if start_label.x <= mx <= start_label.x + start_label.width and start_label.y <= my <= start_label.y + start_label.height:
            selected_option = 1
        elif options_label.x <= mx <= options_label.x + options_label.width and options_label.y <= my <= options_label.y + options_label.height:
            selected_option = 2
        else:
            selected_option = 0

        if selected_option == 1:
            start_label.boxColor = selected
        else:
            start_label.boxColor = notSelected
        if selected_option == 2:
            options_label.boxColor = selected
        else:
            options_label.boxColor = notSelected
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #check if the mouse button has been clicked, and if a menu item is selected, run the appropriate function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_option == 1:
                    levelSelect()
                elif selected_option == 2:
                    options()
                
        pygame.display.update()
    pygame.quit()

def options():
    running = True
    while running:
        pygame.time.delay(60)
        window.fill((0,0,0))
        title_label = title_font.render("Options", 1, (255,255,255))
        window.blit(title_label, (screenSize[0]/2 - title_label.get_width()/2, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()

def levelSelect():
    running = True

    title = MenuItem(100, "Level Select", (255, 255, 255), None, title_font)
    level_1 = MenuItem(screenSize[1]/2 - 100, "Level 1", (255, 255, 255), notSelected, menuItem_font)
    level_2 = MenuItem(screenSize[1]/2, "Level 2", (255, 255, 255), notSelected, menuItem_font)
    level_3 = MenuItem(screenSize[1]/2 + 100, "Level 3", (255, 255, 255), notSelected, menuItem_font)
    level_4 = MenuItem(screenSize[1]/2 + 200, "Level 4", (255, 255, 255), notSelected, menuItem_font)

    while running:
        pygame.time.delay(60)
        window.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

        if level_1.x <= mx <= level_1.x + level_1.width and level_1.y <= my <= level_1.y + level_1.height:
            selected_option = 1
        elif level_2.x <= mx <= level_2.x + level_2.width and level_2.y <= my <= level_2.y + level_2.height:
            selected_option = 2
        elif level_3.x <= mx <= level_3.x + level_3.width and level_3.y <= my <= level_3.y + level_3.height:
            selected_option = 3
        elif level_4.x <= mx <= level_4.x + level_4.width and level_4.y <= my <= level_4.y + level_4.height:
            selected_option = 4
        else:
            selected_option = 0

        if selected_option == 1:
            level_1.boxColor = selected
        else:
            level_1.boxColor = notSelected
        if selected_option == 2:
            level_2.boxColor = selected
        else:
            level_2.boxColor = notSelected
        if selected_option == 3:
            level_3.boxColor = selected
        else:
            level_3.boxColor = notSelected
        if selected_option == 4:
            level_4.boxColor = selected
        else:
            level_4.boxColor = notSelected

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_option == 1:
                    level1()
                elif selected_option == 2:
                    level2()
                elif selected_option == 3:
                    level3()
                elif selected_option == 4:
                    level4()

        title.draw(window)

        level_1.draw(window)
        level_2.draw(window)
        level_3.draw(window)
        level_4.draw(window)

        pygame.display.update()

main_menu()