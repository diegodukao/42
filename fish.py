import pygame
import random
from helpers import load_image

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

