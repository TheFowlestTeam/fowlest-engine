# fowlest/core/engine.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys

from .utils import FSTUtils
from ..node import FSTBaseNode, FSTCameraNode

from ..math import Vec2

import time

class FSTEngine:
    def __init__(self, width: int = 640, height: int = 480):
        FSTUtils.print_info("FowlestEngine I - 2025 (C) The Fowlest Team, FowluhhDev, GamerGage")
        
        # Window meta
        self.width = width
        self.height = height
        self.screen: pygame.Surface
        self.title = "Game"
        
        self.dt = 0
        self._dtimes = [time.time(), 0]
        
        self.fps = 0
        
        self.camera: FSTCameraNode = FSTCameraNode()
        
    def add(self, list: list, node: FSTBaseNode):
        node.surface = self.screen
        list.append(node)
        FSTUtils.print_info("Added node. Type is {}.".format(node.type_name))
        
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
        
        self._dtimes[1] = time.time()
        self.dt = self._dtimes[1] - self._dtimes[0]
        self._dtimes[0] = self._dtimes[1]
        
        self.fps = 1000 / self.dt
    
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
        # say the funny
        FSTUtils.print_info("\"Peace to the world, and my mind\" -FowluhhDev 2025")
        FSTUtils.print_info("Exiting Fowlest Engine, goodbye!")
        pygame.quit()
        sys.exit()
    
    def is_running(self):
        return self.running
        
