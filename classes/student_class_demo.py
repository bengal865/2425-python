# Author: Bruce Provencher
# Date: 15 APR 2021
# Project: Student Class Example

class Student():

    def __init__(self, fname, gender, school, grade):
        """A class representing a student in the physical world."""
        self.fname = fname
        self.gender = gender
        self.school = school
        self.grade = grade

    def show_award(self):
        print(f'Congratulations, {self.fname}! You made the Honor Roll this semester at {self.school} High School!')

    def display_biography(self):
        print(f'{self.fname} is a {self.grade} at {self.school} this year.')


# Create two students
brock = Student('Brock', 'male', 'Alba', 'senior')
krista = Student('Krista', 'female', 'Kingsley', 'junior')

# Display a single attribute about each student
print(f'Brock goes to {brock.school} High School.')
print(f'Krista goes to {krista.school} High School.\n')

print('Student Award Info:\n')
brock.show_award()
krista.show_award()

print('\nSummary of Student Information:\n')
krista.display_biography()
brock.display_biography()
