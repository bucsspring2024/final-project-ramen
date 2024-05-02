import pygame

class Music: 
    def startmusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music.wav")
        pygame.mixer.music.play(-1)