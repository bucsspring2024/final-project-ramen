from src.arrow import Arrow
import pygame
import math
import time
import random
from src.hero import Hero
from src.airbend import Airbend

class Controller:
  def __init__(self):
    '''
    it creates background and dimensions of the background.
    sets color of text
    Args: self
    Returns: none
    '''
    pygame.init()
    self.display=pygame.display.set_mode((700,700))
    self.width,self.height=pygame.display.get_window_size()
    self.background=pygame.image.load("assets/backround.jpg")
    self.bg_rect= self.background.get_rect(topleft= (0,0))
    pygame.display.flip()
    self.text_color= (187,187,187)
    self.font= pygame.font.Font(None, 48)
   
    
    
  def mainloop(self):
    """
    it is the main driver code and is it where all the classes interact
    args:self
    return:none
    """
    collision=0
    level= 1
    speed= 1
    numArrow=4

    
    heart=Hero(305,350,"assets/heartshield.gif")
    hero=pygame.sprite.Group()
    hero.add(heart)
    
    snake=Airbend(355,350,"assets/snakeshield.png")
    airbend=pygame.sprite.Group()
    airbend.add(snake)
    
    arrowRight=pygame.sprite.Group()
    arrowLeft=pygame.sprite.Group() 
    arrowTop=pygame.sprite.Group()
    arrowBottom=pygame.sprite.Group()
  

    for i in range(level):
      arrowT= Arrow('top',random.randint(330,400),0,"assets/arrowf.png")
      arrowTop.add(arrowT)
      arrowB= Arrow('bottom',random.randint(330,400),700,"assets/arrowf.png")
      arrowBottom.add(arrowB)
      arrowR= Arrow('right',0,random.randint(370,450),"assets/arrowf.png")
      arrowRight.add(arrowR)
      arrowL= Arrow('left',700,random.randint(370,450),"assets/arrowf.png")
      arrowLeft.add(arrowL)
    text= self.font.render(f"Level: {level}",True,"red")
    numText=self.font.render(f"Arrow: {numArrow}",True,"red")
    overMsg= None
    run=True
    while run:
      
      pygame.time.Clock().tick(60)
      
      self.display.blit(self.background,(0,0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          run=False
          break
        arrowR.rect.right += speed
        arrowL.rect.left += speed
        arrowT.rect.top += speed
        arrowB.rect.bottom += speed
        
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
              
        if pygame.sprite.spritecollide(snake,arrowRight,True):
          arrowR.remove(arrowRight)
          collision += 1
          
            
        if pygame.sprite.spritecollide(snake,arrowLeft,True):
          arrowL.remove(arrowLeft)
          collision += 1
          

          
        if pygame.sprite.spritecollide(snake,arrowTop,True):
          arrowT.remove(arrowTop)
          collision += 1
          

          
        if pygame.sprite.spritecollide(snake,arrowBottom,True):
          arrowB.remove(arrowBottom)
          collision += 1
          
        if pygame.sprite.spritecollide(heart,arrowBottom,True):
          heart.remove(hero)
          time.sleep(1000000000)
          overMsg=self.font.render("GAME OVER",True,"red")

          
        if pygame.sprite.spritecollide(heart,arrowTop,True):
          heart.remove(hero)
          time.sleep(1000000000)
          
          overMsg=self.font.render("GAME OVER",True,"red")

        if pygame.sprite.spritecollide(heart,arrowRight,True):
          heart.remove(hero)
          time.sleep(1000000000)
          overMsg=self.font.render("GAME OVER",True,"red")

          
        if pygame.sprite.spritecollide(heart,arrowLeft,True):
          heart.remove(hero)
          time.sleep(100000000)
          overMsg=self.font.render("GAME OVER",True,"red")

          
        if collision==0:
          level=1
        else:
          level=int(math.log2(collision))
        
          arrowT= Arrow('top',random.randint(330,400),0,"assets/arrowf.png")
          arrowTop.add(arrowT)
          arrowB= Arrow('bottom',random.randint(330,400),700,"assets/arrowf.png")
          arrowBottom.add(arrowB)
          arrowR= Arrow('right',0,random.randint(370,450),"assets/arrowf.png")
          arrowRight.add(arrowR)
          arrowL= Arrow('left',700,random.randint(370,450),"assets/arrowf.png")
          arrowLeft.add(arrowL)
          numArrow += 4
      
        
              
      hero.draw(self.display)
      airbend.draw(self.display)
      self.display.blit(text,(300,600)) 
      self.display.blit(numText,(300,650))   
      arrowRight.draw(self.display)
      arrowRight.update('right',700,speed)
      arrowLeft.draw(self.display)
      arrowLeft.update('left',0,speed)
      arrowTop.draw(self.display)
      arrowTop.update('top',0,speed)
      arrowBottom.draw(self.display)
      arrowBottom.update('bottom',700,speed)
      
      text= self.font.render(f"Level: {level}",True,"red")
      numText= self.font.render(f"Arrows: {numArrow}",True,"red")
      pygame.display.update()
      
      if level==1:
        
        speed=1
      elif level==2:
        
        speed=3
      elif level==3:
       
        speed=5
      elif level==4:
        
        speed=10
      
                
    
        
