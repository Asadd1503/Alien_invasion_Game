import sys
import pygame
from time import sleep
from settings import SETTING
from ship import SHIP
from bullet import BULLET
from alien import ALIEN
from game_stats import GAMESTATS
from button import BUTTON
from blast import BLAST
from scoreboard import SCOREBOARD

class AlienInvasion:
    """Main class to manage behavior of game"""
    def __init__(self):
        pygame.init()
        self.settings = SETTING()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.settings.game_title)
        self.game_stats = GAMESTATS(self)
        self.score_board = SCOREBOARD(self)
        self.ship = SHIP(self)
        self.blast = BLAST(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.button = BUTTON(self, "Press S to Start")
        self.game_over_button = BUTTON(self, "GAME OVER")
        self._set_coordinates_game_over_button()

        
        self._create_alien_fleet()

    def _set_coordinates_game_over_button(self):
        #setting coordinates to make it appear on the bootom of screen
        self.game_over_button.rect.midbottom = self.screen_rect.midbottom
        self.game_over_button.msg_image_rect.center = self.game_over_button.rect.center
        self.game_over_button.rect_y = float(self.game_over_button.rect.y)
        self.game_over_button.msg_y = float(self.game_over_button.msg_image_rect.y)

    def _create_alien_fleet(self):
        """Calculating space available for aliens and then placing them """
        alien = ALIEN(self)
        alien_width, alien_height = alien.rect.size
        #Calculating space for placing aliens in a row excluding left and right margins
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x//(2*alien_width)
        #Calculating available space excluding ship and 2 times alien height for firing field
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - ship_height - (2*alien_height)
        number_of_rows = available_space_y//(2*alien_height)
        #Creating first row of aliens
        for row_number in range(number_of_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(row_number, alien_number)
                               
    def _create_alien(self, row_number ,alien_number):
        new_alien = ALIEN(self)
        new_alien_width, new_alien_height = new_alien.rect.size
        new_alien.x = new_alien_width + 2 * new_alien_width * alien_number
        new_alien.rect.x = new_alien.x

        new_alien.y = new_alien_height + 2 * new_alien_height * row_number
        new_alien.rect.y = new_alien.y
        #Also upadting x and y coordinates of every alien instance before adding in group
        #Adding alien instance to goup name aliens so one function can be perform on all of them at a time
        self.aliens.add(new_alien)


    def run_game(self):
        """main loop for gameplay"""
        
        while True:
            self._check_event()
            if self.game_stats.game_active and not self.game_stats.game_over and not self.game_stats.game_pause:
                self.ship.update_ship()
                self._update_bullets()
                self._update_aliens()
            
            """ALL the commands to update screen like draw ship, color background, update screen to new etc."""
            self.screen.fill(self.settings.bg_color)   
            self.ship.blitme()
            #drawing bullet rectangle for every bullet object in bullets group
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            self.score_board.show_score()
            if not self.game_stats.game_active:
                self.button.draw_button()
            if self.game_stats.game_over:
                self.game_over_button.move_button_up()
                if self.game_over_button.rect.center <= self.screen_rect.center:
                    self._set_coordinates_game_over_button()
                    self.game_stats.game_over = False
                    break
                self.game_over_button.draw_button()
     
            pygame.display.flip()

    def _update_aliens(self):
        """calls _check_fleet_edge_and_drop() method and then calls update on each alien instance to make it move"""
        
        self._check_fleet_edge_and_drop()
        self.aliens.update()
        #Detecting collisiom between ship and aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #Checking if aliens have reached bottom of screen or not
        self._check_alien_at_bottom()


    def _check_alien_at_bottom(self):
        """Calling from update_aliens after ship_hit , checking wether aliens have reached bottom of screen or not"""
        """if yes then performing respective tasks"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                #then perform same tasks as ship has been hit
                self._ship_hit()
                break
            else:
                continue

    def _ship_hit(self):
        """Calling from update aliens, and doing tasks required after ship has been hit"""
        #decreasing ship limit in game stats
        self.game_stats.ships_left -= 1
        self.score_board.prep_ship()
        if self.game_stats.ships_left > 0:
            #removing reamining bullets and aliens on screen
            self.bullets.empty()
            self.aliens.empty()
            self._create_alien_fleet()
            #recentering ship
            self.ship.recenter_ship()
            #sleep time 
            sleep(self.settings.sleep_time)
        
        else:
            self.game_stats.game_over = True
            self.run_game()
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)
            #setting mouse cursor visible again
            #sleep(self.settings.sleep_time)
            #print("GAME OVER :-(")
            #pygame.quit()
            #sys.exit(0)



    def _check_fleet_edge_and_drop(self):
        """For each alien instance in group checks wether they have reached either edge of screen or not,"""
        """ if yes then drop them and add in their x coordinate in opposite direction """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                for each_alien in self.aliens.sprites():
                    each_alien.rect.y += self.settings.drop
                self.settings.aliens_direction *= -1
                break
            else:
                continue

    def _update_bullets(self):
        """update every bullet instance which has been created by pressing space"""
        self.bullets.update()

        #checks and delete every bullet in bullets group attribute if it passes above the display screen rect    
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.ship.screen_rect.top:
                self.bullets.remove(bullet)
            #print(len(self.bullets))   
        self._bullets_aliens_collisions()


    def _bullets_aliens_collisions(self):
        """ Now using pygame.sprite.groupcollide() to detect any collision between two groups and get rid of them,"""
        """if colision happens."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # If collisions dictionary exists do following tasks
            self._prepapre_and_display_blast(collisions)
        self._next_level()    
        
    def _prepapre_and_display_blast(self, collisions):
        # for the list of aliens hit by a bullet show blast image on their places
        for alien_list_shot in collisions.values():
            for alien in alien_list_shot:
                self.blast.rect.center = alien.rect.center
                #Delaying in while loop for displaying blast image and let every other image as it is
                for i in range(1, 10):
                    self._check_event()
                    self.ship.update_ship()
                    self.aliens.update()
                    self.bullets.update()
                    self.screen.fill(self.settings.bg_color)
                    self.ship.blitme()
                    for bullet in self.bullets.sprites():
                        bullet.draw_bullet()
                    self.blast.blitme()
                    self.aliens.draw(self.screen)
                    
                    pygame.display.flip()

    def _next_level(self):
        # If all the aliens have been shot dead then speed up the game and recreate alien fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.increase_game_pace()
            #Also increase level
            self.game_stats.level += 1
            self.game_stats.super_bullet = 1
            self.score_board.prep_level()
            self.score_board.check_high_level()


    def _shoot_bullets(self):
        if self.settings.bullets_fired_once > len(self.bullets):
            #giving large bullet perk on reaching every level mutiple of 3
            if (self.game_stats.level % 3) == 0:
                if self.game_stats.super_bullet <= 3:
                    self.settings.bullet_width = 500
                    self.settings.bullet_height = 3
                    self.game_stats.super_bullet += 1
                else:
                    self.settings.bullet_width = 3
                    self.settings.bullet_height = 10
            else:
                self.settings.bullet_width = 3
                self.settings.bullet_height = 10

            #on every tab of space making new bullet
            new_bullet = BULLET(self)
            #adding it to group bullets
            self.bullets.add(new_bullet)        

    def _update_screen(self):
        pass
         

    def _check_event(self):
        """checking for any input from user for exiting, etc."""
        for event in pygame.event.get():
            #checking for any mouse or keyboard input
            if event.type == pygame.QUIT:
                with open('highest_level.txt', 'w') as f:
                    f.write(str(self.game_stats.high_level))
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            
    
    def _check_keyup(self, event):
        """checking for key release"""
        # is it right key
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        # Is it left key
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _check_keydown(self, event):
        """checking for key press"""
        #is it right keyH
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        # Is it left key
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        # Is is q for quit
        elif event.key == pygame.K_q:
            with open('highest_level.txt', 'w') as f:
                f.write(str(self.game_stats.high_level))
            sys.exit(0)
        #Is it space
        elif event.key == pygame.K_SPACE:
            self._shoot_bullets()
        
        elif event.key == pygame.K_s:
            self._start_new_game()
        #Pausing game on p press
        elif event.key == pygame.K_p:
            self.game_stats.game_pause = True
        #Resuming game on r press
        elif event.key == pygame.K_r:
            self.game_stats.game_pause = False

    def _start_new_game(self):
        pygame.mouse.set_visible(False)
        self.game_stats.reset_stats()
        self.score_board.prep_ship()
        self.game_stats.game_active = True
        self.aliens.empty()
        self.bullets.empty()
        self._create_alien_fleet()
        self.ship.recenter_ship()
        self.settings.initialize_dynamic_settings()
        self.score_board.prep_level()

    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
                

