import random

from pygame import mixer


def blitme(self):
    if self.orientation == "Right":
        self.screen.blit(self.image, self.rect)
    elif self.orientation == "Left":
        self.screen.blit(pygame.transform.flip(self.image, False, True), self.rect)


import pygame

pygame.init()
mixer.init()

mixer.music.load('snd/audio2.ogg')
mixer.music.set_volume(100)
mixer.music.play()

height = 600
width = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Amogus")

ship = pygame.image.load("img/amogus.png").convert_alpha()
shipX = 0
shipY = 0

player = pygame.image.load("img/body.png").convert_alpha()
speed = 10
playerPositionX = 200
playerPositionY = 200
playerDeltaX = 0
playerDeltaY = 0

running = True
clock = pygame.time.Clock()
flip = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerDeltaY = -speed
            if event.key == pygame.K_s:
                playerDeltaY = speed
            if event.key == pygame.K_a:
                playerDeltaX = -speed
            if event.key == pygame.K_d:
                playerDeltaX = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerDeltaY = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerDeltaX = 0
    if playerDeltaX > 0:
        flip = False
    elif playerDeltaX < 0:
        flip = True
        mixer.music.play()

    playerPositionX += playerDeltaX
    playerPositionY += playerDeltaY

    if playerPositionX < 0:
        playerPositionX = 0
    if playerPositionY < 0:
        playerPositionY = 0
    if playerPositionX > width - 100:
        playerPositionX = width - 100
    if playerPositionY > height - 75:
        playerPositionY = height - 75

    screen.fill((255, 255, 255))

    if flip:
        screen.blit(pygame.transform.flip(player, True, False), (playerPositionX, playerPositionY))
    else:
        screen.blit(player, (playerPositionX, playerPositionY))

    shipY += 100
    if shipY > height + 50:
        shipY = -50
        shipX = random.randint(0, 750)

    screen.blit(ship, (shipX, shipY))

    pygame.display.update()
    clock.tick(600000)

pygame.quit()
