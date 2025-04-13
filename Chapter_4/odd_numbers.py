'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
'''

# Using list comprehensions
odd=[print(value) for value in range(1,20,2)]

# As instructed
odd_2 = list(range(1,20,2))

for number in odd_2:
    print(number)