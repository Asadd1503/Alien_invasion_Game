import pygame
class SHIP:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        #X-coordinnate
        
        #loadig ship_image
        self.image = pygame.image.load('ship/myship.bmp')
        self._resize_image()
        #Making ship image a rectangle to make it esier to place using x y coordinates
        self.rect = self.image.get_rect()
        
        
        #flag for right movement and left movement
        self.move_right = False
        self.move_left = False
        #assignning ship image rectangle to screen which i made in Alien Invasion class for gameplay
        self.rect.midbottom = self.screen_rect.midbottom
        #Assigning ship rect mid bottom's x corordinate which it has taken from screen rect midbottom
        self.x = float(self.rect.x)
        self.rect.y -= (self.rect.height//10)

    def _resize_image(self):
        """resize the image of ship which is quite large"""
        original_width, original_height = self.image.get_size()
        new_width = original_width//20
        new_height = original_height//20
        # Resize the image
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def update_ship(self):
        """Increasing and decreasing rect X cordinate to move left or right"""
        
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed 

        self.rect.x = self.x

        
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def recenter_ship(self):
        """Calling from _ship_hit for recentering ship after it has been hit by alien"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.rect.y -= (self.rect.height//10)

