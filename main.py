from __future__ import annotations

import os.path

import tcod as libtcod

from ExampleState import ExampleState

from StateMachine import StateMachine

def main() -> None :
    ASSETS_FOLDER = "assets"
    FONT_FILE = os.path.join(ASSETS_FOLDER, "Alloy_curses_12x12.png")

    screen_width = 80
    screen_height = 50
    
    tileset = libtcod.tileset.load_tilesheet(FONT_FILE, columns = 16, rows = 16, charmap = libtcod.tileset.CHARMAP_CP437)
    libtcod.tileset.procedural_block_elements(tileset = tileset)
    console = libtcod.console.Console(screen_width, screen_height)
    

    state = ExampleState(x = console.width // 2, y = console.height // 2)
    STATE_MACHINE = StateMachine(state)
    


    with libtcod.context.new(tileset = tileset) as context :
        while True :
            console.clear()
            STATE_MACHINE.on_draw(console)
            context.present(console, keep_aspect = True)
            for event in libtcod.event.wait() :
                print(event)
                STATE_MACHINE.on_event(event)
    

        
if __name__ == "__main__" :
    main()
