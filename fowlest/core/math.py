class Vec2:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y
        
    def add_vec(self, vec):
        self.x += vec.x
        self.y += vec.y

class Rect:
    def __init__(self, position: Vec2, size: Vec2):
        self.position = position
        self.size = size