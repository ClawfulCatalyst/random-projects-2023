import random

values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

hex = ['0','0','0','0','0','0']
for i in range(6):
    rand_in_16_a = random.randint(0,15)
    rand_in_16_b = random.randint(0,15)
    val = values[rand_in_16_a] + values[rand_in_16_b]
    hex[i] = val

print(':'.join(hex))
