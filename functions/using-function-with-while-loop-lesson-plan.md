**Lesson Plan 1: Looping with Functions (Basic)**

**Target Audience:** 11th/12th Grade Computer Science

**Time Allotment:** 45 Minutes **Michigan Standards:** CS.A.ALG.1.2, CS.A.PRG.1.3

**Key Terms and Concepts:**

- While Loop
- Function Definition
- User Input
- quit condition

**Lesson Outline: Hook (1-2 minutes):**

- Play a game of "Guess the Number" with the class. Explain how you can keep track of guesses with a loop. Briefly introduce the concept of "quitting" the loop when a condition is met.

**Mini Lesson (8-10 minutes):**

- Briefly review while loops, focusing on the syntax and the importance of the loop condition.
- Introduce the concept of functions in Python, explaining how they are reusable blocks of code.

**Guided Practice (15 minutes):**

1. **Function for Input Validation (5 minutes):**
- Teacher leads students through writing a simple function get\_valid\_number(prompt). This function asks the user for a number using

  input(prompt), but keeps asking until the user enters a valid number (integer or float).

2. **Looping with the Function (10 minutes):**
- Teacher guides students on writing a program that uses the get\_valid\_number function inside a while loop. The loop keeps prompting the user for numbers until they enter a specific value (e.g., -1) to quit.
- Emphasize placing the quit condition **within** the loop to allow continuous input until the user signals termination.

**Station Rotations (15 minutes) - Dr. Catlin Tucker's Model:**

1. **Function Fun (5 minutes):** Students have pre-written functions with intentional errors (e.g., missing return statement, incorrect parameter). They identify and fix the errors.
1. **Challenge Loop (5 minutes):** Students modify the loop program to perform a different action with the user-entered numbers (e.g., calculate an average).
1. **Mystery Box (5 minutes):** Students are given a box with pre-written code snippets (functions and a loop) with missing parts. They need to assemble the code to achieve a specific task (e.g., count even numbers entered).

**Activities (5 minutes):**

- Students reflect on the challenges of placing the quit condition within the loop.

**Independent Practice (5 minutes):**

- Students write a short program using a loop and a function of their choice. (e.g., a function to check if a number is even and a loop to keep asking for even numbers until the user enters 0).

**Assessment:**

- Observe student participation in activities and station rotations.
- Review student code from independent practice, focusing on function usage within the loop and correct placement of the quit condition.

**Differentiation:**

- **Advanced Students:**
- Challenge them to write recursive functions to be used within the loop.
- Explore nested loops with additional functionalities.
- **Struggling Students:**
- Provide scaffolding for the independent practice by giving them a template for the loop and function.
- Offer peer support during station rotations.

**Discussion Questions:**

1. Why is it important to place the quit condition within the loop for user input? (**Answer:** It ensures the loop keeps asking for input until the user explicitly signals termination.)
1. How can a function be helpful when used inside a loop? (**Answer:** It allows for code reuse and modularity, making the loop program more organized and easier to read.)
1. What are some potential errors that could occur when combining loops and functions? (**Answer:** Forgetting to return a value in the function, using incorrect function parameters, or placing the quit condition outside the loop.)
3
