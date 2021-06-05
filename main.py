import pygame
import time
import random

pygame.init()

# Colours for game
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Load images
beatlevelscreen1 = pygame.image.load("images/continue1.png")
clickedbeatlevelcontinue1 = pygame.image.load("images/clickedbeatcontinuelevel11.png")
clickedbeatlevelquit1 = pygame.image.load("images/clickedbeatquit11.png")
beatlevelcontinue1 = pygame.image.load("images/continue11.png")
beatlevelquit1 = pygame.image.load("images/quit11.png")
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
rocket2pic = pygame.image.load("images/nred1.png")
rocket2pic2 = pygame.image.load("images/clickedship1.png")
rocket1pic = pygame.image.load("images/nblue1.png")
rocket1pic1 = pygame.image.load("images/clcikedship2.png")
star1 = pygame.image.load("images/nstar1.png")
asteroid1pic = pygame.image.load("images/astro2.png")
asteroid2pic = pygame.image.load("images/astro4.png")
startImg = pygame.image.load("images/ttitle1.png")
quitImg = pygame.image.load("images/quit2.png")
clickStartImg = pygame.image.load("images/clickedttitle1.png")
clickQuitImg = pygame.image.load("images/clickedquit1.png")
selectText = pygame.image.load("images/CHOOSE3png.png")
helpImg = pygame.image.load("images/help1.png")
clickHelpImg = pygame.image.load("images/clickHelp1.png")

# Creating the Window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shooting Star")

# Setting Clock
clock = pygame.time.Clock()

# Player Class Parameters
playerparms = []
SpaceShip1parms = [rocket2pic, 5, 377, 450, 36, 30, 1.1]
SpaceShip2parms = [rocket1pic, 3.5, 380, 510, 30, 25, 1.02]


# Allows mouse to be used
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


# Allows the mouse to be used
class Button2:
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


# Gives coordinates of background
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))


# Sets hitbox and speed of spaceship
class Player:
    def __init__(self, p_img, speedIn, spaceship_x, spaceship_y, hitbox_x, hitbox_y, speedmultiplier):
        self.speed = speedIn
        self.spaceship_x = spaceship_x
        self.spaceship_y = spaceship_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier


# Sets hitbox and speed of asteroids
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
    gameDisplay.blit(text, (0, 0))


# When crashing into an asteroid message is displayed
def text_objects(text, font):
    textsurface = font.render(text, True, blue)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash(message):
    message_display(message)


# Function to quit
def quitgame():
    pygame.quit()
    quit()

# MainMenu
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

# HelpScreen
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

def levelScreen():
    level = True

    while level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectlevelscreen, (0, 0))
        level1Select = Button(level11, 76, 218, 169, 169, level111, 76, 218, selectScreen)
        level2select = Button(level22, 319, 218, 169, 169, level222, 319, 218, selectScreen)
        level3Select = Button(level33, 562, 218, 169, 169, level333, 562, 218, selectScreen)

        pygame.display.update()
        clock.tick(15)

# User can select what ship they want to use
def selectScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectscreenmenu, (0, 0))
        SpaceShip1Select = Button2(rocket2pic, 258, 268, 40, 150, rocket2pic2, 250, 239, SpaceShip1parms, game_loop)
        SpaceShip2select = Button2(rocket1pic, 512, 297, 40, 100, rocket1pic1, 506, 280, SpaceShip2parms, game_loop)

        pygame.display.update()
        clock.tick(15)


# MainGame
def game_loop():
    # Creates the falling objects and spaceships
    spaceship = Player(playerparms[0], playerparms[1], playerparms[2], playerparms[3], playerparms[4], playerparms[5],
                       playerparms[6])
    star = Gameobject(star1, 5, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid1 = Gameobject(asteroid1pic, 3, random.randrange(0, display_width - 20), -600, 40, 35)
    asteroid2 = Gameobject(asteroid1pic, 3, random.randrange(0, display_width - 20), -1000, 40, 35)
    asteroid3 = Gameobject(asteroid2pic, 4, random.randrange(0, display_width - 20), random.randrange(-2000, -1000), 55,
                           100)

    # Setting Variables
    x_change = 0
    score = 0

    score = 0

    if score == 1:
        # gameDisplay.fill(black)
        # gameDisplay.blit(beatlevelscreen1, (0, 0))
        continueLevel = Button(beatlevelcontinue1, 119, 260, 555, 38, clickedbeatlevelcontinue1, 119, 260, game_loop)
        quitLevel = Button(beatlevelquit1, 323, 329, 148, 41, clickedbeatlevelquit1, 323, 329, levelScreen)

        pygame.display.update()
        clock.tick(15)

    # Gameloop to keep it running
    while score != 1:

        # Game background
        gameDisplay.fill(white)
        bg = Background(spacebackground, 0, 0)

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

        # Speed of the objects
        star.coord_y += star.speed
        asteroid1.coord_y += asteroid1.speed + 1.01 * score
        asteroid2.coord_y += asteroid1.speed + 1.01 * score
        asteroid3.coord_y += asteroid3.speed

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
        # Score
        scorecounter(score)

        # When hit by asteroid 1
        if spaceship.spaceship_y < asteroid1.coord_y + asteroid1.hitbox_y and spaceship.spaceship_y > asteroid1.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > asteroid1.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < asteroid1.coord_y + asteroid1.hitbox_y:
            if spaceship.spaceship_x > asteroid1.coord_x and spaceship.spaceship_x < asteroid1.coord_x + asteroid1.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid1.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid1.coord_x + asteroid1.hitbox_x:
                crash("Oh No! Your Spaceship Was Hit!")

        # When hit by asteroid 2
        if spaceship.spaceship_y < asteroid2.coord_y + asteroid2.hitbox_y and spaceship.spaceship_y > asteroid2.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > asteroid2.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < asteroid2.coord_y + asteroid2.hitbox_y:
            if spaceship.spaceship_x > asteroid2.coord_x and spaceship.spaceship_x < asteroid2.coord_x + asteroid2.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid2.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid2.coord_x + asteroid2.hitbox_x:
                crash("Oh no! Your Spaceship Was Hit!")

        # When hit by asteroid 3
        if spaceship.spaceship_y < asteroid3.coord_y + asteroid3.hitbox_y:
            if spaceship.spaceship_x > asteroid3.coord_x and spaceship.spaceship_x < asteroid3.coord_x + asteroid3.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > asteroid3.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < asteroid3.coord_x + asteroid3.hitbox_x:
                crash("Oh no! Your Spaceship Was Hit!")

        # When spaceship collects star
        if spaceship.spaceship_y < star.coord_y + star.hitbox_y and spaceship.spaceship_y > star.coord_y or spaceship.spaceship_y + spaceship.hitbox_y > star.coord_y and spaceship.spaceship_y + spaceship.hitbox_y < star.coord_y + star.hitbox_y:
            if spaceship.spaceship_x > star.coord_x and spaceship.spaceship_x < star.coord_x + star.hitbox_x or spaceship.spaceship_x + spaceship.hitbox_x > star.coord_x and spaceship.spaceship_x + spaceship.hitbox_x < star.coord_x + star.hitbox_x:
                star.coord_y = -10
                star.coord_x = random.randrange(0, display_width - 25)
                score += 1
                print(score)





        pygame.display.update()
        clock.tick(60)


mainmenu()
selectScreen()
helpScreen()
game_loop()
pygame.QUIT()
quit()
