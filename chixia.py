from typing import Any
from buff import DamageType

class Chixia(object):
    level = 0
    attack = 0
    crit_rate = 0
    crit_damage = 0
    crit_multiplier = 0
    
    # all buffs/debuffs
    damage_multipliers = []
    # all buffs/debuffs aggregated by type
    total_multipliers = []

    def __init__(self, 
                 level = 1,
                 attack = 24, 
                 crit_rate = 0.05, 
                 crit_damage = 0.5):
        self.level = level
        self.attack = attack
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.crit_multiplier = 1 + (crit_rate * crit_damage)
        for _ in range(len(DamageType)):
            self.total_multipliers.append(0)

    def set_level(self, level):
        self.level = level

    def set_attack(self, attack):
        self.attack = attack

    def set_crit_rate(self, crit_rate):
        self.crit_rate = crit_rate
        self.crit_multiplier = 1 + (self.crit_rate * self.crit_damage)


    def set_crit_damage(self, crit_damage):
        self.crit_damage = crit_damage
        self.crit_multiplier = 1 + (self.crit_rate * self.crit_damage)


    def add_buff(self, buff):
        self.damage_multipliers.append(buff)
        type = buff.type.value
        self.total_multipliers[type] += buff.amount
