**Lesson Plan: Taking Control - User Input with Python Target Audience:** 11th & 12th Grade Computer Science

**Time Allotment:** 45 minutes

**Michigan State CS Standards Addressed:**

- CP.K12.CT.2.2 - Develop and use algorithms that process input from the user.
- CP.K12.CT.2.3 - Develop and use algorithms that produce formatted output.

**Key Terms and Concepts:**

- input() function
- Data types (integers, floats)
- int() function
- float() function
- Modulus operator (%)

**Lesson Outline:**

**Introduction (Hook - 5 minutes)**

- Play a short quiz game where students can only answer "yes" or "no" using hand signals (e.g., trivia, 20 questions). Discuss how limiting this interaction is and how programs can become more interactive by taking user input.

**Mini Lesson (8 minutes)**

- Briefly introduce the input() function in Python. Show how it captures user input as a string.
- Demonstrate how to use print() statements to display this captured input.
- Ask students: How can we make the program work with numbers the user enters?

**Resources:**

- Video: Introduction to User Input in Python
- Article: Getting Input from the User in Python <https://www.programiz.com/python-programming/examples>

**Guided Practice (15 minutes)**

- **Activity 1 (5 minutes):** Write a simple program that asks the user for their name and age, then greets them with both pieces of information. (Introduce variable assignment here)
- **Activity 2 (10 minutes):** Challenge students to modify the program to accept the user's age as a number. Discuss type mismatch errors and introduce the int() function to convert the input string to an integer.
- Show how the program behaves differently if the user enters a non-numeric value.

**Station Rotations (10 minutes)**

- **Station 1: Number Guessing Game (3 minutes)**
- Students write a program that generates a random number and asks the user to guess it. Use a loop to allow multiple guesses. Provide a template with the random number generation pre-written.
- **Station 2: Mad Libs with Input (3 minutes)**
- Provide a silly story template with placeholders for various words (e.g., noun, adjective, verb). Students use input() to collect these words and fill the template.
- **Station 3: Challenge Station (4 minutes)**
- Introduce the concept of data types (integers, floats). Challenge students to write a program that asks the user for a length (integer) and width (float) and calculates the area.

**Activities (5 minutes)**

- Have students share their completed programs from the stations. Briefly discuss any challenges they faced.

**Independent Practice (5 minutes)**

- Challenge students to create their own interactive program using input(). Encourage them to incorporate different data types and explore the modulus operator (%).

**Assessment:**

- Review student work from the independent practice activity. Look for proper use of input(), data type conversion functions (int(), float()), and clear explanations of their program's functionality.

**Differentiation:**

- **Advanced Students:** Challenge them to explore error handling for invalid user input (e.g., non-numeric values). Introduce exception handling concepts.
- **Struggling Students:** Provide additional support during guided practice activities. Offer pre-written code snippets for specific functionalities.

**Discussion Questions:**

1. Why is it important for programs to be able to take input from the user? (Increased interactivity, user-specific responses)
1. What are the potential challenges associated with user input? (Type mismatch errors, invalid data)
1. How can we ensure our programs handle user input effectively? (Data type conversion, error handling)
3
