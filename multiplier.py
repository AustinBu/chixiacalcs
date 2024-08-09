from all_multipliers import *

class Multiplier(object):
    basic1 = basic1
    basic2 = basic2
    basic3 = basic3
    basic4 = basic4
    heavy1 = heavy1
    heavy2 = heavy2
    air = air
    counter = counter
    skill = skill
    forte = forte
    ult = ult
    intro = intro
    outro = outro
    all = []

    def __init__(self, levels):
        self.all = [
            self.basic1,
            self.basic2,
            self.basic3,
            self.basic4,
            self.heavy1,
            self.heavy2,
            self.air,
            self.counter,
            self.skill,
            self.forte,
            self.ult,
            self.intro,
            self.outro
        ]
        for j in range(len(self.all)):
            if j < 8:
                level = levels[0]
            elif j == len(self.all) - 1:
                level = 0
            else:
                level = levels[j - 7]
            for i in range(len(self.all[j][0])):
                self.all[j][i + 1] = self.all[j][i + 1][level]

    def basic_combo(self):
        total_multiplier = 0
        combo = [self.basic1, self.basic2, self.basic3, self.basic4]
        for attack in combo:
            total_multiplier += calciplier(attack)
        return total_multiplier

    def forte_combo(self, hits):
        return calciplier(self.forte, [hits, 1])
    
    def parse_attack(self, attack):
        if type(attack) == str:
            if attack == "skill":
                return self.skill
            elif attack == "forte":
                return self.forte
            elif attack == ult:
                return self.ult
        else:
            return attack

def calciplier(attack, hits=[]):
    total_multiplier = 0
    for i in range(len(attack[0])):
        multiplier = attack[i+1] * attack[0][i]
        if hits != []:
            multiplier *= hits[i]
        total_multiplier += multiplier
    return total_multiplier

def calc_with_split(attack, hits=[]):
    total_multiplier = 0
    split = []
    for i in range(len(attack[0])):
        multiplier = attack[i+1] * attack[0][i]
        if hits != []:
            multiplier *= hits[i]
        total_multiplier += multiplier
        split.append(multiplier)
    return total_multiplier, split
