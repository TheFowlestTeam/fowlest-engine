# fowlest/math/vec2.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage, Skinned, Avery

class Vec2:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y
        
    def add_vec(self, vec):
        self.x += vec.x
        self.y += vec.y