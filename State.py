import tcod as libtcod

class State:
    name : str

    def on_draw(self, console : libtcod.console.Console) -> None :
        pass

    def on_event(self, event : libtcod.event.Event) -> None :
        pass

    def on_update(self, dt : float) -> None :
        pass 