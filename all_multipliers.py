from buff import BuffType

# List of number of hits
# List of level multipliers
# Damage Type

basic1 = [[1], 
          [33.30, 36.04, 66.21],
          [BuffType.BASIC]]
basic2 = [[2], 
          [24.3, 26.3, 48.32],
          [BuffType.BASIC]]
basic3 = [[4], 
          [16.88, 18.26, 33.55],
          [BuffType.BASIC]]
basic4 = [[1], 
          [117, 126, 232.61],
          [BuffType.BASIC]]
heavy1 = [[1], 
          [18, 19.48, 35.79],
          [BuffType.HEAVY]]
heavy2 = [[1], 
          [40.5, 43.83, 80.52],
          [BuffType.HEAVY]]
air = [[1], 
        [16.2, 17.52, 32.21],
          [BuffType.BASIC]]
counter = [[1], 
            [171, 185.03, 339.97],
          [BuffType.BASIC]]
skill = [[8], 
          [16],
          [BuffType.SKILL]]
ult = [[11, 1], 
       [29.1],
       [480],
       [BuffType.ULT]]
forte = [[1, 1], 
         [10], 
         [220],
         [BuffType.SKILL]]
intro = [[2, 4], 
         [24.75], 
         [12.38],
          [BuffType.INTRO]]
outro = [[1], 
         [530],
         [BuffType.OUTRO]]

all = [basic1, basic2, basic3, basic4, heavy1, heavy2, skill, air, counter, ult, forte, intro, outro]
for move in all:
    move[-1].append(BuffType.FUSION)


