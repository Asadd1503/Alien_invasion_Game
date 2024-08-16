import pygame

class BLAST:
    def __init__(self, tp_game):
        self.screen = tp_game.screen
        
        self.image = pygame.image.load('ship/blast.bmp')
        self._resize_image()
        self.rect = self.image.get_rect()
        self.rect.topright = (0, 0)


    def _resize_image(self):
        """resize the image of ship which is quite large"""
        original_width, original_height = self.image.get_size()
        new_width = original_width//20
        new_height = original_height//20
        # Resize the image
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)