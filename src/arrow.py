import pygame
import random


class Arrow(pygame.sprite.Sprite):
    def __init__(self,dir, xA, yA, img):
        super().__init__()
        if dir == 'right':
            self.image=pygame.image.load(img)
            self.image = pygame.transform.scale(self.image, (40,40))
            self.image= pygame.transform.rotate(self.image,270)
            self.rect=self.image.get_rect()
            self.rect.bottom=yA
            self.x=xA
        elif dir == 'left':
            self.image=pygame.image.load(img)
            self.image = pygame.transform.scale(self.image, (40,40))
            self.image= pygame.transform.rotate(self.image,90)
            self.rect=self.image.get_rect()
            self.rect.bottom=yA
            self.x=xA  
        elif dir == 'top':
            self.image=pygame.image.load(img)
            self.image = pygame.transform.scale(self.image, (40,40))
            self.image= pygame.transform.rotate(self.image,0)
            self.rect=self.image.get_rect()
            self.rect.right=xA
            self.y=yA  
        elif dir == 'bottom':
            self.image=pygame.image.load(img)
            self.image = pygame.transform.scale(self.image, (40,40))
            self.image= pygame.transform.rotate(self.image,180)
            self.rect=self.image.get_rect()
            self.rect.right=xA
            self.y=yA 
    
            
    def update(self,dir,w,speed):
        if dir == 'right':
            self.rect.x += speed
            if self.rect.left>w:
                self.rect.right=0
        elif dir == 'left':
            self.rect.x -= speed
            if self.rect.right<w:
                self.rect.left=700
        elif dir == 'top':
            self.rect.bottom -= speed
            if self.rect.bottom < w:
                self.rect.top=700
        elif dir == 'bottom':
            self.rect.top += speed
            if self.rect.top > w:
                self.rect.bottom = 0
                    
        
    
        


    