# fowlest/core/utils.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage, Skinned, Avery

import pygame
import os
import platform

def prRed(s):    print("\033[91m{}\033[00m".format(s))
def prYellow(s): print("\033[93m{}\033[00m".format(s))
def prCyan(s):   print("\033[96m{}\033[00m".format(s))
def prGray(s):   print("\033[90m{}\033[00m".format(s))

class FSTUtils:
    # Printing
    def print_info(text: str = ""):    prCyan("[INFO] - " + text)
    def print_warning(text: str = ""): prYellow("[WARN] - " + text)
    def print_error(text: str = ""):   prRed("[FAIL] - " + text)
    def print_spacer():                prGray("[BRKL] - ----------------------------")
    
    # Game Info (like FlxG in Flixel or som)
    def get_game_width():  return pygame.display.get_window_size()[0]
    def get_game_height(): return pygame.display.get_window_size()[1]
    def get_game_title():  return pygame.display.get_caption()
    
    def set_game_title(title: str): pygame.display.set_caption(title)
    def set_game_icon(path: str):
        icon = pygame.image.load(path)
        pygame.display.set_icon(icon)
        
    def get_platform(): return platform.system()
    
    # Miscellaneous
    def get_game_dir(): return os.getcwd()