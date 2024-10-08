from chixia import Chixia
from damage import *
from multiplier import Multiplier

wife = Chixia(90, 887, 1851, 0.734, 1.678)
wife.add_buff(Buff("Echo", 0.086, BuffType.SKILL, 0))
wife.add_buff(Buff("Echo", 0.323, BuffType.BASIC, 0))
wife.add_buff(Buff("Echo", 0.079, BuffType.HEAVY, 0))
wife.add_buff(Buff("Echo", 0.116, BuffType.ULT, 0))
wife.add_buff(Buff("Echo", 0.323, BuffType.BASIC, 0))
wife.add_buff(Buff("Echo", 0.82, BuffType.FUSION, 0))

wife.add_buff(Buff("Verina", 0.15, BuffType.DEEPEN, 0))

# print("-")
# print(calc_basic_combo(wife, 0))
# print("-")
# print(calc_forte_combo(wife, 0, 70))
# print("-")
# print(calc_forte_combo(wife, 0, 30) * 2)
# print("-")

mp = Multiplier([0, 0, 0, 0, 0])
new_combo = [mp.skill, mp.forte, mp.ult]
hits = [[], [30, 1], []]

print(calc_damage(wife, new_combo, hits, simulate=False))
print(calc_damage(wife, new_combo, hits, simulate=True))
