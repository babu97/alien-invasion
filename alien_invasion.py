import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    """Overall class to manage game assets  and Behaviours."""
    def __init__(self) -> None:
        """initiate the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)

        pygame.display.set_caption("Alien Invasion")
        #set the game Background Color

        
        """start the main loop for the game."""
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

            #watch for keyboard and mouse events.
    def _check_events(self):
            
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          #move the ship to the right. 
                          self.ship.moving_right = True
                     elif event.key  == pygame.K_LEFT:
                          self.ship.moving_left =True
                elif event.type == pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                          #move the ship to the right. 
                          self.ship.moving_right = False
                     elif event.key  == pygame.K_LEFT:
                          self.ship.moving_left =False

              

            #make the most recenly drawn screen visible.
    def _update_screen(self): 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()



            pygame.display.flip()
if __name__ =='__main__':
  #make a game instance, and run the game.

  ai = AlienInvasion()
  ai.run_game()