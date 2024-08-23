import pygame.font
import pygame
from ship import SHIP

class SCOREBOARD:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
        self.font = pygame.font.SysFont(None, 48)
        self.txt_color = (30, 30, 30)

        
        self.prep_level()
        self.prep_ship()
        self.prep_high_level()

    def prep_ship(self):
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.game_stats.ships_left):
            ship = SHIP(self)
            ship.rect.topleft = self.screen_rect.topleft
            ship.rect.x = 10 + ship.rect.width*ship_number
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_high_level(self):
        high_level_str = str(self.game_stats.high_level)
        self.high_level_image = self.font.render("Highest: "+high_level_str, True, self.txt_color, self.settings.bg_color)
        self.high_level_rect = self.high_level_image.get_rect()
        self.high_level_rect.midtop = self.screen_rect.midtop
        self.high_level_rect.y += 5

   
    def prep_level(self):
        level_str = str(self.game_stats.level)
        self.level_image = self.font.render("Level: "+level_str, True, self.txt_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 10

    def check_high_level(self):
        if self.game_stats.level > self.game_stats.high_level:
            self.game_stats.high_level = self.game_stats.level
            self.prep_high_level()


    def show_score(self):
        """displaying score instance"""
        self.ships.draw(self.screen)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_level_image, self.high_level_rect)
