from State import State
import tcod as libtcod

class ExampleState(State):
    name = "ExampleState"

    player_x : int
    player_y : int
    
    def __init__(self, x : int, y : int) :
        self.player_x = x
        self.player_y = y

    def on_draw(self, console : libtcod.console.Console) -> None :
        console.print(self.player_x, self.player_y, "@")

    def on_event(self, event : libtcod.event.Event) -> None :
        match event:
            case libtcod.event.Quit() :
                raise SystemExit
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.LEFT) :
                self.player_x -= 1
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.RIGHT) :
                self.player_x += 1
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.UP) :
                self.player_y -= 1
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.DOWN) :
                self.player_y += 1
            case _ :
                pass