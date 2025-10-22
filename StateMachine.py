from State import State
import tcod as libtcod

class StateMachine:
    stack = [State]

    def __init__(self) :
        self.stack.clear()

    def pop(self) -> None :
        self.stack.pop()

    def push(self, state : State) -> None :        
        self.stack.append(state)

    def current(self) -> State :
        return self.stack[len(self.stack) -1]
    
    def on_draw(self, console : libtcod.console.Console) -> None :
        self.stack[len(self.stack) -1].on_draw(console)
    
    def on_event(self, event : libtcod.event.Event) -> None :
        self.stack[len(self.stack) -1].on_event(event)

    def on_update(self, dt : float) -> None :
        self.stack[len(self.stack) -1].on_update(dt)
