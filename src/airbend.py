import pygame

class Airbend(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self,x):
        self.rect.x=(x)
    def update(self,y):
        self.rect.y=(y)