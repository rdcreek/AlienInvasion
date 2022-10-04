import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    #Overall Class

    def __init__(self):
        #initialize the game
        pygame.init()
        self.settings = Settings()

        """ Fullscreen mode--Comment out to use Windowed Settings"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


        # Windowed Mode--Comment out to use Fullscreen Settings.
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
            #Move ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            #Press 'q' to quit
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        self._update_screen()
        # Get rid of bullets that have gone off-screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            #Create an alien and place it in the row.
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)


    def run_game(self):
        #start main loop for game
        #Watch for keyboard/mouse events.
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()

if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

