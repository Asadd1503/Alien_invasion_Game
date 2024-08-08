import pygame.font
class BUTTON:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings
    
        self.font = pygame.font.SysFont(None, 48)
        #initializing rect and adjusting it at the center of screen
        self.rect = pygame.Rect(0 ,0, self.settings.button_width, self.settings.button_height)
        self.rect.center = self.screen_rect.center
        
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """making the image of msg and declaring as rect"""
        self.msg_image = self.font.render(msg, True, self.settings.txt_clr)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """first drawing button rect and then msg image in it"""
        self.screen.fill(self.settings.button_rect_clr, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



