# fowlest/core/utils.py
# Part of FowlestEngine
# Created July 20th, 2025
# 2025 (C) The Fowlest Team, FowluhhDev, GamerGage

import pygame

def prRed(s): print("\033[91m{}\033[00m".format(s))
def prYellow(s): print("\033[93m{}\033[00m".format(s))
def prCyan(s): print("\033[96m{}\033[00m".format(s))

class FSTUtils:
    def print_info(text: str = ""):
        prCyan("[INFO] - " + text)
        
    def print_warning(text: str = ""):
        prYellow("[WARN] - " + text)
        
    def print_error(text: str = ""):
        prRed("[ERROR] - " + text)