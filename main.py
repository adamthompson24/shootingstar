import pygame
import time
import random

pygame.init()

# Set and play music on a loop
gameSound = pygame.mixer.Sound("SpaceInvaderMusic1.mp3")
gameSound.set_volume(0.2)
gameSound.play(-1)

# Define colours for game
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Load images
currentlevel3 = pygame.image.load("images/sayslevel2.png")
currentlevel2 = pygame.image.load("images/sayslevel22.png")
currentlevel1 = pygame.image.load("images/sayslevel1.png")
level1complete = pygame.image.load("images/level1complete1.png")
level2complete = pygame.image.load("images/complete5.png")
level3complete = pygame.image.load("images/complete35.png")
level11 = pygame.image.load("images/1level1.png")
level22 = pygame.image.load("images/2level2.png")
level33 = pygame.image.load("images/3level3.png")
level111 = pygame.image.load("images/1level2.png")
level222 = pygame.image.load("images/1level22.png")
level333 = pygame.image.load("images/1level33.png")
selectlevelscreen = pygame.image.load("images/levelscreen1.png")
selectscreenmenu = pygame.image.load("images/selectshipscreen.png")
redx1 = pygame.image.load("images/redx.png")
whitex1 = pygame.image.load("images/whitex.png")
helpscreen1 = pygame.image.load("images/helpscreen.png")
titlepic1 = pygame.image.load("images/titlescreen2.png")
spacebackground = pygame.image.load("images/nbackground1.png")
spacebackground2 = pygame.image.load("images/background222.png")
spacebackground3 = pygame.image.load("images/background333.png")
rocket2pic = pygame.image.load("images/nred1.png")
rocket2pic2 = pygame.image.load("images/clickedship1.png")
rocket1pic = pygame.image.load("images/nblue1.png")
rocket1pic1 = pygame.image.load("images/clcikedship2.png")
star1 = pygame.image.load("images/nstar1.png")
asteroid1pic = pygame.image.load("images/astro2.png")
asteroid2pic = pygame.image.load("images/astro4.png")
asteroid3pic = pygame.image.load("images/astro35.png")
startImg = pygame.image.load("images/ttitle1.png")
quitImg = pygame.image.load("images/quit2.png")
clickStartImg = pygame.image.load("images/clickedttitle1.png")
clickQuitImg = pygame.image.load("images/clickedquit1.png")
selectText = pygame.image.load("images/CHOOSE3png.png")
helpImg = pygame.image.load("images/help1.png")
clickHelpImg = pygame.image.load("images/clickHelp1.png")

# Create main window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shooting Star")

# Set game clock
clock = pygame.time.Clock()

# Define spaceship parameters
playerparms = []
SpaceShip1parameters = [rocket2pic, 5, 377, 450, 36, 30, 1.1]
SpaceShip2parameters = [rocket1pic, 3.5, 380, 510, 30, 25, 1.02]


# Create common button format
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))


# Create spaceship button format
class SelectShipButton:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, parms, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                playerparms.append(parms[0])
                playerparms.append(parms[1])
                playerparms.append(parms[2])
                playerparms.append(parms[3])
                playerparms.append(parms[4])
                playerparms.append(parms[5])
                playerparms.append(parms[6])
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))


# Give coordinates of background
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))


# Set hitbox and speed of spaceship
class Player:
    def __init__(self, p_img, speedIn, spaceship_x, spaceship_y, hitbox_x, hitbox_y, speedmultiplier):
        self.speed = speedIn
        self.spaceship_x = spaceship_x
        self.spaceship_y = spaceship_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier


# Set hitbox and speed of asteroids
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y


# Score Function
def scorecounter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Stars Collected:" + str(count), True, white)
    gameDisplay.blit(text, (10, 0))

# Load high score
def loadHighScore(level):
    try:
        file = open("score" + str(level) + ".txt", "r")
        score = file.readline()
        file.close
        return int(score)
    except FileNotFoundError:
        return 0

# Show high score and save new high score
def showHighScore(score, highScore, level):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Highscore:" + str(highScore), True, white)
    gameDisplay.blit(text, (680, 0))

    # Save when new high score
    if score > highScore:
        highScore = score
        file = open("score" + str(level) + ".txt", "w")
        file.write(str(score))
        file.close()
    return highScore

