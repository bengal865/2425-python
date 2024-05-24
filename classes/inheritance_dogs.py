# Bruce Provencher
# 18 MAY 2021
# Inheritance and Dog Classes
# Source: https://youtu.be/C2QfkDcQ5MU


# Superclass named Dog
class Dog():
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__( name, age, friendliness)


class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__( name, age, friendliness)

class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__( name, age, friendliness)

sammy = Samoyed('Sammy', 2, 10)

print(f'\nName: {sammy.name}')
print(f'Age: {sammy.age}')
print(f'Friendliness (1 - 10): {sammy.friendliness}\n')
print(f'{sammy.name} likes walks: {sammy.likes_walks()}\n')