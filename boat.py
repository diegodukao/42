import pygame
from helpers import load_image
from fish import *

class Boat(pygame.sprite.Sprite):
    """The boats that will represent the player and the computer"""
    
    def __init__(self, position, idle_images, sink_images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = idle_images
        self.image = idle_images[0]
        self.sink_images = sink_images
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
        self.is_sinking = False
        self.value_collected = 0
        
    def update(self, screen):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        t = pygame.time.get_ticks()
        
        if t - self._last_update > self._delay:
            if self.is_alive:
                self.image = self._images[self._frame]
                self._last_update = t
                self.sprites = pygame.sprite.RenderPlain((self))
                self._frame += 1
            if self._frame >= len(self._images):
                if self.is_sinking:
                    self.is_alive = False
                else:
                    self._frame = 0
        
        self.sprites.draw(screen)
        
    def throw_hook(self, possible_values):
        """Get a fish (and a value)"""
        fish = Fish([40, 80], possible_values)
        self.value_collected += fish.value
        if self.value_collected > 42:
            self.sink()
            
        return fish
            
    def sink(self):
        """Sink the boat when the value is greater than 42"""
        self._frame = 0
        self._images = self.sink_images
        self.is_sinking = True
    
    def show_weight(self, game, position):
        percent = str((self.value_collected * 100) / 42) + "%"
        text = game.font.render("Weight %s" % percent, 1, (255, 0, 0))
        game.screen.blit(text, position)
        
    def show_value(self, game, position):
        color = (255, 0, 0)
        text = game.font.render("Value: %i" % self.value_collected, 1, color)
        game.screen.blit(text, position)
