# List  Comprehensions Demo
# 11 JUN 20XX

# Concise way to create Python lists

# Format
# [expression for value in iterable if condition]
# Source: https://youtu.be/YlY2g2xrl6Q?feature=shared

# Traditional loop
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# List comprehension
doubles2 = [x * 2 for x in range(1, 11)]
print('The second list looks like this:')
print(doubles2)

# List comprehension
triples = [y * 3 for y in range(1, 11)]
print('The triples list:')
print(triples)

# List comprehension
squares = [z ** 2 for z in range(1, 11)]
print('The squares list:')
print(squares)

squares2 = [pow(a, 2) for a in range(1, 21)]
print('The squares2 list:')
print(squares2)

# With strings
fruits = ['apple', 'orange', 'kiwi', 'coconut']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# Return first character of string
first_names = ['mike', 'jennifer', 'karl', 'alyssa', 'hunter']
first_chars = [first_name[0] for first_name in first_names]
print(first_chars)

nums = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in nums if num >= 0]
print(positive_nums)

negative_nums = [num for num in nums if num < 0]
print(negative_nums)

even_nums = [num for num in nums if num % 2 == 0]
odd_nums = [num for num in nums if num % 2 == 1]
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30, 88]
passing_grades = [grade for grade in grades if grade >= 59]
print(passing_grades)