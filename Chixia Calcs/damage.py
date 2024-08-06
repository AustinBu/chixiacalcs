import multipliers as mp
from buff import *
from chixia import *

wife = Chixia(90, 1000, 0.73, 1.72)
res_multiplier = 0

def calc_damage(multiplier):
    all_type_buff = 0
    for buff in wife.damage_multipliers:
        if buff.type == DamageType.ALL:
            all_type_buff += buff.amount
    return round(multiplier/100 
                 * wife.attack 
                 * (1 + (wife.crit_rate * wife.crit_damage))
                 * (1 + all_type_buff), 
                3)

def calc_basic_combo(level):
    multiplier = mp.basic_combo(level)/100
    total_buff = 0
    total_buff += wife.total_multipliers[DamageType.ALL.value]
    total_buff += wife.total_multipliers[DamageType.ELEMENTAL.value]
    total_buff += wife.total_multipliers[DamageType.BASIC.value]
    return int(multiplier 
                 * wife.attack 
                 * wife.crit_multiplier 
                 * (1 + total_buff))

def calc_forte_combo(level, hits):
    multiplier = mp.forte_combo(level, hits)/100
    total_buff = 0
    total_buff += wife.total_multipliers[DamageType.ALL.value]
    total_buff += wife.total_multipliers[DamageType.ELEMENTAL.value]
    total_buff += wife.total_multipliers[DamageType.SKILL.value]
    return int(multiplier 
                 * wife.attack 
                 * wife.crit_multiplier 
                 * (1 + total_buff))

def add_multiplier(amount, type):
    wife.add_buff(Buff(amount, type))

add_multiplier(0.15, DamageType.ALL)
print(calc_basic_combo(0))
print(calc_forte_combo(0, 30))