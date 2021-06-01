# How many [words] are triangle words? 

words_file = open('words.txt', 'r')
words = words_file.read().split(',')
words_file.close()

alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 
            'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 
            'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 
            'Y': 25, 'Z': 26}

triangle_numbers = []
for i in range(1, 100):
    num = i*(i + 1) // 2
    triangle_numbers.append(num)

new_words = []
for word in words:
    new_words.append(word.strip('\"'))

triangle_count = 0
for word in new_words:
    total = 0
    letters = list(word)
    for letter in letters:
        total += alphabet.get(letter)
    if total in triangle_numbers:
        triangle_count += 1

print(triangle_count)
# answer equals 162