from enum import Enum

class DamageType(Enum):
    ALL = 0
    BASIC = 1
    HEAVY = 2
    SKILL = 3
    ULT = 4
    INTRO = 5
    OUTRO = 6
    ELEMENTAL = 7

class Buff(object):
    amount = 0
    type = 0

    def __init__(self, amount, type):
        self.amount = amount
        self.type = type
