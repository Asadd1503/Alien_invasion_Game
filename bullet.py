import pygame
from pygame.sprite import Sprite

class BULLET(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        #making screen game display and settings attribute in bullet class
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Making bullet rectangle
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        #setting place at the mid top of ship_rect
        self.bullet_rect.midtop = ai_game.ship.ship_rect.midtop
        #storing bullet coordinate of midtop of ship_rect in y
        self.y = float(self.bullet_rect.y)

    def update(self):
        """moving the bullet up on the screen"""
        self.y -= self.settings.bullet_speed
        self.bullet_rect.y = self.y
        



        
    def draw_bullet(self):
        #Drawing using method in pygame.draw class 
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)

