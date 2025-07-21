import pygame

from ..base import FSTBaseNode
from ...math import Vec2

class FSTSpriteNode(FSTBaseNode):
    def __init__(self, image_path: str):
        super().__init__()
        
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        
        self.set_size(Vec2(self.image.get_width(), self.image.get_height()))
        
    def _draw(self):
        self.surface.blit(self.image.convert_alpha(), (self.dimensions.position.x, self.dimensions.position.y))