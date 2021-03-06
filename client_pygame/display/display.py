#
# This file is where you make the display for your game
# Make changes and add functions as you need.
#

import math
import pygame
from config import *
from common.event import *
from client.base_display import BaseDisplay

class Display(BaseDisplay):
    """
    This class controls all of the drawing of the screen
    for your game.  The process of drawing a screen is
    to first draw the background, and then draw everything
    that goes on top of it.  If two items are drawn in the
    same place, then the last item drawn will be the one
    that is visible.

    The screen is a 2 dimensional grid of pixels, with the
    origin (0,0) located at the top-left of the screen, and
    x values increase to the right and y values increase as
    you go down.  The y values are opposite of what you learned
    in your math classes.

    Documentation on drawing in pygame is available here:
    http://www.pygame.org/docs/ref/draw.html

    The methods in this class are:
    __init__ creates data members (variables) that are used
        in the rest of the methods of this class.  This is
        useful for defining colors and sizes, loading image
        or sound files, creating fonts, etc.  Basically,
        any one time setup.

    paint_game controls the drawing of the screen while the
        game is in session.  This is responsible for making
        sure that any information, whether graphics, text, or
        images are drawn to the screen.

    paint_waiting_for_game controls the drawing of the screen
        after you have requested to join a game, but before
        the game actually begins.
    
    paint_game_over controls the drawing of the screen after
        the game has been won, but before the game goes away.
        This is a short (3-5 second) period.

    process_event controls handling events that occur in the
        game, that aren't represented by objects in the game
        engine.  This includes things like collisions,
        objects dying, etc.  This would be a great place to
        play an audio file when missiles hit objects.

    paint_pregame controls the drawing of the screen before
        you have requested to join a game.  This would usually
        allow the user to know the options available for joining
        games.

    Method parameters and data members of interest in these methods:
    self.width is the width of the screen in pixels.
    self.height is the height of the screen in pixels.
    self.* many data members are created in __init__ to set up
        values for drawing, such as colors, text size, etc.
    surface is the screen surface to draw to.
    control is the control object that is used to
        control the game using user input.  It may
        have data in it that influences the display.
    engine contains all of the game information about the current
        game.  This includes all of the information about all of
        the objects in the game.  This is where you find all
        of the information to display.
    event is used in process_event to communicate what
        interesting thing occurred.
    
    Note on text display:  There are 3 methods to assist
    in the display of text.  They are inherited from the
    BaseDisplay class.  See client/base_display.py.
    
    """

    def __init__(self, width, height):
        """
        Configure display-wide settings and one-time
        setup work here.
        """
        BaseDisplay.__init__(self, width, height)

        # There are other fonts available, but they are not
        # the same on every computer.  You can read more about
        # fonts at http://www.pygame.org/docs/ref/font.html
        self.font_size = 30
        self.font = pygame.font.SysFont("oldenglishtext",self.font_size)
       

        # Colors are specified as a triple of integers from 0 to 255.
        # The values are how much red, green, and blue to use in the color.
        # Check out http://www.colorpicker.com/ if you want to try out
        # colors and find their RGB values.
        self.player_image     = pygame.image.load("FrontStandard.png")
        self.player_image_front1 = pygame.image.load("FrontWalk1.png")
        self.player_image_front2 = pygame.image.load("FrontWalk2.png")
        self.player_image_back1 = pygame.image.load("BackWalk1.png")
        self.player_image_back2 = pygame.image.load("BackWalk2.png")
        self.player_image_right_standard = pygame.image.load("SideStandard.png")
        self.player_image_right1 = pygame.image.load("SideWalk1.png")
        self.player_image_right2 = pygame.image.load("SideWalk2.png")
        self.player_image_left_standard = pygame.image.load("LeftStandard.png")
        self.player_image_left1 = pygame.image.load("LeftWalk1.png")
        self.player_image_left2 = pygame.image.load("LeftWalk2.png")
        self.image_count      = 0
        self.enemy_image   = pygame.image.load("EnemyFrontStandard.png")
        self.enemy_image_front1 = pygame.image.load("EnemyFront1.png")
        self.enemy_image_front2 = pygame.image.load("EnemyFront2.png")
        self.enemy_image_back1 = pygame.image.load("EnemyBack1.png")
        self.enemy_image_back2 = pygame.image.load("EnemyBack2.png")
        self.enemy_image_back_standard = pygame.image.load("EnemyBackStandard.png")
        self.enemy_image_right_standard = pygame.image.load("EnemyRightStandard.png")
        self.enemy_image_right1 = pygame.image.load("EnemyRight1.png")
        self.enemy_image_right2 = pygame.image.load("EnemyRight2.png")
        self.enemy_image_left_standard = pygame.image.load("EnemyLeftStandard.png")
        self.enemy_image_left1 = pygame.image.load("EnemyLeft1.png")
        self.enemy_image_left2 = pygame.image.load("EnemyLeft2.png")
        self.enemy_image_count = 0
        self.missile_color    = (0, 255, 255)
        self.arrow_image_up   = pygame.image.load("ArrowUp.png")
        self.arrow_image_down = pygame.image.load("ArrowDown.png")
        self.arrow_image_left = pygame.image.load("ArrowLeft.png")
        self.arrow_image_right = pygame.image.load("ArrowRight.png")
        self.fireball_up = pygame.image.load("FireballUp.png")
        self.fireball_down = pygame.image.load("FireballDown.png")
        self.fireball_left = pygame.image.load("FireballLeft.png")
        self.fireball_right = pygame.image.load("FireballRight.png")
        self.npc_image1       = pygame.image.load("NPC1.png")
        self.npc_image2       = pygame.image.load("NPC2.png")
        self.npc_image_count  = 0
        self.wall_image       = pygame.image.load("Wall.png")
        self.text_color       = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.background_image = pygame.image.load("BackgroundV1.png")
        self.game_over_lose = pygame.image.load("LoseScreen.png")
        self.game_over_win = pygame.image.load("VictoryScreen.png")
        self.game_load = pygame.image.load("LoadingScreen.png")
        self.title_image = pygame.image.load("TitleScreen.png")
        self.health_images = [
            pygame.image.load("Health Bar11.png"),
            pygame.image.load("Health Bar10.png"),
            pygame.image.load("Health Bar9.png"),
            pygame.image.load("Health Bar8.png"),
            pygame.image.load("Health Bar7.png"),
            pygame.image.load("Health Bar6.png"),
            pygame.image.load("Health Bar5.png"),
            pygame.image.load("Health Bar4.png"),
            pygame.image.load("Health Bar3.png"),
            pygame.image.load("Health Bar2.png"),
            pygame.image.load("Health Bar1.png"),
        ]
        self.arrows = [
            pygame.image.load("ArrowBar11.png"),
            pygame.image.load("ArrowBar10.png"),
            pygame.image.load("ArrowBar9.png"),
            pygame.image.load("ArrowBar8.png"),
            pygame.image.load("ArrowBar7.png"),
            pygame.image.load("ArrowBar6.png"),
            pygame.image.load("ArrowBar5.png"),
            pygame.image.load("ArrowBar4.png"),
            pygame.image.load("ArrowBar3.png"),
            pygame.image.load("ArrowBar2.png"),
            pygame.image.load("ArrowBar1.png")
        ]
        self.exp = [
            pygame.image.load("ExpBar1.png"),
            pygame.image.load("ExpBar2.png"),
            pygame.image.load("ExpBar3.png"),
            pygame.image.load("ExpBar4.png"),
            pygame.image.load("ExpBar5.png"),
            pygame.image.load("ExpBar6.png"),
            pygame.image.load("ExpBar7.png"),
            pygame.image.load("ExpBar8.png"),
            pygame.image.load("ExpBar9.png"),
            pygame.image.load("ExpBar10.png")
        ]
        self.music = "8bit Adventure Music.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.00)
        return

    def paint_pregame(self, surface, control):
        """
        Draws the display before the user selects the game type.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        #surface.fill(self.background_color, rect)
        surface.blit(self.title_image, rect)
        # text message in center of screen
        #s = "Press 'd' for dual player, 's' for single player,"
        #self.draw_text_center(surface, s, self.text_color,
                              #self.width/2, self.height/2.25,
                             # self.font)
        #s = "'t' for tournament, 'esc' to quit."
        #self.draw_text_center(surface, s, self.text_color,
                             # self.width/2, self.height/2.25 + 3*self.font_size/2,
                              #self.font)
        return
        
    def paint_waiting_for_game(self, surface, engine, control):
        """
        Draws the display after user selects the game type, before the game begins.
        This is usually a brief period of time, while waiting for an opponent
        to join the game.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.blit(self.game_load, rect)
        # text message in center of screen
        #s = "Waiting for an opponent who is willing to get destroyed
        #self.draw_text_center(surface, s, self.text_color,
                             # self.width/2, self.height/2,
                             # self.font)
        return

    def paint_game(self, surface, engine, control):
        """
        Draws the display after the game starts.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.blit(self.background_image, rect)
            
        # draw each object
        objs = engine.get_objects()
        for key in objs:
            obj = objs[key]
            if obj.is_wall():
                self.paint_wall(surface, engine, control, obj)
            elif obj.is_npc():
                self.paint_npc(surface, engine, control, obj)
            elif obj.is_missile():
                self.paint_missile(surface, engine, control, obj)
            elif obj.is_player():
                self.paint_player(surface, engine, control, obj)
            else:
                print "Unexpected object type: %s" % (str(obj.__class__))
                
        # draw game data
        if control.show_info:
            self.paint_game_status(surface, engine, control)
        return

        
    def paint_game_over(self, surface, engine, control):
        """
        Draws the display after the game ends.  This
        chooses to display the game, and add a game over
        message.
        """
        if engine.get_name() == engine.get_winner_name():
            rect = pygame.Rect(0, 0, self.width, self.height)
            surface.blit(self.game_over_win, rect)
        else:
            rect = pygame.Rect(0, 0, self.width, self.height)
            surface.blit(self.game_over_lose, rect)

        s = "Game Over (%s wins!)" % (engine.get_winner_name())
        self.draw_text_center(surface, s, self.text_color, int(self.width/2), int(self.height/2), self.font)
        return

    def process_event(self, surface, engine, control, event):
        """
        Should process the event and decide if it needs to be displayed, or heard.
        """
        import os
        #print(os.getcwd())
        if isinstance(event, MissileFireEvent):
            if event.get_player_oid() == engine.get_player_oid():
                sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'fire.wav'))
                sound.set_volume(0.50)
                sound.play()
            else:
                sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'Fireball+3.wav'))
                sound.set_volume(0.50)
                sound.play()
        return

    # The following methods draw appropriate rectangles
    # for each of the objects, by type.
    # Most objects have an optional text display to
    # demonstrate how to send information from the control
    # to the display.
    def paint_wall(self, surface, engine, control, obj):
        """
        Draws walls.
        """
        rect = self.obj_to_rect(obj)
        #pygame.draw.rect(surface, self.wall_color, rect)
        surface.blit(self.wall_image, rect)
        return

    def paint_npc(self, surface, engine, control, obj):
        """
        Draws living NPCs.
        """
        if obj.is_alive():
            #color = self.npc_color
            #rect = self.obj_to_rect(obj)
            #pygame.draw.rect(surface, color, rect)
            if self.npc_image_count <= 5:
                surface.blit(self.npc_image1, (obj.get_px(), obj.get_py()))
                self.npc_image_count += 1
            elif 5 < self.npc_image_count <= 9:
                surface.blit(self.npc_image2, (obj.get_px(), obj.get_py()))
                self.npc_image_count += 1
                if self.npc_image_count > 9:
                    self.npc_image_count = 0
        return
        
    def paint_missile(self, surface, engine, control, obj):
        """
        Draws living missiles.
        """
        if obj.is_alive():
            if obj.get_player_oid() == engine.get_player_oid():
                rect = self.obj_to_rect(obj)
                if obj.get_dx() <= 0:
                        if abs(obj.get_dx()) > abs(obj.get_dy()):
                            # facing left image
                            surface.blit(self.arrow_image_left, rect)
                        else:
                            # facing up image
                            surface.blit(self.arrow_image_up, rect)
                elif obj.get_dx > 0:
                        if abs(obj.get_dx()) > abs(obj.get_dy()):
                            # facing right image
                            surface.blit(self.arrow_image_right, rect)
                        else:
                            # facing down image
                            surface.blit(self.arrow_image_down, rect)
            else:
                rect = self.obj_to_rect(obj)
                if obj.get_dx() <= 0:
                        if abs(obj.get_dx()) > abs(obj.get_dy()):
                            # facing left image
                            surface.blit(self.fireball_left, rect)
                        else:
                            # facing up image
                            surface.blit(self.fireball_up, rect)
                elif obj.get_dx > 0:
                        if abs(obj.get_dx()) > abs(obj.get_dy()):
                            # facing right image
                            surface.blit(self.fireball_right, rect)
                        else:
                            # facing down image
                            surface.blit(self.fireball_down, rect)
        return
        
    def paint_player(self, surface, engine, control, obj):
        """
        Draws living players.
        My player is my opponent are in different colors
        """
        if obj.is_alive():
            rect = self.obj_to_rect(obj)
            if obj.get_oid() == engine.get_player_oid():
                if obj.get_dx() <= 0:
                    if abs(obj.get_dx()) > abs(obj.get_dy()):
                        # facing left image
                        if self.image_count <= 4:
                            surface.blit(self.player_image_left1, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 4 < self.image_count <= 9:
                            self.image_count += 1
                            surface.blit(self.player_image_left_standard, (obj.get_px(), obj.get_py()))
                        elif 9 < self.image_count <= 14:
                            surface.blit(self.player_image_left2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 14 < self.image_count <= 19:
                            self.image_count += 1
                            surface.blit(self.player_image_left_standard, (obj.get_px(), obj.get_py()))
                        if self.image_count > 19:
                            self.image_count = 0
                    else:
                        # facing up image
                        if self.image_count <= 5:
                            surface.blit(self.player_image_back1, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 5 < self.image_count <= 10:
                            surface.blit(self.player_image_back2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif self.image_count > 10:
                            self.image_count = 0
                            surface.blit(self.player_image_back1, (obj.get_px(), obj.get_py()))
                        #elif self.image_count == 0:
                            #surface.blit(self.player_image_back_standard, (obj.get_px(), obj.get_py()))
                elif obj.get_dx() > 0:
                    if abs(obj.get_dx()) > abs(obj.get_dy()):
                        # facing right image                        
                        if self.image_count <= 4:
                            surface.blit(self.player_image_right1, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 4 < self.image_count <= 9:
                            self.image_count += 1
                            surface.blit(self.player_image_right_standard, (obj.get_px(), obj.get_py()))
                        elif 9 < self.image_count <= 14:
                            surface.blit(self.player_image_right2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 14 < self.image_count <= 19:
                            self.image_count += 1
                            surface.blit(self.player_image_right_standard, (obj.get_px(), obj.get_py()))
                        if self.image_count > 19:
                            self.image_count = 0
                    else:
                        # facing down image
                        if self.image_count <= 5:
                            surface.blit(self.player_image_front1, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 5 < self.image_count <= 10:
                            surface.blit(self.player_image_front2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif self.image_count > 10:
                            self.image_count = 0
                            surface.blit(self.player_image_front1, (obj.get_px(), obj.get_py()))
                else:
                    surface.blit(self.player_image, (obj.get_px(), obj.get_py()))
            else:
                #color = self.opponent_color
                #pygame.draw.rect(surface, color, rect)
                if obj.get_dx() <= 0:
                    if abs(obj.get_dx()) > abs(obj.get_dy()):
                        # facing left image
                        if self.enemy_image_count <= 4:
                            surface.blit(self.enemy_image_left1, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif 4 < self.enemy_image_count <= 9:
                            self.enemy_image_count += 1
                            surface.blit(self.enemy_image_left_standard, (obj.get_px(), obj.get_py()))
                        elif 9 < self.enemy_image_count <= 14:
                            surface.blit(self.enemy_image_left2, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif 14 < self.enemy_image_count <= 19:
                            self.enemy_image_count += 1
                            surface.blit(self.enemy_image_left_standard, (obj.get_px(), obj.get_py()))
                        if self.enemy_image_count > 19:
                            self.enemy_image_count = 0
                    else:
                        # facing up image
                        if self.enemy_image_count <= 5:
                            surface.blit(self.enemy_image_back1, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif 5 < self.enemy_image_count <= 10:
                            surface.blit(self.enemy_image_back2, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif self.enemy_image_count > 10:
                            self.enemy_image_count = 0
                            surface.blit(self.enemy_image_back1, (obj.get_px(), obj.get_py()))
                        #elif self.enemy_image_count == 0:
                            #surface.blit(self.enemy_image_back_standard, (obj.get_px(), obj.get_py()))
                elif obj.get_dx > 0:
                    if abs(obj.get_dx()) > abs(obj.get_dy()):
                        # facing right image                        
                        if self.enemy_image_count <= 4:
                            surface.blit(self.enemy_image_right1, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif 4 < self.enemy_image_count <= 9:
                            self.enemy_image_count += 1
                            surface.blit(self.enemy_image_right_standard, (obj.get_px(), obj.get_py()))
                        elif 9 < self.enemy_image_count <= 14:
                            surface.blit(self.enemy_image_right2, (obj.get_px(), obj.get_py()))
                            self.image_count += 1
                        elif 14 < self.enemy_image_count <= 19:
                            self.enemy_image_count += 1
                            surface.blit(self.enemy_image_right_standard, (obj.get_px(), obj.get_py()))
                        if self.enemy_image_count > 19:
                            self.enemy_image_count = 0
                    else:
                        # facing down image
                        if self.enemy_image_count <= 5:
                            surface.blit(self.enemy_image_front1, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif 5 < self.enemy_image_count <= 10:
                            surface.blit(self.enemy_image_front2, (obj.get_px(), obj.get_py()))
                            self.enemy_image_count += 1
                        elif self.enemy_image_count > 10:
                            self.enemy_image_count = 0
                            surface.blit(self.enemy_image_front1, (obj.get_px(), obj.get_py()))
                else:
                    surface.blit(self.enemy_image, (obj.get_px(), obj.get_py()))
        return

    def get_health_image(self, health):
        health = health / 3.0
        return self.health_images[int(math.ceil(health))]

    def get_arrow_image(self, missile_mana):
        if missile_mana > 10.0:
            missile_mana = 10.0
        return self.arrows[int(math.floor(missile_mana))]

    def get_exp(self, experience):
        experience = experience / 4.5
        i = int(math.ceil(experience))
        if i < 0:
            i = 0
        elif i >= len(self.exp):
            i = len(self.exp) - 1
        return self.exp[i]

    def paint_game_status(self, surface, engine, control):
        """
        This method displays some text in the bottom strip
        of the screen.  You can make it do whatever you want,
        or nothing if you want.
        """

        # display my stats
        oid = engine.get_player_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                s = "Me: %s  HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_name(),
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                position_x = 20
                position_y = self.height - STATUS_BAR_HEIGHT + 3 * self.font_size / 2
                #self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
                image = self.get_health_image(obj.get_health())
                surface.blit(image, (0, surface.get_height() - 50))
                image = self.get_arrow_image(obj.get_missile_mana())
                surface.blit(image, (100, surface.get_height() - 50))
                image = self.get_exp(obj.get_experience())
                surface.blit(image, (130, surface.get_height() - 50))
        # display opponent's stats
        oid = engine.get_opponent_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                s = "Opponent: %s  HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_opponent_name(),
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                position_x = 20
                position_y = self.height - STATUS_BAR_HEIGHT + 6 * self.font_size / 2
                #self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
                image = self.get_health_image(obj.get_health())
                surface.blit(image, (surface.get_width() - 108, surface.get_height() - 50))
                image = self.get_arrow_image(obj.get_missile_mana())
                surface.blit(image, (surface.get_width() - 155, surface.get_height() - 50))
                image = self.get_exp(obj.get_experience())
                surface.blit(image, (surface.get_width() - 200, surface.get_height() - 50))
        return

