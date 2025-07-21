# fowlest/node/display/sprite.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage

import pygame

from ..base import FSTBaseNode
from ...math import Vec2

class FSTSpriteNode(FSTBaseNode):
    def __init__(self, image_path: str):
        super().__init__()
        
        self.rotation: float = 0
        
        self.pivot: Vec2 = Vec2(0, 0)
        
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        
        self.type_name = "Sprite"
        
        self.set_size(Vec2(self.image.get_width(), self.image.get_height()))
        
    def _draw(self):
        image_rect = self.image.get_rect(topleft = (self.get_position().x - (self.get_size().x * self.pivot.x), self.get_position().y - (self.get_size().y * self.pivot.y)))
        offset_center_to_pivot = pygame.math.Vector2((self.get_position().x, self.get_position().y)) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-self.rotation)
        rotated_image_center = (self.get_position().x - rotated_offset.x, self.get_position().y - rotated_offset.y)
        
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rotated_image_rect = rotated_image.get_rect(center = (rotated_image_center[0], rotated_image_center[1]))

        offset_rect = rotated_image_rect.copy()
        offset_rect.top = -self.offset[1]
        offset_rect.left = -self.offset[0]
        
        self.surface.blit(rotated_image, rotated_image_rect)