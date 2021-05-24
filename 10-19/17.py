# If all the numbers from 1 to 1000 (one thousand) inclusive 
# were written out in words, how many letters would be used? 

def number_split(num):
    length = len(str(num))
    if (length == 1 or length == 4):
        split = []
        split.append(num)
        return split
    if (length == 2):
        split = [int(char) for char in str(num)]
        if (num % 100 > 10 and num % 100 < 20):
            split[-1] += 10
            del split[-2]
        else:
            split[0] *= 10
        return split
    if (length == 3):
        split = [int(char) for char in str(num)]
        if (num % 100 > 10 and num % 100 < 20):
            split[-1] += 10
            split[0] *= 100
            del split[-2]
        else:
            split[0] *= 100
            split[1] *= 10
        return split

total_letters = 0
number_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
                12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 
                70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundredand',
                200: 'twohundredand', 300: 'threehundredand', 400: 'fourhundredand', 
                500: 'fivehundredand', 600: 'sixhundredand', 700: 'sevenhundredand',
                800: 'eighthundredand', 900: 'ninehundredand',
                1000: 'onethousand'}

def num_letters(num):
    letters = 0
    components = number_split(num)
    print(components)
    for component in components:
        letters += len(number_dict.get(component))
    if (num % 100 == 0 and num != 1000):
        letters -= 3
    return letters

for num in range(1, 1001):
    total_letters += num_letters(num)

print(total_letters)
# answer equals 21124