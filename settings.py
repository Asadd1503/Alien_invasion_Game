class SETTING:
    def __init__(self):
        """initial screen settings """
        self.sleep_time = 1
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (240, 240, 240)
        self.game_title = "ALIEN INVASION :-)"
        #Ship settings
        
        #Bullet Settings
        
        self.bullet_width = 3 #3
        self.bullet_height = 10 #10
        self.bullet_color = (60, 60, 60)
        self.bullets_fired_once = 3
        #Aliens settings
        
        self.aliens_direction = 1
        self.drop = 25
        #Game stats
        self.ships_limit = 3
        #Button settings
        self.button_width = 300
        self.button_height = 60
        self.txt_clr = (30, 30, 30)
        self.button_rect_clr = (0, 255, 0)
        # Game pace speed contol
        self.speedup_scale = 1.1
        # alien point increase rate
        self.score_scale = 1.5
        #All the settings which will change throughout the game are declared in this method so that 
        #They can be reinitialized on the start of new game
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.bullet_speed = 1.5
        self.ship_speed = 0.75
        self.alien_speed = 0.25
        self.aliens_direction = 1
        self.alien_point = 50

    def increase_game_pace(self):
        """After all the aliens have shot down this method increases the game pace by a specified amount in setting class"""
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point*self.score_scale)
        

        
