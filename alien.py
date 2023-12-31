import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game) :
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.setings = ai_game.settings

       
        # load the Alien image and get its rect.

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen . 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        #store a decimal value for the ship's horizontal positon.
        #movement flags
        self.x = float(self.rect.x)

    def check_edge(self):
        """Return true  if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right or self.rect.left <= 0:
            return True

    def  update(self):
        """Move he alien to the right"""

        self.x += (self.setings.alien_speed* self.setings.fleet_direction)
        self.rect.x =self.x
        
    