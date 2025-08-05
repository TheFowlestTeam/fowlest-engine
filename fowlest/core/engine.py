# fowlest/core/engine.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage, Skinned, Avery

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys

from .utils import FSTUtils
from ..node import FSTBaseNode, FSTCameraNode
from .config import FSTConfig
from ..display.layer import FSTLayer

from ..math import Vec2

import time

class FSTEngine:
    def __init__(self, config: FSTConfig):
        FSTUtils.print_info("FowlestEngine I - 2025 (C) The Fowlest Team - FowluhhDev, GamerGage, Skinned, Avery")
        
        # Window meta
        if config:
            self.width  = config.width
            self.height = config.height
            self.title  = config.title
        else:
            FSTUtils.print_warning("Using default config as none was given.")
            self.width = 640
            self.height = 480
            self.title = "Game"
        self.screen: pygame.Surface
        
        self.layers: list[FSTLayer] = []
        
        self.dt = 0
        self._dtimes = [time.time(), 0]
        
        self.fps = 0
        
        self.camera: FSTCameraNode = FSTCameraNode()
        
    def add(self, list: list, node: FSTBaseNode):
        list.append(node)
        node._ready()
        FSTUtils.print_info("Added node. Type is {}, Layer is {}.".format(node.type_name, node.layer))
        
    def add_layer(self, layer: FSTLayer):
        self.layers.append(layer)
        FSTUtils.print_info("Added layer.")
        
    def start(self):
        FSTUtils.print_info("Creating game with dimensions of %sx%s and a title of %s" %(self.width, self.height, self.title))
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        # Title
        pygame.display.set_caption(self.title)
        
        # How many calories we burning today? "No clue"
        self.running = True
        
        FSTUtils.print_spacer()
        
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
            if node.layer != None:
                node._draw(self.layers[node.layer].surface, self.camera)
            else:
                node._draw(self.screen, self.camera)
                
        for layer in self.layers:
            self.screen.blit(layer.surface, (0, 0))
            
        pygame.display.flip()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
    def quit(self):
        # say the funny
        FSTUtils.print_spacer()
        FSTUtils.print_info("\"Peace to the world, and my mind\" -FowluhhDev 2025")
        FSTUtils.print_info("Exiting FowlestEngine, goodbye!")
        pygame.quit()
        sys.exit()
    
    def is_running(self):
        return self.running
    
    def get_current_camera(self):
        return self.camera
    
    def set_current_camera(self, camera: FSTCameraNode):
        self.camera = camera
        
