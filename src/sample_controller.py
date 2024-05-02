from src.arrow import Arrow
import pygame
import time
import random
from src.hero import Hero
from src.airbend import Airbend
from src.arrow import *
class Controller:
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.display=pygame.display.set_mode((700,700))
    self.width,self.height=pygame.display.get_window_size()
    self.background=pygame.image.load("assets/backround.jpg")
    self.bg_rect= self.background.get_rect(topleft= (0,0))
    pygame.display.flip()
    self.text_color= (187,187,187)
    self.font= pygame.font.Font(None, 48)
    
  def mainloop(self):
    numArrow= 1
    speed= 5
    level=1
    heart=Hero(305,350,"assets/heartshield.gif")
    hero=pygame.sprite.Group()
    hero.add(heart)
    
    snake=Airbend(355,350,"assets/snakeshield.png")
    snake2=Airbend(355,350,"assets/snakeshield.png")
    airbend=pygame.sprite.Group()
    airbend.add(snake)
    airbend.add(snake2)
    
    arrowRight=pygame.sprite.Group()
    
    '''
    arrowTop=pygame.sprite.Group()
    arrowBottom=pygame.sprite.Group()
    arrowLeft=pygame.sprite.Group() 
    '''
    if len(arrowRight) < numArrow:
        arrow1= Arrow(0,350,"assets/arrowf.png")
        arrowRight.add(arrow1)
    
    
    text= self.font.render(f"Level: {level}",True,"red")
    run=True
    while run:
      
      pygame.time.Clock().tick(60)
      
      self.display.blit(self.background,(0,0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          run=False
          break
        arrow1.rect.right += speed
        # if event.type==pygame.WINDOWSHOWN:
        #   arrow1.rect.x += speed
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_RIGHT:
            if snake.rect.x <= 330:
              snake.rect.x += 50
          if event.key==pygame.K_LEFT:
            if snake.rect.x >= 300:
              snake.rect.x -= 50
          if event.key==pygame.K_UP:
            if snake.rect.top >= 310:
              snake.rect.y -= 50
          if event.key==pygame.K_DOWN:
            if snake.rect.bottom <= 450:
              snake.rect.y += 50
              
          if event.key==pygame.K_d:
            if snake2.rect.x <= 330:
              snake2.rect.x += 50
          if event.key==pygame.K_a:
            if snake2.rect.x >= 300:
              snake2.rect.x -= 50
          if event.key==pygame.K_w:
            if snake2.rect.top >= 310:
              snake2.rect.y -= 50
          if event.key==pygame.K_s:
            if snake2.rect.bottom <= 450:
              snake2.rect.y += 50
      
      hero.draw(self.display)
      airbend.draw(self.display)
      self.display.blit(text,(300,600))    
      arrowRight.draw(self.display)
      pygame.display.update()
                
    
        # if event.type==pygame.KEYDOWN:
          
    
    
    #select state loop
    
  
  ### below are some sample loop states ###

  # def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  # def gameloop(self):
      #event loop

      #update data

      #redraw
    
  # def gameoverloop(self):
      #event loop

      #update data

      #redraw
