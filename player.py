class Player:
    def __init__(self, pygame):
        self.texture = pygame.image.load("img/player.png").convert_alpha()
        self.speed = 10
        self.posX = 200
        self.posY = 200
        self.deltaX = 0
        self.deltaY = 0

    def move(self):
        self.posX += self.deltaX
        # self.posY += self.deltaY

    def print(self, screen):
        screen.blit(self.texture, (self.posX, self.posY))
