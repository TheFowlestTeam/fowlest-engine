# fowlest/core/engine.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys

from .utils import FSTUtils
from ..node.base import FSTBaseNode

class FSTEngine:
    def __init__(self, width: int = 640, height: int = 480):
        print("FowlestEngine I - 2025 (C) The Fowlest Team, FowluhhDev, GamerGage")
        
        # Window meta
        self.width = width
        self.height = height
        self.screen: pygame.Surface
        self.title = "Game"
        
    def add(self, list, node: FSTBaseNode):
        node.surface = self.screen
        list.append(node)
        print("Node added!")
        
    def start(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        # Title
        pygame.display.set_caption(self.title)
        
        # How many calories we burning today? "No clue"
        self.running = True
        
    def update(self, nodes):
        for node in nodes:
            node._update()
    
    def draw(self, nodes):
        self.screen.fill((0, 0, 0))
        
        for node in nodes:
            node._draw()
            
        pygame.display.flip()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
    def quit(self):
        # "Peace to the world, and my mind" -FowluhhDev 2025
        pygame.quit()
        sys.exit()
    
    def is_running(self):
        return self.running
