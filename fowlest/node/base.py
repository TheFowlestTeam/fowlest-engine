# fowlest/node/base.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage

from ..math.rect import Rect
from ..math.vec2 import Vec2

class FSTBaseNode:
    def __init__(self):
        self.dimensions: Rect = Rect(Vec2(0, 0), Vec2(0, 0))
        
        self.owner = None
        self.surface = None
        
    def _draw(self):
        pass
    
    def _update(self):
        pass
    
    def set_position(self, position: Vec2):
        self.dimensions.position = position
    
    def set_size(self, size: Vec2):
        self.dimensions.size = size
        
    def get_horizontal_align_position(self, width: int = 640, align: int = 0):
        match align:
            case 0:
                return 0
            case 1:
                return (width - self.dimensions.size.x) / 2
            case 2:
                return width - self.dimensions.size.x
            case _:
                return 0
    
    def get_vertical_align_position(self, height: int = 480, align: int = 0):
        match align:
            case 0:
                return 0
            case 1:
                return (height - self.dimensions.size.y) / 2
            case 2:
                return height - self.dimensions.size.y
            case _:
                return 0