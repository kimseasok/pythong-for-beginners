names = ['John', 'Bob', 'Mosh']

print(names[0])

startFromTwo = names[2:]

for name in names:
    print(name)

print(startFromTwo)

# find max num in list

numbers = [3, 10, 20, 30, 5, 9, 35, 40, 12]

max = numbers[0]

for number in numbers:

    if number > max:

        max = number

print(max)

# Multi dimentional list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][0])

# Tuple in python

tuple_numbers = (1, 2, 3 )

print(tuple_numbers)