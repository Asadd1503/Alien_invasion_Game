import pygame
from pygame.sprite import Sprite

class ALIEN(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        #Giving surface to screen for future use in this class
        self.screen = ai_game.screen
        #Importing image and Making it rect
        self.image = pygame.image.load('ship/alien.bmp')
        self._resize_alien()
        self.rect = self.image.get_rect()
        #Setting  x,y coordinates of alien_rect
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Storing x coordinate for moving later
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



    def _resize_alien(self):
        """Decrease the image size by 20 times to make it fit in game window"""
        orig_width, orig_height = self.image.get_size()
        new_width = orig_width//20
        new_height = orig_height//20
        self.image = pygame.transform.scale(self.image, (new_width, new_height))