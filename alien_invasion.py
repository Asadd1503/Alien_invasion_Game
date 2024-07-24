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
            self.ship.update_ship()
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
                sys.exit(0)
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            
            
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
    
    def _check_keyup(self, event):
        """checking for key release"""
        # is it right key
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
                    
        # Is it left key
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False



    def _check_keydown(self, event):
        """checking for key press"""
        #is it right keyH
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        # Is it left key
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        # Is is q for quit
        elif event.key == pygame.K_q:
            sys.exit(0)
                    
            
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
                

