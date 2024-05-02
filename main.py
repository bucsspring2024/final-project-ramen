import pygame
from src.music import Music
from src.sample_controller import Controller

def main():
    pygame.init()
    controller=Controller()
    # music = Music()
    #Create an instance on your controller object
    #Call your mainloop
    # music.startmusic()
    controller.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
