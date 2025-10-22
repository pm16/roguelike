import tcod as libtcod

class State:
    name : str
    GAME : object

    def __init__(self, game, name) :
        self.name = name
        self.GAME = game
    def on_draw(self, console : libtcod.console.Console) -> None :
        pass

    def on_event(self, event : libtcod.event.Event) -> None :
        pass

    def on_update(self) -> None :
        pass 