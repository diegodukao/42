#! /usr/bin/env python

import sys
import pygame
from helpers import *

class Game:
    """The Main Game Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=800, height=600):
        """Initialize PyGame"""
        pygame.init
        
        """Set the window size"""
        self.width = width
        self.height = height
        
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        """Create the background"""
        self.bg, self.bg_rect = load_image("ocean.jpg")
        self.bg = self.bg.convert()
    
    def load_sprites(self):
        """Load the sprites that we need"""
        self.player_boat = Boat([60, 300])
        self.player_boat_sprites = pygame.sprite.RenderPlain((self.player_boat))
    
    def main(self):
        """Load all of our sprites"""
        self.load_sprites()
        
        """This is the Main Loop of the game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if (event.key == K_RETURN):
                        self.player_boat.throw_hook()
            
            self.screen.blit(self.bg, self.bg_rect)
            self.player_boat_sprites.draw(self.screen)
            pygame.display.flip()


class Boat(pygame.sprite.Sprite):
    """The boats that will represent the player and the computer"""
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('paper_boat.jpg')
        self.rect.topleft = position
        self.value_collected = 0
        
    def throw_hook(self):
        fish = Fish()
        self.value_collected += fish.value
        print(self.value_collected)


class Fish(pygame.sprite.Sprite):
    """The values that the player and the computer will fish"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('coin.png')
        self.value = 10


if __name__ == "__main__":
    game_window = Game()
    game_window.main()

