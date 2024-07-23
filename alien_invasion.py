import sys
import pygame
from settings import SETTING
from ship import SHIP

class AlienInvasion:
    """Main class to manage behavior of game"""
    def __init__(self):
        pygame.init()
        self.settings = SETTING()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)
        self.ship = SHIP(self)
        

    def run_game(self):
        """main loop for gameplay"""
        
        while True:
            self._check_event()
            self._update_screen()
            
            
            

    def _update_screen(self):
        """commands to update screen like draw ship, color background, update screen to new etc."""
        self.screen.fill(self.settings.bg_color)   
        self.ship.blitme()
     
        pygame.display.flip()
         

    def _check_event(self):
        """checking for any input from user for exiting, etc."""
        for event in pygame.event.get():
                #checking for any mouse or keyboard input
                if event.type == pygame.QUIT:
                    sys.exit()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
                

