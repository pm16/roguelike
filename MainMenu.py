from State import State
from Menu import Menu
from ExampleState import ExampleState

import tcod as libtcod

class MainMenu(State) :
    menu : Menu
    
    def __init__(self, game, name) :
        self.name = name
        self.GAME = game
        self.menu = Menu(self.name, "*", self.GAME.SCREEN_WIDTH // 2, self.GAME.SCREEN_HEIGHT // 2)

        self.menu.items.append("Start")
        self.menu.items.append("Options")
        self.menu.items.append("Quit")

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