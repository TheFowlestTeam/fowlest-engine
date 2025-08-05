# fowlest/node/display/sprite.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage, Skinned, Avery

import pygame

from ..base import FSTBaseNode
from ...math import Vec2

class FSTSpriteNode(FSTBaseNode):
    def __init__(self, image_path: str):
        super().__init__()
        
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        
        self.type_name = "Sprite"
        
        self.set_size(Vec2(self.image.get_width(), self.image.get_height()))
        
    def _draw(self, surface, camera):
        pos = (self.get_position().x - self.offset.x - camera.get_position().x, self.get_position().y - self.offset.y - camera.get_position().y)
        surface.blit(self.image, pos)