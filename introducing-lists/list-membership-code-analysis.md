## Code Analysis

- Study the code snippet below
- What do you think the code is supposed to do?

### Thought Questions
1. What information does the ```check_student_enrollment()` function expect to receive from you?
2. Interpret line 12 below.  What's the difference between how the logical operator `and` and the logical operator `or` works?
3. The `result` variable is an example of a **Boolean** variable.  What are the only two possible values can you assign to a Boolean variable?

  ```python
def check_student_enrollment(student, biology_1, biology_2, biology_3):
  return student in biology_1 and (student in biology_2 or student in biology_3)

biology_1 = ["Alice", "Bob", "Charlie"]
biology_2 = ["Bob", "David", "Eve"]
biology_3 = ["Alice", "Eve", "Frank"]

specific_student = "David"
result = check_student_enrollment(specific_student, biology_1, biology_2, biology_3)

if result:
    print(f"{specific_student} is enrolled in Biology 1 and at least one of the other two classes (Biology 2 or Biology 3).")
else:
    print(f"{specific_student} is not enrolled in both Biology 1 and either Biology 2 or Biology 3.")
