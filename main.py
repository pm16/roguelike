from __future__ import annotations
import tcod as libtcod
from Game import Game

def main() -> None :
    GAME = Game()
    with libtcod.context.new(tileset = GAME.TILESET) as context :
        while True :
            GAME.STATE_MACHINE.on_update()
            GAME.CONSOLE.clear()
            GAME.STATE_MACHINE.on_draw(GAME.CONSOLE)
            context.present(GAME.CONSOLE, keep_aspect = True)
            for event in libtcod.event.wait() :
                #print(event)
                GAME.STATE_MACHINE.on_event(event)
                    
if __name__ == "__main__" :
    main()
