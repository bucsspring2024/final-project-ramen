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
    self.clock.tick(60)
    self.text_color= (187,187,187)
    self.font= pygame.font.Font(None, 48)
    
  def mainloop(self):
    hero=Hero(305,350,"assets/heartshield.gif")
    hero_group=pygame.sprite.Group()
    hero_group.add(hero)
    airbend=Airbend(355,350,"assets/snakeshield.png")
    airbend_group=pygame.sprite.Group()
    airbend_group.add(airbend)
    num_arrow= 1
    arrow1_group=pygame.sprite.Group()
  
    # self.add1(num_arrow,arrow1_group)
    # self.arrow1_draw(num_arrow,arrow1_group)
    
    speed= 1
    level=1
    move= 200
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
      self.add1(num_arrow,arrow1_group)
      self.arrow1_draw(num_arrow,arrow1_group)

      
      # arrow1_group.draw(self.display)
      
      
      
      
      pygame.display.flip()
  def add1(self,num_arrow,arrow1_group):
      for arrow1 in range(num_arrow):
        x=50
        y=350
        arrow1=Arrow(x,y,"assets/arrowf.png")
        arrow1_group.add(arrow1)
        arrow1.rect.x += 1

      return arrow1_group
  def arrow1_draw(self,num_arrow,arrow1_group):
      for arrow1 in range(num_arrow):
        arrow1_group.update(350)
        arrow1_group.draw(self.display)
  # def add1(self,num_arrow,arrow1_group):
   
  #   for arrow1 in range(num_arrow):
  #     x1=100
  #     y1=350
  #     arrow1= Arrow(x1,y1,"assets/arrowf.png")
  #     arrow1_group=pygame.sprite.Group()
  #     arrow1_group.add(arrow1)
  #   return arrow1_group
  # def arrow1_draw(self,num_arrow,arrow1_group):
  #   for arrow1 in range(num_arrow):
  #     arrow1_group.draw(self.display)
  # def rand2(self,one,two):
  #   ran_x=random.randint(0,one)
  #   ran_y=random.randint(0,two)
  #   return ran_x,ran_y
  # def add2(self,num_arrow,arrow2_group):
  #   for arrow2 in range(num_arrow):
  #     ran_x,ran_y = self.rand2(ran_x,ran_y)
  #     arrow2= Arrow(ran_x,ran_y,"assets/arrowf.png")
  #     arrow2_group.add2(arrow2)
  #   return arrow2_group
  # def rand3(self,one,two):
  #   ran_x=random.randint(0,one)
  #   ran_y=random.randint(0,two)
  #   return ran_x,ran_y
  # def add3(self,num_arrow,arrow3_group):
  #   for arrow3 in range(num_arrow):
  #     ran_x,ran_y = self.rand3(700,500)
  #     arrow3= Arrow(ran_x,ran_y,"assets/arrowf.png")
  #     arrow3_group.add3(arrow3)
  #   return arrow3_group
  # def rand4(self,one,two):
  #   ran_x=random.randint(0,one)
  #   ran_y=random.randint(0,two)
  #   return ran_x,ran_y
  # def add4(self,num_arrow,arrow4_group):
  #   for arrow4 in range(num_arrow):
  #     ran_x,ran_y = self.rand4(700,500)
  #     arrow4= Arrow(ran_x,ran_y,"assets/arrowf.png")
  #     arrow4_group.add4(arrow4)
  #   return arrow4_group
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
