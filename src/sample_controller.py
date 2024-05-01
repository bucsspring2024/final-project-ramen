from src.arrow import Arrow
import pygame
import random
from src.hero import Hero
from src.airbend import Airbend

class Controller:
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.display=pygame.display.set_mode((700,700))
    self.width,self.height=pygame.display.get_window_size()
    self.background=pygame.image.load("assets/backround.jpg")
    self.bg_rect= self.background.get_rect(topleft= (0,0))
    self.clock= pygame.time.Clock()
    self.clock.tick(30)
    self.text_color= (187,187,187)
    self.font= pygame.font.Font(None, 48)
    
  def mainloop(self):
    hero=Hero(305,350,"assets/heartshield.gif")
    hero_group=pygame.sprite.Group()
    hero_group.add(hero)
    airbend=Airbend(355,350,"assets/snakeshield.png")
    airbend_group=pygame.sprite.Group()
    airbend_group.add(airbend)
    num_arrow= 32
    arrow_group= pygame.sprite.Group()
    arrow_group=self.add(num_arrow,arrow_group)
    speed= 2
    level=1
    move= 15
    text= self.font.render(f"Level: {level}",True,"red")
    run=True
    while run:
      self.display.blit(self.background,(0,0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          run=False
          break
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_RIGHT:
            if airbend.rect.x <= 330:
              airbend.rect.x += 50
          if event.key==pygame.K_LEFT:
            if airbend.rect.x >= 300:
              airbend.rect.x -= 50
          if event.key==pygame.K_UP:
            if airbend.rect.top >= 310:
              airbend.rect.y -= 50
          if event.key==pygame.K_DOWN:
            if airbend.rect.bottom <= 450:
              airbend.rect.y += 50
      hero_group.draw(self.display)
      airbend_group.draw(self.display)
      self.display.blit(text,(350,600))
      pygame.display.flip()
  def rand(self,one,two):
    ran_x=random.randint(0,one)
    ran_y=random.randint(0,two)
    return ran_x,ran_y
  def add(self,num_arrow,arrow_group):
    for arrow in range(num_arrow):
      ran_x,ran_y = self.rand(700,500)
      arrow= Arrow(ran_x,ran_y,"assets/arrow.png")
      arrow_group.add(arrow)
    return arrow_group
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
