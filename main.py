import random

import pygame
from pygame import mixer

pygame.init()
mixer.init()

mixer.music.load('snd/audio2.ogg')
mixer.music.set_volume(100)
# mixer.music.play()

height = 600
width = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Amogus")

background = pygame.image.load("img/Background/starBackground.png").convert()

ship = pygame.image.load("img/enemyShip.png").convert_alpha()
shipX = 0
shipY = 0
shipSpeed = 2

player = pygame.image.load("img/player.png").convert_alpha()
playerSpeed = 10
playerPositionX = 200
playerPositionY = height - 100
playerDeltaX = 0
playerDeltaY = 0

shoot = pygame.image.load("img/laserRed.png").convert_alpha()
shooting = False
shootX = 0
shootY = 0

score = 0
scoreFont = pygame.font.SysFont("Arial", 30)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerDeltaY = -playerSpeed
            if event.key == pygame.K_s:
                playerDeltaY = playerSpeed
            if event.key == pygame.K_a:
                playerDeltaX = -playerSpeed
            if event.key == pygame.K_d:
                playerDeltaX = playerSpeed
            if event.key == pygame.K_h and not shooting:
                shooting = True
                shootX = playerPositionX
                shootY = playerPositionY
            if event.key == pygame.K_p:
                background = pygame.image.load("img/body.png").convert()
                shoot = pygame.image.load("img/amogus.png").convert_alpha()
            if event.key == pygame.K_o:
                background = pygame.image.load("img/Background/starBackground.png").convert()
                shoot = pygame.image.load("img/laserRed.png").convert_alpha()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerDeltaY = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerDeltaX = 0

    playerPositionX += playerDeltaX
    # playerPositionY += playerDeltaY

    if playerPositionX < 0:
        playerPositionX = 0
    if playerPositionY < 0:
        playerPositionY = 0
    if playerPositionX > width - 100:
        playerPositionX = width - 100
    if playerPositionY > height - 75:
        playerPositionY = height - 75

    screen.fill((255, 255, 255))
    for i in range(10):
        for j in range(10):
            screen.blit(background, (i * 254, j * 256))
    screen.blit(player, (playerPositionX, playerPositionY))

    if shooting:
        shootY -= 20
        screen.blit(shoot, (shootX, shootY))

        if shipX + 98 > shootX and shipX < shootX + 33:
            if shipY + 50 > shootY and shipY < shootY + 9:
                score += 1
                print("Treffer:", score)
                shooting = False
                shipY = 0
                shipX = random.randint(0, width - 50)

        if shootY <= 0:
            shooting = False

    shipX += shipSpeed

    if shipX + 98 > playerPositionX and shipX < playerPositionX + 99:
        if shipY + 50 > playerPositionY and shipY < playerPositionY + 75:
            shipX -= shipSpeed
            print("SUS")

    if shipY > height + 50:
        shipY = -50
        shipX = random.randint(0, 750)

    if shipX < 0:
        shipSpeed = -shipSpeed
        shipX = 0
        shipY += 50
    elif shipX > width - 60:
        shipSpeed = -shipSpeed
        shipX: 800
        shipY += 60
    screen.blit(ship, (shipX, shipY))

    scoreText = scoreFont.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(scoreText, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
