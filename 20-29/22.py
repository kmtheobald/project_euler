# What is the total of all the name scores in the file?

names = open('names.txt')
names_list = names.read().split(',')
names.close()

for i in range(len(names_list)):
    names_list[i] = names_list[i].replace('"', '')

alpha_value = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
                'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
                'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

names_list.sort()
name_score_total = 0
for i in range(len(names_list)):
    name_score = 0
    for char in names_list[i]:
        name_score += alpha_value.get(char)
    
    name_score_total += ((i + 1) * name_score)

print(name_score_total)
# answer equals 871198282