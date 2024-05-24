# last_name = 'Lincoln'
# print(f'First three letters of the string {last_name}:')
# for letter in last_name[:3]:
#     print(letter.upper())

# Source: https://youtu.be/rHTwjV1ORUQ

import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '()[]{},;:.-_/\\?+*# ' # Included a blank space at end of this string

first_names = ['Mike', 'Jenna', 'Carlos', 'Elisabeth', 'Maddox', 'Kael', 'Destiny', 'Noah', 'Braydan', 'Noe']
# first_name_sliced = random.choice(first_names)
# first_name_sliced = first_name_sliced[0:3]
last_names = ['Matthes', 'Sorensen', 'Schmidt', 'Haines', 'Crowley', 'Spitz', 'Moore', 'Bekins', 'Ford', 'Worley']

upper = True
lower = True
nums = True
syms = True

full_username = ''

if upper:
    full_username += uppercase_letters

if lower:
    full_username += lowercase_letters

if nums:
    full_username += digits

if syms:
    full_username += symbols

length = 7
num_usernames = 3

for x in range(num_usernames):
    username = ''.join(random.sample(full_username, length))
    truncated_first_name = f'{first_names[x][0:3]}'
    full_username = f'{last_names[x]}{truncated_first_name}{username}'
   
    print(full_username)



        
