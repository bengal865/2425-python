Lesson Plan: Returning Values from Python Functions (45 minutes)

**Grade Level:** 11th & 12th Grade (AP Computer Science Principles)

**Michigan State Standards:** CP.A.2, CP.A.3

**Key Terms and Concepts:** function, return statement, argument, optional argument, variable

**Lesson Hook (1-2 minutes):**

- Begin by showing students a simple magic trick. (e.g., pull a coin from behind their ear).
- Explain how the trick relies on a hidden mechanism (the function) that produces a surprising result (the returned value).
- Today, we'll learn how to create functions in Python that can return values, making our code more powerful and reusable.

**Mini Lesson (8-10 minutes):**

- Briefly review the concept of functions and how they take inputs (arguments) and perform actions.
- Introduce the idea of a "return statement" as a way for a function to send a value back to the code that called it.
- Show a simple example:

  Python

def s quar e( x) :![](Aspose.Words.fdfbeb5d-8f10-4a2e-946e-859fd9aa46e2.001.png)

r es ul t = x \* x r et ur n r es ul t

number = 5![](Aspose.Words.fdfbeb5d-8f10-4a2e-946e-859fd9aa46e2.002.png)

s quar ed\_number = s quar e( number )

pr i nt ( s quar ed\_number ) # Out put : 25

**Guided Practice Activities (20 minutes):**

1. (5 minutes) Have students work in pairs to rewrite the previous example without the intermediate variable (result).
   1. Expected Answer: def square(x): return x \* x
1. (10 minutes) Present a new function that calculates the area of a rectangle.
   1. Ask students: How can we modify the function to take either one or two arguments (length and width) but still calculate the area?
   1. Guide them towards using an optional argument with a default value (e.g., width=1).
1. (5 minutes) Challenge students to write a function that checks if a number is even and returns True or False.

**Station Rotations (10 minutes):**

1. **Function Frenzy:** Students work on a worksheet with various problems requiring them to write functions with return statements for tasks like calculating volume of a sphere or converting Celsius to Fahrenheit.
1. **Mystery Box:** Provide pre-written functions with missing parts (deliberate errors) and have students debug them to identify the issue related to the return statement.
1. **Code Golf:** Challenge students to rewrite existing functions with return statements in the most concise way possible.

**Activities (5 minutes):**

- Briefly discuss common mistakes related to the return statement (e.g., forgetting to return a value, returning multiple values unintentionally).

**Independent Practice (Homework - 10 minutes):**

- Assign students a coding challenge where they need to use functions with return statements for tasks like calculating the average of a list of numbers or finding the maximum element in a list.

**Assessment:**

- Observe students' participation during guided practice and station rotations.
- Collect and review their independent practice assignments.

**Differentiation:**

- **Advanced Students:** Challenge them to explore functions that return multiple values using tuples or unpacking.
- **Struggling Students:** Provide additional scaffolded examples and pair them with stronger students during station rotations.

**Discussion Questions:**

1. What is the difference between printing a value inside a function and returning it? (**Answer:** Printing displays the value in the console, while returning sends it back to the calling code for further use.)
1. Can a function have multiple return statements? (**Answer:** Yes, but the function will exit after the first encountered return statement is executed.)
1. How can you make an argument in a Python function optional? (**Answer:** By assigning a default value to the argument in the function definition.)
2
