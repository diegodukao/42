#! /usr/bin/env python

import sys
import pygame
import random
from boat import *
from possiblevalues import *
from helpers import *

class Game:
    """The Main Game Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=800, height=600):
        """Initialize the game screen"""
        pygame.init()
        
        #Set the window size
        self.width = width
        self.height = height
        
        #Create the Screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        #Create the background
        self.bg, self.bg_rect = load_image("bg.jpg")
        self.bg = self.bg.convert()
        
        self.inicial_instructions_text = [
            "RETURN: Catch a fish",
            "BACKSPACE: Stop fishing"
        ]
        
        self.final_instructions_text = "Hit Return to start a new game or Backspace to quit."
        
        self.game_running = True
    
    def main(self):
        self.create_game_itens()
#        self.initialize_sounds()
        self.initialize_text()
        
        self.player.throw_hook(self.possible_values.list)
        self.computer.throw_hook(self.possible_values.list)
        
        #This is the Main Loop of the game
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYUP:
                    self.key_handler(event.key)
            
            self.update_screen()
    
    def create_game_itens(self):
        """Load the sprites that we need"""
        
        player_frames_names = [
            "boat_frame1.png",
            "boat_frame2.png",
            "boat_frame3.png",
            "boat_frame4.png",
            "boat_frame5.png",
            "boat_frame6.png",
            "boat_frame7.png",
            "boat_frame8.png",
            "boat_frame9.png",
            "boat_frame10.png",
            "boat_frame11.png",
            "boat_frame10.png",
            "boat_frame9.png",
            "boat_frame8.png",
            "boat_frame7.png",
            "boat_frame6.png",
            "boat_frame5.png",
            "boat_frame4.png",
            "boat_frame3.png",
            "boat_frame2.png"
        ]
        
        player_sink_frames_names = [
            "sink_frame1.png",
            "sink_frame2.png",
            "sink_frame3.png",
            "sink_frame4.png",
            "sink_frame5.png",
            "sink_frame6.png",
            "sink_frame7.png",
            "sink_frame8.png",
            "sink_frame9.png",
            "sink_frame10.png",
            "sink_frame11.png",
            "sink_frame12.png",
            "sink_frame13.png"
        ]
        
        computer_frames_names = [
            "boat2_frame1.png",
            "boat2_frame2.png",
            "boat2_frame3.png",
            "boat2_frame4.png",
            "boat2_frame5.png",
            "boat2_frame6.png",
            "boat2_frame7.png",
            "boat2_frame8.png",
            "boat2_frame9.png",
            "boat2_frame10.png",
            "boat2_frame11.png",
            "boat2_frame10.png",
            "boat2_frame9.png",
            "boat2_frame8.png",
            "boat2_frame7.png",
            "boat2_frame6.png",
            "boat2_frame5.png",
            "boat2_frame4.png",
            "boat2_frame3.png",
            "boat2_frame2.png"
        ]
        
        computer_sink_frames_names = [
            "sink2_frame1.png",
            "sink2_frame2.png",
            "sink2_frame3.png",
            "sink2_frame4.png",
            "sink2_frame5.png",
            "sink2_frame6.png",
            "sink2_frame7.png",
            "sink2_frame8.png",
            "sink2_frame9.png",
            "sink2_frame10.png",
            "sink2_frame11.png",
            "sink2_frame12.png",
            "sink2_frame13.png"
        ]
        
        player_images = load_animation_sprites(player_frames_names)
        player_sink_images = load_animation_sprites(player_sink_frames_names)
        computer_images = load_animation_sprites(computer_frames_names)
        computer_sink_images = load_animation_sprites(computer_sink_frames_names)
        
        self.player = Boat([35, 300], player_images, player_sink_images)
        self.player_sprites = pygame.sprite.RenderPlain((self.player))
        self.computer = Boat([450, 300], computer_images, computer_sink_images)
        self.computer_sprites = pygame.sprite.RenderPlain((self.computer))
        self.fish_sprites = pygame.sprite.Group()
        
        self.possible_values = PossibleValues()
        
    def initialize_sounds(self):
        pygame.mixer.init()
        pygame.mixer.music.load("data/sounds/bg_music.wav")
        pygame.mixer.music.play(-1)
        
    def initialize_text(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.font_instructions = pygame.font.Font(None, 23)
        
        self.inicial_instructions = []
        self.inicial_instructions.append(self.font_instructions.render(
            self.inicial_instructions_text[0],
            1,
            (0, 0, 0)
        ))
        self.inicial_instructions.append(self.font_instructions.render(
            self.inicial_instructions_text[1],
            1,
            (0, 0, 0)
        ))
        
        self.final_instructions = self.font.render(
            self.final_instructions_text,
            1,
            (255, 102, 0)
        )
        
    def update_screen(self):
        """Show the sprites and update the display"""
        self.screen.blit(self.bg, self.bg_rect)
        
        self.player.update(self.screen)
        self.computer.update(self.screen)
        
        self.fish_sprites.draw(self.screen)
        self.player.show_weight(self, [35, 10])
        self.player.show_value(self, [35, 35])
        
        self.computer.show_weight(self, [530, 10])
        self.computer.show_value(self, [530, 35])
        
        if self.game_running:
            self.screen.blit(self.inicial_instructions[0], [280, 10])
            self.screen.blit(self.inicial_instructions[1], [280, 30])
        else:
            self.screen.blit(self.result_text, [280, 130])
            self.screen.blit(self.final_instructions, [50, 160])
        
        pygame.display.flip()
        
    def key_handler(self, key):
        if key == K_RETURN:
            if self.game_running:
                if not self.player.is_sinking:
                    player_fish = self.player.throw_hook(self.possible_values.list)
                    self.fish_sprites.empty()
                    self.fish_sprites.add(player_fish)
                    
                    if self.player.is_sinking:
                        self.finish_game()
                #if not self.computer.is_sinking:
                    #self.computer.throw_hook(self.possible_values.list)
            else:
                self.restart_game()
        elif key == K_BACKSPACE:
            if self.game_running:
                self.finish_game()
            else:
                sys.exit()
        
    def finish_game(self):
        if self.player.is_sinking:
            self.final_text = "You are dead!"
        else:
            while self.computer.value_collected <= self.player.value_collected:
                self.computer.throw_hook(self.possible_values.list)
        
        if (self.computer.is_sinking
                or self.player.value_collected > self.computer.value_collected):
            self.final_text = "You win!"
        elif self.player.value_collected < self.computer.value_collected:
            self.final_text = "You lose!"
        else:
            self.final_text = "Draw"
        
        self.result_text = self.font.render(self.final_text, 1, (255, 30, 0))
        
        self.game_running = False
            
    def restart_game(self):
        del self.player
        del self.player_sprites
        del self.computer
        del self.computer_sprites
        del self.possible_values
        self.create_game_itens()
        self.game_running = True

if __name__ == "__main__":
    game_window = Game()
    game_window.main()

