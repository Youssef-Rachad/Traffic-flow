## This is taken from https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f tutorial but will be modified for this projects purposes

import pygame
from pygame import gfxdraw
import numpy as np

class Window:
    def __init__(self, sim, config={}):
        self.sim = sim # Simulation to visualize
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val) # Take all config settings

        def set_default_config(self):
            '''Method to reset window config'''
            self.width = 1400
            self.height = 900
            self.bg_color = (250, 250, 250)

            self.fps = 60
            self.zoom = 5
            self.offset = (0, 0)

            # Set mouse controls
            self.mouse_last = (0, 0)
            self.mouse_down = False

        def loop(self, loop=None): # Main loop
