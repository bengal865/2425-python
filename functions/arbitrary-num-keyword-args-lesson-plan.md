**Lesson Plan 2: Supercharge Your Functions with Keyword Arguments (45 minutes) Grade Level:** 11th &12th Grade (AP Computer Science Principles)

**Michigan State Standards:** CPS.2.P.1, CPS.2.DP.2 **Key Terms and Concepts:**

- Functions with Keyword Arguments
- Arbitrary Keyword Arguments (**\*\*kwargs**)

**Lesson Hook (1-2 minutes):**

- Present a scenario where a function needs to handle data with various properties, but not all properties are guaranteed to be provided each time (e.g., building a user profile with optional fields like location or hobbies).
- Ask students: How can we design Python functions that can accept a variable number of named arguments?

**Mini Lesson (8-10 minutes):**

1. Briefly review defining a Python function with keyword arguments. (e.g., def greet(name, greeting="Hello"): print(greeting, name))
1. Introduce the concept of functions accepting an arbitrary number of keyword arguments using \*\*kwargs.
1. Demonstrate a basic example: def user\_profile(name, \*\*info): print("Name:", name); for key, value in info.items(): print(key, ":", value). Explain how \*\*kwargs captures all remaining keyword arguments as a dictionary.

   This Python code defines a function called user\_profile that takes two arguments:

1. **name:** This is expected to be a string representing the user's name. It's treated as a positional argument, meaning it needs to be provided in a specific order when calling the function.
1. **info:** This argument uses the \*\* syntax, signifying it captures an arbitrary number of keyword arguments. These keyword arguments willbe stored in a dictionary named info within the function.

Here's a breakdown of what the function does:

1. **Prints the Name:** It starts by printing "Name:" followed by the value of the name argument.
1. **Iterates through user info:** It uses a for loop to iterate through the info dictionary. The loop unpacks each key-value pair into variables named key and value.
1. **Prints User Information:** Inside the loop, it prints the key from the info dictionary followed by a colon (":")and then the corresponding value.

In essence, this function acts like a user profile builder. You can call it with the user's name and any additional information you want to store about them (like location, hobbies, etc.) using keyword arguments. The function then displays the name and all the provided user information in a clear format.

**Guided Practice Activities (20 minutes):**

(5 minutes)Walk students through modifying the greet function to accept an arbitrarynumber of greetings using \*\*kwargs and printing a personalized message for each.

Python![](Aspose.Words.cfeec66f-ee18-47be-ad9e-641b1eea8664.001.png)

def greet(name, \*\*greetings):

"""

This function greets a person with various greetings provided as keyword arguments.

Args:

name: The name of the person to greet (str).

\*\*greetings: An arbitrary number of greetings provided as keyword arguments

(str).

"""

print(f"Hello, {name}!")

for greeting, message in greetings.items():

print(f"{greeting.title()}: {message}")

\# Example usage

greet("Alice", morning="Good morning", afternoon="Have a wonderful afternoon!")

1. (10 minutes) Provide a code snippet with a function that displays information about a book (e.g., display\_book(title, author))and ask students to modify it to accept additional details (publisher, year) using \*\*kwargs and a conditional statement to display only the provided information.

Unset![](Aspose.Words.cfeec66f-ee18-47be-ad9e-641b1eea8664.002.png)

2. def display\_book(title, author, \*\*info):
2. """
2. This function displays information about a book. 5.
6. Args:
7. title: The title of the book (str).![](Aspose.Words.cfeec66f-ee18-47be-ad9e-641b1eea8664.003.png)
7. author: The author of the book (str).
7. \*\*info: An arbitrary number of additional book details

provided as keyword arguments (str).

10. """
10. print(f"Title: {title}")
10. print(f"Author: {author}")

13\.

14. # Check for provided information in kwargs and print accordingly
14. if "publisher" in info:
14. print(f"Publisher: {info['publisher']}")
14. if "year" in info:
14. print(f"Year Published: {info['year']}")

19\.

20\. # You can add similar checks for other optional info like genre, edition, etc.

21\.

22. # Example usage with all details
22. display\_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", publisher="Pan Books", year=1979)

24\.

25. # Example usage with some details
25. print("---")
25. display\_book("The Lord of the Rings", "J.R.R. Tolkien", year=1954)

![](Aspose.Words.cfeec66f-ee18-47be-ad9e-641b1eea8664.004.png)

Explanation:

1. The function display\_book takes three arguments:
- title: The title of the book (str).
- author: The author of the book (str).
- \*\*info: An arbitrary number of additional book details provided as keyword arguments (str). These are stored in a dictionary named info within the function.
2. It starts by printing the title and author information.
2. Then, it uses conditional statements to check for specific keys ("publisher" and "year") within the info dictionary.
2. Ifa key is found, it retrieves the corresponding value using info['key'] and prints it with a label (e.g., "Publisher:", "Year Published:").
2. You can add similar checks for other optional book details (genre, edition, etc.) by including them in the conditional statements.
2. The provided examples demonstrate calling the function with different combinations of information using keyword arguments. The output willonly display information that was provided during the function call.

28\. (5 minutes) Facilitate a class discussion to ensure students understand how keyword arguments and \*\*kwargs work together.

**Station Rotation Activities (10 minutes):**

(Divide the class into 3 groups and rotate every 3-4 minutes)

- Station 1: "Customize It!":Students receive pre-written code with a function containing both keyword arguments and \*\*kwargs that performs a specific task (e.g., creates a dictionary with user preferences). They need to customize the function to accept additional preferences using \*\*kwargs.
- Station 2: "Function Architect": Students are provided with a template for a function and a scenario requiring customization with various named arguments (e.g., formatting a message based on urgency and recipient type). They need to complete the function using \*\*kwargs to handle different arguments.
- Station 3: "Think Outside the Box!": Advanced students receive a challenging problem requiring manipulation of data passed through \*\*kwargs (e.g., analyzing a dataset of customer purchases with varying product categories). They design a function using \*\*kwargs to efficiently process the data.

**Activities (5 minutes):**

- Briefly have students reflect on the benefits of using functions with \*\*kwargs.

**Independent Practice (Homework - 10 minutes estimated):**

- Assign a coding challenge where students write a function using \*\*kwargs to solve a real-world problem with a variable number of named arguments (e.g., building a shopping cart with various product details).

**Assessment:**

- Review student work from guided practice activities and station rotations.
- Collect and assess the completed homework assignment.

**Differentiation:**

- Advanced Students: Encourage them to explore advanced functionalities within \*\*kwargs (e.g., using default values for keyword arguments, combining with positional arguments).
- Struggling Students: Provide additional guided practice with simpler examples and scaffolding during station rotations.

**Discussion Questions:**

1. What are the advantages of using functions with \*\*kwargs compared to functions with only keyword arguments? (Possible Answer: Provides flexibilityin accepting an unknown number of named properties)
1. Can \*\*kwargs be used with positional arguments in the same function? Why or why not? (Possible Answer: Yes, but positional arguments must be defined before \*\*kwargs to avoid ambiguity)
1. How can we make our functions using \*\*kwargs user-friendly and handle unexpected keyword arguments effectively? (Possible Answer: Write clear documentation, type hints for the user, and handle potential errors within the function)
7
