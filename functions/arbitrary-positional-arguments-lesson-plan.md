**Lesson Plan 1: Power Up Your Functions with Arguments! (45 minutes) Grade Level:** 11th & 12th Grade (AP Computer Science Principles) **Michigan State Standards:** CPS.2.P.1, CPS.2.DP.2

**Key Terms and Concepts:**

- Functions with Arguments
- Positional Arguments
- Arbitrary Arguments (\*args)

**Lesson Hook (1-2 minutes):**

- Start by showing a short video of a real-world example where calculations depend on an unknown number of inputs (e.g., calculating average sales for a week with varying daily sales numbers).
- Ask students: How can we write Python code to handle these situations where the number of inputs might change?

**Mini Lesson (8-10 minutes):**

1. Briefly review defining a simple Python function with positional arguments. (e.g., def greet(name): print("Hello", name)).
1. Introduce the concept of functions accepting an arbitrary number of arguments using \*args.
1. Demonstrate a basic example: def sum\_all(\*numbers): total = 0; for num in numbers: total += num; return total. Explain how \*numbers captures all remaining

   arguments as a tuple.

**Guided Practice Activities (20 minutes):**

1. (5 minutes) Walk students through modifying the greet function to accept an arbitrary number of names using \*args and printing a personalized greeting for each.
1. (10 minutes) Provide a code snippet with a function that calculates the area of different shapes based on their type (e.g., square(side), rectangle(length, width)) and ask students to modify it to accept arguments for all shapes using \*args and a conditional statement to determine the area based on the first argument (shape type).
1. (5 minutes) Facilitate a class discussion to ensure students understand how positional arguments and \*args work together.

**Station Rotation Activities (10 minutes):**

(Divide the class into 3 groups and rotate every 3-4 minutes)

- Station 1: "Mystery Function": Students receive pre-written code with a function containing both positional arguments and \*args that performs a specific task (e.g., finds the highest number from a list). They need to decipher the function's behavior and document their findings.
- Station 2: "Function Factory": Students are provided with a template for a function and a scenario requiring an unknown number of inputs (e.g., calculating average exam scores for a class). They need to complete the function using \*args to address the variable number of inputs.
- Station 3: "Challenge Me!": Advanced students receive a more complex problem requiring manipulation of data passed through \*args (e.g., analyzing a list of student grades with different subject scores). They design a function to solve the problem efficiently.

**Activities (5 minutes):**

- Briefly have students reflect on the benefits of using functions with \*args.

**Independent Practice (Homework - 10 minutes estimated):**

- Assign a coding challenge where students write a function using \*args to solve a real-world problem with a variable number of inputs (e.g., calculating total grocery costs with varying item prices).

**Assessment:**

- Review student work from guided practice activities and station rotations.
- Collect and assess the completed homework assignment.

**Differentiation:**

- Advanced Students: Encourage them to explore advanced functionalities within \*args (e.g., unpacking arguments, combining with keyword arguments).
- Struggling Students: Provide additional guided practice with simpler examples and scaffolding during station rotations.

**Discussion Questions:**

1. What are the advantages of using functions with \*args compared to functions with only positional arguments? (Possible Answer: Gives you more flexibility in handling an unknown number of inputs)
1. Can \*args be used with keyword arguments in the same function? Why or why not? (Possible Answer: No, as \*args captures all remaining arguments)
1. How can we ensure our functions using \*args are robust and handle different types of inputs effectively? (Possible Answer: Use conditional statements and data type checks in the function)
3
