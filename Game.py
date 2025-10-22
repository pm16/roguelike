from __future__ import annotations
import os.path
from StateMachine import StateMachine
from ExampleState import ExampleState
import tcod as libtcod

from MainMenu import MainMenu

class Game:
    STATE_MACHINE : StateMachine
    ASSETS_FOLDER = "assets"
    FONT_FILE = os.path.join(ASSETS_FOLDER, "Alloy_curses_12x12.png")
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    TILESET : libtcod.tileset.Tileset
    CONSOLE : libtcod.console.Console
    STATES = dict()
    
    def __init__(self) :
        self.TILESET = libtcod.tileset.load_tilesheet(self.FONT_FILE, columns = 16, rows = 16, charmap = libtcod.tileset.CHARMAP_CP437)
        libtcod.tileset.procedural_block_elements(tileset = self.TILESET)
        self.CONSOLE = libtcod.console.Console(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.STATE_MACHINE = StateMachine()
        self.STATES.clear()
        self.load_states()
        self.STATE_MACHINE.push(self.STATES["Main Menu"])

    def load_states(self) :
        self.STATES = {
            "Main Menu" : MainMenu(self, "Main Menu"),
            "Example State" : ExampleState(self, "Example State")
        }
            
        