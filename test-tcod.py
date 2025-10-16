from __future__ import annotations

import sys
import os

#os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]

import glob

import tcod as libtcod

ASSETS_FOLDER = "assets"
FONT_FILE = os.path.join(ASSETS_FOLDER, "Alloy_curses_12x12.png")

class ExampleState:
    player_x : int
    player_y : int
    def __init__(self, x, y) :
        self.player_x = x
        self.player_y = y

    def on_draw(self, console : libtcod.console.Console) -> None :
        console.print(self.player_x, self.player_y, "@")




def main() -> None :
    screen_width = 80
    screen_height = 50

    tileset = libtcod.tileset.load_tilesheet(FONT_FILE, columns = 16, rows = 16, charmap = libtcod.tileset.CHARMAP_CP437)
    libtcod.tileset.procedural_block_elements(tileset = tileset)
    console = libtcod.console.Console(screen_width, screen_height)
    state = ExampleState(x = console.width // 2, y = console.height // 2)


    with libtcod.context.new(tileset = tileset) as context :
        while True :
            console.clear()
            state.on_draw(console)
            context.present(console)
            for event in libtcod.event.wait() :
                print(event)
                if isinstance(event, libtcod.event.Quit) :
                    raise SystemExit
    

        
if __name__ == "__main__" :
    main()