# Format asteroid hit message
def text_objects(text, font):
    textsurface = font.render(text, True, blue)
    return textsurface, textsurface.get_rect()

# Stop game, print message and restart
def restartLevel1(text):
    largeText = pygame.font.Font("freesansbold.ttf", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop1()

# Set input crash message
def crashShipLevel1(message):
    restartLevel1(message)

# Stop game, print message and restart
def restartLevel2(text):
    largeText = pygame.font.Font("freesansbold.ttf", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop2()

# Set input crash message
def crashShipLevel2(message):
    restartLevel2(message)

# Stop game, print message and restart
def restartLevel3(text):
    largeText = pygame.font.Font("freesansbold.ttf", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop3()

# Set input crash message
def crashShipLevel3(message):
    restartLevel3(message)

# Function to quit
def quitgame():
    pygame.quit()
    quit()

# Main Menu
def mainmenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        bg = Background(titlepic1, 0, 0)

        startButton = Button(startImg, 308.5, 341.39, 183, 36, clickStartImg, 308.5, 341.39, levelScreen)
        helpButton = Button(helpImg, 322.81, 406.23, 150, 36, clickHelpImg, 322.81, 406.23, helpScreen)
        quitButton = Button(quitImg, 323.86, 471.44, 148, 42, clickQuitImg, 323.86, 471.44, quitgame)

        pygame.display.update()
        clock.tick(15)

# Help Screen
def helpScreen():
    help1 = True

    while help1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                pygame.display.update()
                clock.tick(15)

        gameDisplay.fill(black)
        bg = Background(helpscreen1, 0, 0)
        helpbackbutton = Button(whitex1, 16, 16, 64, 64, redx1, 16, 16, mainmenu)

        pygame.display.update()
        clock.tick(15)

# Level Screen
def levelScreen():
    level = True

    while level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectlevelscreen, (0, 0))
        level1Select = Button(level11, 76, 218, 169, 169, level111, 76, 218, selectScreen1)
        level2select = Button(level22, 319, 218, 169, 169, level222, 319, 218, selectScreen2)
        level3Select = Button(level33, 562, 218, 169, 169, level333, 562, 218, selectScreen3)

        pygame.display.update()
        clock.tick(15)

# User can select what ship they want to use for level 1
def selectScreen1():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectscreenmenu, (0, 0))
        SpaceShip1Select = SelectShipButton(rocket2pic, 258, 268, 40, 150, rocket2pic2, 250, 239, SpaceShip1parameters, game_loop1)
        SpaceShip2select = SelectShipButton(rocket1pic, 512, 297, 40, 100, rocket1pic1, 506, 280, SpaceShip2parameters, game_loop1)

        pygame.display.update()
        clock.tick(15)

# Level 1
def game_loop1():
    # Load high score
    highScore = loadHighScore(1)

    # Creates the falling objects and spaceships
    spaceship = Player(playerparms[0], playerparms[1], playerparms[2], playerparms[3], playerparms[4], playerparms[5],
                       playerparms[6])
    star = Gameobject(star1, 5, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid1 = Gameobject(asteroid1pic, 3, random.randrange(0, display_width - 20), -600, 40, 35)

    # Setting Variables
    x_change = 0
    score = 0
    gameexit = False

    # Gameloop to keep it running
    while not False:

        # Game background
        gameDisplay.fill(white)
        bg = Background(spacebackground, 0, 0)
        gameDisplay.blit(currentlevel1, (249, 8))
        maingamebackbutton = Button(whitex1, 16, 16, 64, 64, redx1, 16, 16, mainmenu)

        # Images for asteroids and stars
        gameDisplay.blit(star.b_image, (star.coord_x, star.coord_y))
        gameDisplay.blit(asteroid1.b_image, (asteroid1.coord_x, asteroid1.coord_y))

        # Users spaceship
        gameDisplay.blit(spaceship.p_img, (spaceship.spaceship_x, spaceship.spaceship_y))

        # Controls for the ship
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and spaceship.spaceship_x > 0:
                    x_change = spaceship.speed * -1 + -1 * spaceship.speedmult * score
                elif event.key == pygame.K_RIGHT and spaceship.spaceship_x < display_width - 45:
                    x_change = spaceship.speed + spaceship.speedmult * score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        spaceship.spaceship_x += x_change

        # Speed of the objects
        star.coord_y += star.speed
        asteroid1.coord_y += asteroid1.speed + 1.01 * score


        # Making sure the ship is in the width of the screen
        if spaceship.spaceship_x > display_width - spaceship.hitbox_x or spaceship.spaceship_x < 0:
            x_change = 0

        # Created boundaries for the falling objects
        if star.coord_y > display_height:
            star.coord_y = -10
            star.coord_x = random.randrange(0, display_width - 25)
        if asteroid1.coord_y > display_height - 10:
            asteroid1.coord_y = -10
            asteroid1.coord_x = random.randrange(0, display_width - 25)

        # Save score
        scorecounter(score)
        highScore = showHighScore(score, highScore, 1)

        # When hit by asteroid 1
        if spaceship.spaceship_y < asteroid1.coord_y + asteroid1.hitbox_y and spaceship.spaceship_y > asteroid1.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > asteroid1.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < asteroid1.coord_y + asteroid1.hitbox_y:
            if spaceship.spaceship_x > asteroid1.coord_x and spaceship.spaceship_x < asteroid1.coord_x + asteroid1.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid1.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid1.coord_x + asteroid1.hitbox_x:
                crashShipLevel1("Oh No! Your Spaceship Was Hit!")

        # When spaceship collects star
        if spaceship.spaceship_y < star.coord_y + star.hitbox_y and spaceship.spaceship_y > star.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > star.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < star.coord_y + star.hitbox_y:
            if spaceship.spaceship_x > star.coord_x and spaceship.spaceship_x < star.coord_x + star.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > star.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < star.coord_x + star.hitbox_x:
                star.coord_y = -10
                star.coord_x = random.randrange(0, display_width - 25)
                score += 1

                print(score)
        if score == 5:
            gameDisplay.blit(level1complete, (110, 222))
            pygame.display.update()
            clock.tick(30)

        pygame.display.update()
        clock.tick(60)

# User can select what ship they want to use for level 2
def selectScreen2():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectscreenmenu, (0, 0))
        SpaceShip1Select = SelectShipButton(rocket2pic, 258, 268, 40, 150, rocket2pic2, 250, 239, SpaceShip1parameters, game_loop2)
        SpaceShip2select = SelectShipButton(rocket1pic, 512, 297, 40, 100, rocket1pic1, 506, 280, SpaceShip2parameters, game_loop2)

        pygame.display.update()
        clock.tick(15)

# Level 2
def game_loop2():
    # Load high score
    highScore = loadHighScore(2)

    # Creates the falling objects and spaceships
    spaceship = Player(playerparms[0], playerparms[1], playerparms[2], playerparms[3], playerparms[4], playerparms[5],
                       playerparms[6])
    star = Gameobject(star1, 5, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid1 = Gameobject(asteroid1pic, 3, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid3 = Gameobject(asteroid2pic, 4, random.randrange(0, display_width - 20), random.randrange(-2000, -1000), 55,
                           100)

    # Setting Variables
    x_change = 0
    score = 0
    gameexit = False

    # Gameloop to keep it running
    while not False:

        # Game background
        gameDisplay.fill(white)
        bg = Background(spacebackground2, 0, 0)
        gameDisplay.blit(currentlevel2, (249, 8))
        maingamebackbutton = Button(whitex1, 16, 16, 64, 64, redx1, 16, 16, mainmenu)

        # Images for asteroids and stars
        gameDisplay.blit(star.b_image, (star.coord_x, star.coord_y))
        gameDisplay.blit(asteroid1.b_image, (asteroid1.coord_x, asteroid1.coord_y))
        gameDisplay.blit(asteroid3.b_image, (asteroid3.coord_x, asteroid3.coord_y))

        # Users spaceship
        gameDisplay.blit(spaceship.p_img, (spaceship.spaceship_x, spaceship.spaceship_y))

        # Controls for the ship
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and spaceship.spaceship_x > 0:
                    x_change = spaceship.speed * -1 + -1 * spaceship.speedmult * score
                elif event.key == pygame.K_RIGHT and spaceship.spaceship_x < display_width - 45:
                    x_change = spaceship.speed + spaceship.speedmult * score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        spaceship.spaceship_x += x_change

        # Speed of the objects
        star.coord_y += star.speed
        asteroid1.coord_y += asteroid1.speed + 1.01 * score
        asteroid3.coord_y += asteroid3.speed + 1.01 * score

        # Making sure the ship is in the width of the screen
        if spaceship.spaceship_x > display_width - spaceship.hitbox_x or spaceship.spaceship_x < 0:
            x_change = 0

        # Created boundaries for the falling objects
        if star.coord_y > display_height:
            star.coord_y = -10
            star.coord_x = random.randrange(0, display_width - 25)
        if asteroid1.coord_y > display_height - 10:
            asteroid1.coord_y = -10
            asteroid1.coord_x = random.randrange(0, display_width - 25)
        if asteroid3.coord_y > display_height:
            asteroid3.coord_y = -2000
            asteroid3.coord_x = random.randrange(0, display_width - 56)

        # Save score
        scorecounter(score)
        highScore = showHighScore(score, highScore, 2)

        # When hit by asteroid 1
        if spaceship.spaceship_y < asteroid1.coord_y + asteroid1.hitbox_y and spaceship.spaceship_y > asteroid1.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > asteroid1.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < asteroid1.coord_y + asteroid1.hitbox_y:
            if spaceship.spaceship_x > asteroid1.coord_x and spaceship.spaceship_x < asteroid1.coord_x + asteroid1.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid1.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid1.coord_x + asteroid1.hitbox_x:
                crashShipLevel2("Oh No! Your Spaceship Was Hit!")

        # When hit by asteroid 3
        if spaceship.spaceship_y < asteroid3.coord_y + asteroid3.hitbox_y:
            if spaceship.spaceship_x > asteroid3.coord_x and spaceship.spaceship_x < asteroid3.coord_x + asteroid3.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid3.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid3.coord_x + asteroid3.hitbox_x:
                crashShipLevel2("Oh no! Your Spaceship Was Hit!")

        # When spaceship collects star
        if spaceship.spaceship_y < star.coord_y + star.hitbox_y and spaceship.spaceship_y > star.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > star.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < star.coord_y + star.hitbox_y:
            if spaceship.spaceship_x > star.coord_x and spaceship.spaceship_x < star.coord_x + star.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > star.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < star.coord_x + star.hitbox_x:
                star.coord_y = -10
                star.coord_x = random.randrange(0, display_width - 25)
                score += 1

                print(score)
        if score == 5:
            gameDisplay.blit(level2complete, (110, 222))
            pygame.display.update()
            clock.tick(30)

        pygame.display.update()
        clock.tick(60)

# User can select what ship they want to use for level 3
def selectScreen3():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectscreenmenu, (0, 0))
        SpaceShip1Select = SelectShipButton(rocket2pic, 258, 268, 40, 150, rocket2pic2, 250, 239, SpaceShip1parameters, game_loop3)
        SpaceShip2select = SelectShipButton(rocket1pic, 512, 297, 40, 100, rocket1pic1, 506, 280, SpaceShip2parameters, game_loop3)

        pygame.display.update()
        clock.tick(15)

# Level 3
def game_loop3():
    # Load high score
    highScore = loadHighScore(3)

    # Creates the falling objects and spaceships
    spaceship = Player(playerparms[0], playerparms[1], playerparms[2], playerparms[3], playerparms[4], playerparms[5],
                       playerparms[6])
    star = Gameobject(star1, 5, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid1 = Gameobject(asteroid1pic, 3, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid2 = Gameobject(asteroid3pic, 3, random.randrange(0, display_width - 20), -1000, 40, 35)
    asteroid3 = Gameobject(asteroid2pic, 4, random.randrange(0, display_width - 20), random.randrange(-2000, -1000), 55,
                           100)

    # Setting Variables
    x_change = 0
    score = 0
    gameexit = False

    # Gameloop to keep it running
    while not False:

        # Game background
        gameDisplay.fill(white)
        bg = Background(spacebackground3, 0, 0)
        gameDisplay.blit(currentlevel3, (249, 8))
        maingamebackbutton = Button(whitex1, 16, 16, 64, 64, redx1, 16, 16, mainmenu)

        # Images for asteroids and stars
        gameDisplay.blit(star.b_image, (star.coord_x, star.coord_y))
        gameDisplay.blit(asteroid1.b_image, (asteroid1.coord_x, asteroid1.coord_y))
        gameDisplay.blit(asteroid2.b_image, (asteroid2.coord_x, asteroid2.coord_y))
        gameDisplay.blit(asteroid3.b_image, (asteroid3.coord_x, asteroid3.coord_y))

        # Users spaceship
        gameDisplay.blit(spaceship.p_img, (spaceship.spaceship_x, spaceship.spaceship_y))

        # Controls for the ship
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and spaceship.spaceship_x > 0:
                    x_change = spaceship.speed * -1 + -1 * spaceship.speedmult * score
                elif event.key == pygame.K_RIGHT and spaceship.spaceship_x < display_width - 45:
                    x_change = spaceship.speed + spaceship.speedmult * score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        spaceship.spaceship_x += x_change

        # Speed of objects
        star.coord_y += star.speed
        asteroid1.coord_y += asteroid1.speed + 1.01 * score
        asteroid2.coord_y += asteroid2.speed + 2 * score
        asteroid3.coord_y += asteroid3.speed + 1.01 * score

        # Making sure the ship is in the width of the screen
        if spaceship.spaceship_x > display_width - spaceship.hitbox_x or spaceship.spaceship_x < 0:
            x_change = 0

        # Created boundaries for the falling objects
        if star.coord_y > display_height:
            star.coord_y = -10
            star.coord_x = random.randrange(0, display_width - 25)
        if asteroid1.coord_y > display_height - 10:
            asteroid1.coord_y = -10
            asteroid1.coord_x = random.randrange(0, display_width - 25)
        if asteroid2.coord_y > display_height:
            asteroid2.coord_y = -410
            asteroid2.coord_x = random.randrange(0, display_width - 25)
        if asteroid3.coord_y > display_height:
            asteroid3.coord_y = -2000
            asteroid3.coord_x = random.randrange(0, display_width - 56)

        # Save score
        scorecounter(score)
        highScore = showHighScore(score, highScore, 3)

        # When hit by asteroid 1
        if spaceship.spaceship_y < asteroid1.coord_y + asteroid1.hitbox_y and spaceship.spaceship_y > asteroid1.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > asteroid1.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < asteroid1.coord_y + asteroid1.hitbox_y:
            if spaceship.spaceship_x > asteroid1.coord_x and spaceship.spaceship_x < asteroid1.coord_x + asteroid1.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid1.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid1.coord_x + asteroid1.hitbox_x:
                crashShipLevel3("Oh No! Your Spaceship Was Hit!")

        # When hit by asteroid 2
        if spaceship.spaceship_y < asteroid2.coord_y + asteroid2.hitbox_y and spaceship.spaceship_y > asteroid2.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > asteroid2.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < asteroid2.coord_y + asteroid2.hitbox_y:
            if spaceship.spaceship_x > asteroid2.coord_x and spaceship.spaceship_x < asteroid2.coord_x + asteroid2.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid2.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid2.coord_x + asteroid2.hitbox_x:
                crashShipLevel3("Oh no! Your Spaceship Was Hit!")

        # When hit by asteroid 3
        if spaceship.spaceship_y < asteroid3.coord_y + asteroid3.hitbox_y:
            if spaceship.spaceship_x > asteroid3.coord_x and spaceship.spaceship_x < asteroid3.coord_x + asteroid3.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid3.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid3.coord_x + asteroid3.hitbox_x:
                crashShipLevel3("Oh no! Your Spaceship Was Hit!")

        # When spaceship collects star
        if spaceship.spaceship_y < star.coord_y + star.hitbox_y and spaceship.spaceship_y > star.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > star.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < star.coord_y + star.hitbox_y:
            if spaceship.spaceship_x > star.coord_x and spaceship.spaceship_x < star.coord_x + star.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > star.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < star.coord_x + star.hitbox_x:
                star.coord_y = -10
                star.coord_x = random.randrange(0, display_width - 25)
                score += 1

                print(score)
        if score == 5:
            gameDisplay.blit(level3complete, (110, 222))
            pygame.display.update()
            clock.tick(30)

        pygame.display.update()
        clock.tick(60)


# Main
mainmenu()
selectScreen1()
game_loop1()
selectScreen2()
game_loop2()
selectScreen3()
game_loop3()
helpScreen()
pygame.QUIT()
quit()
