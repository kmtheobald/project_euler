# Determine which line number has the greatest numerical value

from math import log

exp_file = open('p099_base_exp.txt')
exponentials = exp_file.read().splitlines()
exp_file.close()

max_number = 0
line_number = 0
for i in range(len(exponentials)):
    base_power = exponentials[i].split(',')
    base_power = [int(i) for i in base_power]
    number = base_power[1] * log(base_power[0])
    if (number > max_number):
        max_number = number
        line_number = i + 1

print(line_number)
# answer equals 709