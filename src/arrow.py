import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, xA, yA, img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40,40))
        self.image= pygame.transform.rotate(self.image,270)
        self.rect=self.image.get_rect()
        self.x=xA
        self.y=yA
        self.move()
        
    
        


    