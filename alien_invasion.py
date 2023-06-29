import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import Gamestats
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
       # self.screen = pygame.display.set_mode((1200,800), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")
        # create an instance to store hame stastics 
        self.stats = Gamestats(self)

        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
          self._check_events()
          if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self. _update_aliens()
            
          self._update_screen()
            
    def _update_aliens(self):
        """check if the fleet is at the edge then update the positions of the all aliens  in the fleet
        """
        self._check_fleet_edges()
        """Update the positions of all aliens in the fleet"""
        self.aliens.update()
        #look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        #look for aliens hittinh the bottom of the screeb
        self._check_aliens_bottom()



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
                sys.exit()
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
        #check for any bullets that have hit aliens
        #if so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        #Destroy existing bullets and create new fleet
        if not self.aliens:
         self.bullets.empty()
         self._create_fleet()
        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

   
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens has reached  an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
            break
    def _change_fleet_direction(self):
        """Drop the entire fleet and change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()
    def _ship_hit(self):
        """Respind to ship being hit by an alien"""
        if self.stats.ships_left >0:
            #Decrement ships left.
            self.stats.ships_left -= 1
            #get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
    
        else:
         self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect =self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if the ship got hit
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
