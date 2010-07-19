#! /usr/bin/env python

import sys
import pygame
import random
from boat import *
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
        
        self.game_running = True
    
    def main(self):
        self.create_game_itens()
        #self.initialize_sounds()
        self.initialize_text()
        
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
        
        player_images = load_animation_sprites(player_frames_names)
        computer_images = load_animation_sprites(computer_frames_names)
        
        self.player = Boat([35, 300], player_images)
        self.player_sprites = pygame.sprite.RenderPlain((self.player))
        self.computer = Boat([450, 300], computer_images)
        self.computer_sprites = pygame.sprite.RenderPlain((self.computer))
        self.fish_sprites = pygame.sprite.Group()
        
    def initialize_sounds(self):
        pygame.mixer.init()
        pygame.mixer.music.load("data/sounds/bg_music.wav")
        pygame.mixer.music.play(-1)
        
    def initialize_text(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        
    def update_screen(self):
        """Show the sprites and update the display"""
        self.screen.blit(self.bg, self.bg_rect)
        
        if self.player.is_alive:
            self.player.update(self.screen)
        if self.computer.is_alive:
            self.computer.update(self.screen)
        
        self.fish_sprites.draw(self.screen)
        self.player.show_weight(self, [35, 10])
        
        if not self.game_running:
            self.computer.show_weight(self, [450, 10])
            text = self.font.render(self.final_text, 1, (255, 30, 0))
            self.screen.blit(text, [360, 150])
        
        pygame.display.flip()
        
    def key_handler(self, key):
        if key == K_RETURN:
            if self.game_running:
                if self.player.is_alive:
                    player_fish = self.player.throw_hook()
                    self.fish_sprites.empty()
                    self.fish_sprites.add(player_fish)
                    
                    if not self.player.is_alive:
                        self.finish_game()
                if self.computer.is_alive:
                    self.computer.throw_hook()
            else:
                self.restart_game()
        elif key == K_BACKSPACE:
            if self.game_running:
                self.finish_game()
            else:
                sys.exit()
        
    def finish_game(self):
        if not self.player.is_alive:
            self.final_text = "You are dead!"
        elif (not self.computer.is_alive
                or self.player.value_collected > self.computer.value_collected):
            self.final_text = "You win!"
        elif self.player.value_collected < self.computer.value_collected:
            self.final_text = "You lose!"
        else:
            self.final_text = "Draw"
        
        self.game_running = False
            
    def restart_game(self):
        del self.player
        del self.player_sprites
        del self.computer
        del self.computer_sprites
        self.create_game_itens()
        self.game_running = True

if __name__ == "__main__":
    game_window = Game()
    game_window.main()

