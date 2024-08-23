
class GAMESTATS:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        #starting game inn inactive state
        self.game_active = False
        self.game_over = False
        self.game_pause = False
        self.high_score = 0
        self.super_bullet = 1
        #Try opening highest_level.txt file if it does'nt exist playing for the first time
        #Then wirte file with 0 in it
        try:
            with open('highest_level.txt', 'r') as f:
                highest_level = f.read()
        except:
            with open('highest_level.txt', 'w') as f:
                highest_level = 1
                f.write(str(highest_level))
                self.high_level = highest_level
        else:
            self.high_level = int(highest_level)






    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1
        


