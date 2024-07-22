import pygame
class SHIP:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #loadig ship_image
        self.image = pygame.image.load('ship/myship.bmp')
        
        self.resize_image()
        self.ship_rect = self.image.get_rect()


        #starting new ship at the bottom
        self.ship_rect.midbottom = self.screen_rect.midbottom

    def resize_image(self):
        
        original_width, original_height = self.image.get_size()
        new_width = original_width//15
        new_height = original_height//15
        # Resize the image
        self.image = pygame.transform.scale(self.image, (new_width, new_height))




    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.ship_rect)

