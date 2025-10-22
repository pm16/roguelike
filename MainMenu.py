from State import State
from Menu import Menu
from ExampleState import ExampleState

import tcod as libtcod

class MainMenu(State) :
    name = "Main Menu"

    menu = Menu(name, "*", 20, 20)

    menu.items.append("Start")
    menu.items.append("Options")
    menu.items.append("Quit")

    def on_event(self, event : libtcod.event.Event) -> None :
        match event:
            case libtcod.event.Quit() :
                raise SystemExit
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.UP) :
                self.menu.cursor_up()
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.DOWN) :
                self.menu.cursor_down()
            case libtcod.event.KeyDown(sym = libtcod.event.KeySym.RETURN) :
                self.option(self.menu.select())
            case _ :
                pass

    def on_draw(self, console : libtcod.console.Console) ->None :
        self.menu.draw(console)

    def option(self, choice : str) :
        match choice :
            case "Quit" : 
                raise SystemExit
            case "Options" :
                pass
            case "Start" :
                self.GAME.STATE_MACHINE.push(self.GAME.STATES["Example State"])
                pass
            case _ :
                pass