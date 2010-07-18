import pygame
from helpers import load_image
from fish import *

class Boat(pygame.sprite.Sprite):
    """The boats that will represent the player and the computer"""
    
    def __init__(self, position, images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0
        
        # Attributes of the boat
        self.is_alive = True
        self.value_collected = 0
        
    def update(self, screen):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        t = pygame.time.get_ticks()
        
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t
            self.sprites = pygame.sprite.RenderPlain((self))
        
        self.sprites.draw(screen)
        
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
