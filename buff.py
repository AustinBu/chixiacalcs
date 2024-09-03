from enum import Enum

class BuffType(Enum):
    DEEPEN = 0
    BASIC = 1
    HEAVY = 2
    SKILL = 3
    ULT = 4
    INTRO = 5
    OUTRO = 6
    FUSION = 7
    GLACIO = 8
    AERO = 9
    ELECTRO = 10
    SPECTRO = 11
    HAVOC = 12

class Buff(object):
    name = ""
    amount = 0
    type = 0
    length = 0 # in seconds

    def __init__(self, name, amount, type, length=0):
        self.name = name
        self.amount = amount
        self.type = type
        self.length = length
