# Lesson Plan: Understanding If Statements in Python

## Key Terms and Concepts
- **Conditional Statements**: Statements that allow the program to make decisions based on certain conditions.
- **Boolean Expressions**: Expressions that evaluate to either `True` or `False`.
- **if Statement**: A control structure that executes a block of code if a condition is `True`.
- **else Statement**: A control structure that executes a block of code if the condition in the `if` statement is `False`.
- **elif Statement**: A control structure that allows you to check multiple conditions in sequence.

## Lesson Hook (1 - 2 minutes)
Begin the lesson by asking students a simple question: "How do you make decisions in your everyday life?" Discuss their responses and relate decision-making to programming.

## Mini Lesson (8 - 10 minutes)
### Introduction to If Statements
- Explain that **if statements** are used to execute specific code blocks based on whether a condition is `True`.
- Show examples of basic if statements in Python:

```python
age = 15
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

## If-Else Statements
- Introduce if-else statements as an extension of basic if statements.
- Explain that the else block is executed when the condition in the if statement is False.

```
temperature = 25
if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not too hot.")
```
## If-Elif-Else Statements
- Discuss more complex scenarios using if-elif-else statements.
- Show an example with multiple conditions:

```
grade = 85
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B.")
else:
    print("You need to improve.")
```

## Guided Practice (15 minutes)
- Divide students into pairs.
- Provide a list of scenarios (e.g., checking if a number is positive/negative, determining if a student passed an exam, etc.).
- Ask students to write Python code using if statements to handle these scenarios.

## Station Rotation (15 minutes)
- Set up 3 - 4 stations with different Python problems related to if statements.
- Students rotate through the stations, solving problems collaboratively.
- Stations can include writing code, debugging, and analyzing existing code.

## Activities (5 minutes)
- Have students create their own if statements based on real-world situations (e.g., weather conditions, age restrictions, etc.).

## Independent Practice (5 minutes)
- Assign a small problem-solving task that requires using if statements.
## Assessment
- Give students a set of problems to solve individually using if statements.
## Differentiation
- For advanced students: Challenge them with more complex problems or additional conditions.
- For struggling students: Provide extra practice and scaffolded examples.


**Discussion Questions:**
1. What is the purpose of an `if` statement in Python?
   - **Answer**: An `if` statement allows us to execute specific code blocks based on whether a condition is `True`.
2. How does an `if-else` statement differ from a basic `if` statement?
   - **Answer**: An `if-else` statement includes an additional code block to execute when the condition is `False`.
3. Why would you use an `elif` statement instead of multiple `if` statements?
   - **Answer**: An `elif` statement allows you to check multiple conditions in sequence, making the code more efficient and organized.

