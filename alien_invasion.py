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

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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
            self._update_screen()

if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

