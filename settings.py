class SETTING:
    def __init__(self):
        """initial screen settings """
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (240, 240, 240)
        self.game_title = "ALIEN INVASION :-)"
        #Ship settings
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_fired_once = 3
        #Aliens settings
        self.alien_speed = 0.3
        self.aliens_direction = 1
        self.drop = 8
        
