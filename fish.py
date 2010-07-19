import pygame
import random
from helpers import load_image

class Fish(pygame.sprite.Sprite):
    """The values that the player and the computer will fish"""
    
    def __init__(self, position, possible_values):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('coin.png')
        self.rect.topleft = position
        
        #getting a value randomically
        key_value = random.randint(0, len(possible_values) - 1)
        self.value = possible_values.pop(key_value)
