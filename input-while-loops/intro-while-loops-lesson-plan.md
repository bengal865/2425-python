**Lesson 1: While Loops - Taking Control**

**Target Audience:** 11th/12th Grade Computer Science

**Time Allotment:** 45 Minutes **Michigan State Standards:**

- CP.K12.CT.2.3 - Design and implement programs that use iteration.
- CP.K12.CT.4.2 - Use problem-solving strategies to develop algorithms and programs.

**Key Terms and Concepts:**

- While loop
- User input
- Conditional statements (if/else)
- Flag variable

**Lesson Outline: Introduction (5 min):**

- Play a quick game of "Would you rather?" with questions that involve repeating actions until a certain condition is met.
- Ex: Would you rather eat 10 pieces of candy or keep guessing a number until you get it right?
- Discuss the concept of repetition and how loops can be used in programming to automate these tasks.

**Mini Lesson (10 min):**

- Briefly review the syntax of the while loop and how it works (condition, body).
- Introduce the concept of user input using the input() function in Python.
- Show a simple example of a loop that continues printing numbers until the user types "stop."
- **Discussion Question 1:** How can we modify this code so the user decides when to stop the loop?

**Resources:**

- [While Loop Example](URL python while loop example ON W3Schools w3schools.com)
- [Python Input Function](URL how to input data in python ON W3Schools w3schools.com)

**Guided Practice (15 min):**

- In pairs, students brainstorm ways to modify the code from the MiniLesson to accept user input for the loop termination condition.
- Facilitate a class discussion to share ideas and solidify the concept.
- Provide a starter code with a while True loop and an input() statement prompting the user to enter "quit".
- Students complete the code to print numbers until the user enters "quit".

**Station Rotations (15 min):**

**Station 1: Modify the Game (5 min):** Students modify the previous code to create a simple guessing game. The loop continues until the user guesses a hidden number correctly.

**Station 2: Infinite Jukebox (5 min):** Students explore the concept of an infinite loop (while True) and add user input to control playback. The loop plays songs from a list until the user enters "stop".

**Station 3: Challenge Me! (5 min):** Provide a more challenging scenario (e.g., counting down from 10 with user-specified decrements) and have students write code using the while loop and user input.

**Activities (5 min):**

- Students reflect on the activity by writing a short paragraph explaining how they used user input to control the loop behavior.

**Independent Practice (Homework - 10 min estimated):**

- Students create their own program using a while loop that incorporates user input to control termination.
- Encourage creativity! Examples could be a quiz game, a countdown timer, or a simple chat application.

**Assessment:**

- Review student code from the Guided Practice and Independent Practice sections.
- Look for correct usage of while loops, user input, and conditional statements.

**Differentiation:**

- **Advanced Students:** Challenge them to incorporate error handling for invalid user input.
- **Struggling Students:** Provide additional support during the Guided Practice and offer step-by-step guidance for the Independent Practice.

**Discussion Questions:**

1. **Why is it important to have a way to break out of a while loop?**
- Answer: To prevent infinite loops and ensure the program terminates when desired.
2. **What are other ways (besides user input) we could control loop termination?**
- Answer: We can use variables (flags) or counters to track specific conditions.

**Lesson 2: While Loops - Flags Up!**

**Target Audience:** 11th/12th Grade Computer Science

**Time Allotment:** 45 Minutes **Michigan State Standards:**

- CP.K12.CT.2.3 - Design and implement programs that use iteration.
- CP.K12.CT.4.2 - Use problem-solving strategies to develop algorithms and programs.

**Key Terms and Concepts:**

- While loop
- Flag variable
- Boolean data type

**Lesson Outline: Introduction (5 min):**

- Briefly recap the concept of user input for controlling while loops from Lesson 1.
- Introduce the idea of using a flag variable as a more programmatic way to control loop termination.

**Mini Lesson (10 min):**

- Explain how a flag variable (usually a Boolean) can be used to signal a specific condition within the loop.
- Show an example where a loop continues as long as the playing flag is True, and the loop terminates when playing is changed to False.
- **Discussion Question 1:** How can we use a flag variable to create a program that asks the user to play a game again?

**Resources:**

- [Flag Variable Example](URL while loop with flag c++ ON Tutorialspoint tutorialspoint.com)
- [Boolean Data Type in Python](URL python data types ON W3Schools w3schools.com)

**Guided Practice (15 min):**

- In pairs, students brainstorm how to implement a flag variable in the code from Lesson 1 (guessing game or jukebox example) to eliminate the need for user input to quit.
- Facilitate a class discussion to share ideas and solidify the concept of flag variables.
- Provide a starter code with a while True loop, a flag variable (playing = True), and modify the loop condition to check the flag value.
- Students complete the code to include logic for setting the flag to False when the game is over or the user chooses to stop playback.

**Station Rotations (15 min):**

**Station 1: Enhance the Game (5 min):** Students modify the code from the Guided Practice to add more levels or difficulty to the game based on the flag variable.

**Station 2: Password Checker (5 min):** Introduce a new scenario where a loop continues prompting the user for a password until the correct password is entered. The flag variable controls loop termination.

**Station 3: Creative Coding (5 min):** Challenge students to design their own program using a while loop and a flag variable.

**Activities (5 min):**

- Students write a short reflection explaining how they used a flag variable to control the loop behavior in their code.

**Independent Practice (Homework - 10 min estimated):**

- Students create their own program using a while loop that incorporates a flag variable to control loop termination.
- Encourage them to explore different scenarios and applications.

**Assessment:**

- Review student code from the Guided Practice and Independent Practice sections.
- Look for correct usage of while loops, flag variables, and Boolean data types.

**Differentiation:**

- **Advanced Students:** Challenge them to explore nested loops and how flag variables can be used across multiple loops.
- **Struggling Students:** Provide additional support during the Guided Practice and offer sample code snippets for the Independent Practice.

**Discussion Questions:**

1. **What are some advantages of using flag variables compared to user input for loop termination?**
- Answer: Flag variables provide a more programmatic way to control the loop based on internal conditions, making the code cleaner and potentially more efficient.
2. **Can you think of other scenarios where flag variables might be useful in programming?**
- Answer: Flag variables can be used to track various program states, signal events, or control different sections of code execution.
8
