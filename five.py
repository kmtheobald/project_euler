# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

lcm_ten = 2520 # as given

''' The prime factors of 12, 14, 15, 18, 20 are all evidently contained 
in 2520. That leaves the prime numbers 11, 13, 17, 19 to multiply into 
the lcm, as well as an extra 2 as 16 = 2**4 compared to 8 = 2**3. '''

lcm_twenty = lcm_ten * (11 * 13 * 17 * 19 * 2)
print(lcm_twenty) # yields 232792560
