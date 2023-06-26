import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game) :
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
       
        # load the Alien image and get its rect.

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen . 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        #store a decimal value for the ship's horizontal positon.
        #movement flags
        self.x = float(self.rect.x)
