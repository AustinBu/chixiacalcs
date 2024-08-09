from chixia import Chixia
from damage import *
from multiplier import Multiplier

wife = Chixia(90, 887, 1851, 0.734, 1.678)
wife.add_buff(Buff("Echo", 0.086, DamageType.SKILL))
wife.add_buff(Buff("Echo", 0.323, DamageType.BASIC))
wife.add_buff(Buff("Echo", 0.079, DamageType.HEAVY))
wife.add_buff(Buff("Echo", 0.116, DamageType.ULT))
wife.add_buff(Buff("Echo", 0.323, DamageType.BASIC))
wife.add_buff(Buff("Echo", 0.82, DamageType.FUSION))

wife.add_buff(Buff("Verina", 0.15, DamageType.ALL))

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
