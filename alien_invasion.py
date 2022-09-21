import sys
import pygame
from settings import Settings
from ship import Ship
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
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        #start main loop for game
        #Watch for keyboard/mouse events.
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

