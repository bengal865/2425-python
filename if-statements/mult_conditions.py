# Bruce Provencher
# 13 OCT 2022
# Compound Conditions

my_age = 21
your_age = 17

# Logical operator: and
# If each test passes, then the entire compound condition evaluates to True
if my_age >= 18 and your_age >= 18:
    print('Both of you are old enough to vote!')
else:
    print('At least one of you is NOT old enough to vote!')


joes_height = 70 
lukes_height = 58

if joes_height >= 60 or lukes_height >= 60:
    print('At least one person is tall enough to ride the rollercoaster.')
else:
    print('At least one person does not meet the minimum height requirement.')