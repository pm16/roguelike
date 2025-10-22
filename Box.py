from enum import StrEnum

class BOX(StrEnum) :
    V_LINE = "│",
    H_LINE = "─",
    UL_CORNER = "┌",
    UR_CORNER = "┐",
    LL_CORNER = "└",
    LR_CORNER =  "┘"