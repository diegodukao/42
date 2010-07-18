#! /usr/bin/env python

import sys
import pygame
import random
from helpers import *

class Game:
    """The Main Game Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=800, height=600):
        """Initialize the game screen"""
        pygame.init
        
        #Set the window size
        self.width = width
        self.height = height
        
        #Create the Screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        #Create the background
        self.bg, self.bg_rect = load_image("ocean.jpg")
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
        self.player = Boat([35, 300], 'paper_boat.jpg')
        self.player_sprites = pygame.sprite.RenderPlain((self.player))
        self.computer = Boat([450, 300], 'paper_boat.jpg')
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
            self.player_sprites.draw(self.screen)
        if self.computer.is_alive:
            self.computer_sprites.draw(self.screen)
        
        self.fish_sprites.draw(self.screen)
        
        self.player.show_weight(self, [35, 10])
        if not self.game_running:
            self.computer.show_weight(self, [450, 10])
        
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
        self.game_running = False
        
        if not self.player.is_alive:
            print("You are dead!")
        elif (not self.computer.is_alive
                or self.player.value_collected > self.computer.value_collected):
            print("You win!")
        elif self.player.value_collected < self.computer.value_collected:
            print("You lose!")
        else:
            print("Draw")
            
    def restart_game(self):
        del self.player
        del self.player_sprites
        del self.computer
        del self.computer_sprites
        self.create_game_itens()
        self.game_running = True

class Boat(pygame.sprite.Sprite):
    """The boats that will represent the player and the computer"""
    
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image)
        self.rect.topleft = position
        self.is_alive = True
        self.value_collected = 0
        
    def throw_hook(self):
        """Get a fish (and a value)"""
        fish = Fish([40, 80])
        self.value_collected += fish.value
        if self.value_collected > 42:
            self.sink()
            
        return fish
            
    def sink(self):
        """Sink the boat when the value is greater than 42"""
        self.is_alive = False
    
    def show_weight(self, game, position):
        percent = str((self.value_collected * 100) / 42) + "%"
        text = game.font.render("Weight %s" % percent, 1, (255, 0, 0))
        game.screen.blit(text, position)

possible_values = [
                    1, 1, 1, 1,
                    2, 2, 2, 2,
                    6, 6, 6, 6,
                    8, 8, 8, 8,
                    10, 10, 10, 10,
                    12, 12, 12, 12,
                    14, 14, 14, 14,
                    16, 16, 16, 16,
                    18, 18, 18, 18,
                    20, 20, 20, 20,
                    21
]


class Fish(pygame.sprite.Sprite):
    """The values that the player and the computer will fish"""
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('coin.png')
        self.rect.topleft = position
        
        #getting a value randomically
        key_value = random.randint(0, len(possible_values) - 1)
        self.value = possible_values.pop(key_value)


if __name__ == "__main__":
    game_window = Game()
    game_window.main()

