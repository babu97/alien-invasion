import sys
import pygame
from settings import Settings
class AlienInvasion:
    """Overall class to manage game assets  and Behaviours."""
    def __init__(self) -> None:
        """initiate the game, and create game resources"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((self.settings.scree_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #set the game Background Color

        
        """start the main loop for the game."""

        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
            
            #make the most recenly drawn screen visible. 
            self.screen.fill(self.settings.bg_color)


            pygame.display.flip()
if __name__ =='__main__':
  #make a game instance, and run the game.

  ai = AlienInvasion()
  ai.run_game()
