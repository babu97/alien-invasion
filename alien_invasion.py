import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behaviors."""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200,800), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.bullets.update()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self. _update_aliens()
            
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self.aliens.update()



    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)
            
    def _fire_bullet(self):
        """Create a new bullet and add it to to the bullets group,"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
           
    def _check_keydown_events(self,event):
        """Respond to Keypresses"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.quit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()


    def _check_keyup_events(self,event):
        """respond to keypressses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # update bullets positions.
        self.bullets.update()
        #get rid of bullets that have dissapeared
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
    def _create_fleet(self):
        """Create the fleet of aliens."""
        #make an alien. 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_X = available_space_x // (2*alien_width)
        #determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows  = available_space_y // (2*alien_height)

        #Create the first row of aliens. 
        for row_number in range(number_rows):
         for alien_number in range(number_aliens_X):
            #create an alien and place it in the row. 
           self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number, row_number):
        """Create analien and place it in the row"""
        alien =Alien(self)
        alien_width = alien.rect.width
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
        self.aliens.add(alien)

            

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
