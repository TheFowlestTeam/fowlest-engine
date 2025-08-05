# fowlest/math/rect.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage, Skinned, Avery

from .vec2 import Vec2

class Rect:
    def __init__(self, position: Vec2, size: Vec2):
        self.position = position
        self.size = size