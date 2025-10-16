from __future__ import annotations

import sys
import os

#os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]

import glob

import tcod as libtcod

ASSETS_FOLDER = "assets"
FONT_FILE = os.path.join(ASSETS_FOLDER, "Alloy_curses_12x12.png")

def main() -> None :
    screen_width = 80
    screen_height = 50

    tileset = libtcod.tileset.load_tilesheet(FONT_FILE, columns = 16, rows = 16, charmap = libtcod.tileset.CHARMAP_CP437)
    libtcod.tileset.procedural_block_elements(tileset = tileset)
    console = libtcod.console.Console(screen_width, screen_height)
    console.print(0, 0, "Hello World")

    with libtcod.context.new(tileset = tileset) as context :
        while True :
            context.present(console)
            for event in libtcod.event.wait() :
                print(event)
                if isinstance(event, libtcod.event.Quit) :
                    raise SystemExit
    

        
if __name__ == "__main__" :
    main()

