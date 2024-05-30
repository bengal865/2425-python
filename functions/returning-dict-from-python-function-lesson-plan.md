**Lesson Plan: Returning Dictionaries from Functions (Michigan CS Standard: CP.K12.CT.2.2)**

**Key Terms and Concepts:**

- Function
- Return statement
- Dictionary
- Key-value pair

**Lesson Outline: Hook (1 minute):**

- Show a simple grocery list on the board (e.g., "apples: 3", "milk: 1").
- Ask students how they would store this information in a program? (Possible answers: list, string)
- Briefly introduce dictionaries as a more organized way to store data with key-value pairs.

**Mini Lesson (8 minutes):**

1. Review functions: Briefly discuss functions as reusable blocks of code with inputs and (optional) outputs.
1. Introduce dictionaries:
- Explain key-value pairs and how they work within dictionaries.
- Use visuals like diagrams or real-world examples to illustrate (e.g., phonebook with names as keys and numbers as values).
- Show examples of creating dictionaries using curly braces {} and key-value pairs.

**Guided Practice (15 minutes):**

1. (5 minutes) Walk students through creating a simple function that takes a name as input and returns a dictionary with "name" as the key and the input name as the value.
1. Python![](Aspose.Words.57e930b8-34dc-467b-8702-2f7ae0095de0.001.png)

Unset

3\.

def get\_name\_dict(name):

name\_dict = {"name": name} return name\_dict

4\.

5\.

6\. (10 minutes) Have students practice calling the function with different names and printing the returned dictionary.

**Station Rotations (15 minutes):**

(Use Dr. Catlin Tucker's Station Rotation Model)

- **Station 1: Building Dictionaries (5 minutes):** Students create dictionaries with different key-value pairs related to a chosen topic (e.g., colors, countries).
- **Station 2: Function Challenge (5 minutes):** Students modify the previous function to take two arguments (e.g., name, age) and return a dictionary with both key-value pairs.
- **Station 3: Mystery Function (5 minutes):** Provide a pre-written function that returns a dictionary (e.g., a function that creates a dictionary with student information based on ID).Students call the function, analyze the returned dictionary, and explain its purpose.

**Activities (5 minutes):**

- Class discussion: Briefly discuss the benefits of using dictionaries compared to other data structures for storing specific data.

**Independent Practice (5 minutes):**

- Have students write a short function that takes a book title and author as arguments and returns a dictionary with those details.

**Assessment:**

- Observe students' participation in class discussions and activities.
- Review their independent practice code to check for correct use of dictionaries and function return statements.

**Differentiation:**

- **Advanced Students:** Challenge them to create a function that takes user input (using input())to build a dictionary dynamically.
- **Struggling Students:** Provide additional support during guided practice and station rotations. Offer them pre-written snippets to complete the functions.

**Discussion Questions:**

1. Why are key-value pairs important in dictionaries? (**Answer:** They provide a way to associate specific data with a meaningful label (key) for easy retrieval.)
1. How does returning a dictionary from a function help organize data? (**Answer:** It allows functions to create and return a structured collection of data under one variable name.)
1. Can you think of other situations where using dictionaries might be beneficial? (**Answer:** Student responses may vary, but encourage them to think about scenarios where associating data points with labels is useful (e.g., storing customer information, product details with attributes).
4
