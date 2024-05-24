#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programmer: Bruce Provencher
# Date: 01 JAN 2016
# Project: Generic

# http://www.linuxuser.co.uk/tutorials/make-a-game-on-raspberry-pi

import random # For generating random positions for ball
import pygame # Provides tools for making the game
import sys    # For sys.exit function for closing the script

from pygame.locals import *
from pygame import *

def main():
    # Main game class
    class PiPong():
        
        def __init__(self):
            
            # Make display size a member of this class
            self.display_size = (640, 480)

if __name__ == '__main__':
	main()
