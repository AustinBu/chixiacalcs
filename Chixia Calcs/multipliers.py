import numpy as np
from buff import DamageType

# List of number of hits
# List of level multipliers
# Damage Type

basic1 = [[1], 
          [33.30, 36.04, 66.21],
          DamageType.BASIC]
basic2 = [[2], 
          [24.3, 26.3, 48.32],
          DamageType.BASIC]
basic3 = [[4], 
          [16.88, 18.26, 33.55],
          DamageType.BASIC]
basic4 = [[1], 
          [117, 126, 232.61],
          DamageType.BASIC]
heavy1 = [[1], 
          [18, 19.48, 35.79],
          DamageType.HEAVY]
heavy2 = [[1], 
          [40.5, 43.83, 80.52],
          DamageType.HEAVY]
air1 = [[1], 
        [16.2, 17.52, 32.21],
          DamageType.BASIC]
counter1 = [[1], 
            [171, 185.03, 339.97],
          DamageType.BASIC]
skill1 = [[8], 
          [16],
          DamageType.SKILL]
ult = [[11, 1], 
       [29.1],
       [480],
       DamageType.ULT]
forte = [[1, 1], 
         [10], 
         [220],
         DamageType.SKILL]
intro = [[2, 4], 
         [24.75], 
         [12.38],
          DamageType.INTRO]
outro = [[1], 
         [530],
         DamageType.OUTRO]

def calciplier(combo, level, hits=[]):
    total_multiplier = 0
    for attack in combo:
        for i in range(len(attack[0])):
            multiplier = attack[i+1][level] * attack[0][i]
            if hits != []:
                multiplier *= hits[i]
            total_multiplier += multiplier
    return total_multiplier

def basic_combo(level):
    return calciplier([basic1, basic2, basic3, basic4], level)

def ult_combo(level):
    return calciplier([ult], level)

def forte_combo(level, hits):
    return calciplier([forte], level, [30, 1])