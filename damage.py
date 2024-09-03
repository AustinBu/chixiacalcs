from buff import *
from chixia import *
import random
import numpy as np
from multiplier import *

def calc_damage(wife, combo, hits = [], simulate=False):
    total_damage = 0
    for i in range(len(combo)):
        multiplier, split = calc_with_split(combo[i], hits[i])
        total_buff = calc_buffs(wife,
                                combo[i][-1])
        crit_multiplier = 1
        if simulate:
            crit_percent = np.sum(np.multiply(split, crit_simulate(wife, combo[i])))
            crit_multiplier += (crit_percent * wife.crit_damage) / multiplier
        else:
            crit_multiplier = wife.crit_multiplier

        total_damage += int(multiplier/100
                 * wife.attack 
                 * crit_multiplier 
                 * (1 + total_buff))
    return total_damage

def crit_simulate(wife, attack):
    crit_ratio = []

    for i in attack[0]:
        crit_ratio.append(0)
        for _ in range(i):
            if random.random() < wife.crit_rate:
                crit_ratio[-1] += 1
        crit_ratio[-1] /= i
    return crit_ratio

def calc_forte_combo(wife, mp, hits):
    multiplier = mp.forte_combo(hits)/100
    total_buff = calc_buffs(wife,
                            [BuffType.FUSION, 
                            BuffType.SKILL])
    return int(multiplier 
                 * wife.attack 
                 * wife.crit_multiplier 
                 * (1 + total_buff)
                 * wife.total_multipliers[BuffType.DEEPEN.value])

def calc_buffs(wife, types):
    total_buff = 0
    for type in types:
        total_buff += wife.total_multipliers[type.value]
    return total_buff

def add_multiplier(wife, amount, type, length):
    wife.add_buff(Buff(amount, type, length))

