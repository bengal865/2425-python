# Bruce Provencher
# 17 OCT 2022
# Lists & FOR Loops

friends = ['Mike', 'Jason', 'Robert', 'Jennifer', 'Alyssa']

temperatures = [50, 57, 48, 51, 52, 53, 51, 34, 31]

# Display index number of my second friend in my friends list
print(f"Index number of my second friend: {friends.index('Jason')}")
print(f"Index number of last temperature: {temperatures.index(31)}")

# Using index number to update the friends in my friends list
print('#' * 10)
print('Original friends list:')
for friend in friends:
    print(friend)
print('#' * 10)
# Updating a name in the friends list
friends[4] = 'Sarah'
print('Updated friends list:')
for friend in friends:
    print(friend)
print('#' * 10)
print()
print()
print('Basic Statistics with A List')
for temperature in temperatures:
    print(temperature, end = ' ')
print()
print(f'Maximum temperature: {max(temperatures)}')
print(f'Minimum temperature: {min(temperatures)}')
print(f'SUM of temperatures: {sum(temperatures)}')
print()
print('My favorite Michael Crichton books:')
book_titles = ['andromeda strain', 'timeline', 'the lost world']
for book_title in book_titles:
    print(f'\t{book_title.title()} by Michael Crichton.')
print()
print()