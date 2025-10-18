import tcod as libtcod

class Menu :
    items = [str]
    title : str
    cursor : str
    cursor_pos : int
    x_pos : int
    y_pos : int

    def __init__(self, title : str, cursor : str, x : int, y : int) :
        self.title = title
        self.cursor = cursor
        self.cursor_pos = 0
        self.x_pos = x
        self.y_pos = y
        self.items.clear()

    def cursor_up(self) -> None :
        self.cursor_pos = (self.cursor_pos - 1) % len(self.items)

    def cursor_down(self) -> None :
        self.cursor_pos = (self.cursor_pos + 1) % len(self.items)

    def select(self) -> str :
        return self.items[self.cursor_pos]
    
    def draw(self, console : libtcod.console.Console) -> None :
        console.print(self.x_pos, self.y_pos, self.title)
        y = 1
        for item in self.items :
            console.print(self.x_pos, self.y_pos + y, item)
            y += 1
        console.print(self.x_pos -1, self.y_pos + self.cursor_pos + 1, self.cursor)
