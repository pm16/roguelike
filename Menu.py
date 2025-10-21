import tcod as libtcod
from enum import StrEnum

class BOX(StrEnum) :
    V_LINE = "│",
    H_LINE = "─",
    UL_CORNER = "┌",
    UR_CORNER = "┐",
    LL_CORNER = "└",
    LR_CORNER =  "┘"


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
        longest = 0
        for x in range(len(self.items)) :
            if len(self.items[x]) > len(self.items[(x + 1) % len(self.items)]) :
                longest = len(self.items[x])
        if len(self.title) > longest :
            longest = len(self.title)
        for i in range(longest + 2) :
            console.print(self.x_pos + i -1, self.y_pos  - 1, BOX.H_LINE)
            console.print(self.x_pos + i -1, self.y_pos + len(self.items) +1, BOX.H_LINE)

        for i in range(len(self.items) + 1) :
            console.print(self.x_pos - 2, self.y_pos + i, BOX.V_LINE)
            console.print(self.x_pos + longest + 1, self.y_pos + i, BOX.V_LINE)

        console.print(self.x_pos -2, self.y_pos - 1, BOX.UL_CORNER)
        console.print(self.x_pos + longest + 1, self.y_pos - 1, BOX.UR_CORNER)
        console.print(self.x_pos -2, self.y_pos + len(self.items) + 1, BOX.LL_CORNER)
        console.print(self.x_pos + longest + 1, self.y_pos + len(self.items) + 1, BOX.LR_CORNER)


        console.print(self.x_pos, self.y_pos, self.title)
        y = 1
        for item in self.items :
            console.print(self.x_pos, self.y_pos + y, item)
            y += 1
        console.print(self.x_pos -1, self.y_pos + self.cursor_pos + 1, self.cursor)
