import pygame
class SHIP:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #loadig ship_image
        self.image = pygame.image.load('ship/myship.bmp')
        self._resize_image()
        #Making ship image a rectangle to make it esier to place using x y coordinates
        self.ship_rect = self.image.get_rect()


        #assignning ship image rectangle to screen which i made in Alien Invasion class for gameplay
        self.ship_rect.midbottom = self.screen_rect.midbottom

    def _resize_image(self):
        """resize the image of ship which is quite large"""
        original_width, original_height = self.image.get_size()
        new_width = original_width//20
        new_height = original_height//20
        # Resize the image
        self.image = pygame.transform.scale(self.image, (new_width, new_height))




    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.ship_rect)

