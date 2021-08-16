import os
import sys
import pygame as pg
from pygame import mixer

from snek_inspyred.game.audio.conf import Config, SoundLib

class Sounds(object):
    def __init__(self):
        sm_lib = SoundLib['DEFAULT']
        self.begin_game = mixer.Sound(sm_lib['begin-game'])
        self.eat_food = mixer.Sound(sm_lib['eat-food'])
