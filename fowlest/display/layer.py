import pygame
from ..core.utils import FSTUtils

class FSTLayer:
    def __init__(self):
        self.surface: pygame.Surface = pygame.Surface((FSTUtils.get_game_width(), FSTUtils.get_game_height()), pygame.SRCALPHA)