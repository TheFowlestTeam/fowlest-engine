# fowlest/node/base.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage, Skinned, Avery

from ..core import Rect
from ..core import Vec2
from ..core import FSTSignal

class FSTBaseNode:
    def __init__(self):
        self.dimensions: Rect = Rect(Vec2(0, 0), Vec2(0, 0))
        
        self.layer: None | int = None
        
        self.owner = None
        self.surface = None
        
        self.camera = None
        
        self.type_name = "Base"
        
        self.offset: Vec2 = Vec2(0, 0)
    
    def _ready(self):
        pass
    
    def _draw(self, surface, camera):
        pass
    
    def _update(self):
        pass
    
    def set_position(self, position: Vec2):
        self.dimensions.position = position
    
    def set_size(self, size: Vec2):
        self.dimensions.size = size
    
    def get_position(self):
        return self.dimensions.position
    
    def get_size(self):
        return self.dimensions.size
    
    def define_signal(self, name):
        self.signals[name] = FSTSignal()

    def connect_signal(self, signal_name, callback):
        if signal_name in self.signals:
            self.signals[signal_name].connect(callback)

    def emit_signal(self, signal_name, *args, **kwargs):
        if signal_name in self.signals:
            self.signals[signal_name].emit(*args, **kwargs)
        
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