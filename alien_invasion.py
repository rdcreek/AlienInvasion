import sys
import pygame
from settings import Settings
class AlienInvasion:
    #Overall Class

    def __init__(self):
        #initialize the game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))


        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color = (230, 230, 230)
    def run_game(self):
        #start main loop for game
        #Watch for keyboard/mouse events.
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.Quit:
                    sys.exit()
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            #Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game

