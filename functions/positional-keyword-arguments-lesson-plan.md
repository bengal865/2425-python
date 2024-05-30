**Lesson Plan: Introduction to PositionalArguments**

**Key Terms and Concepts:**

- Positionalarguments
- Function parameters
- Function calls

**Lesson Outline:**

1. **Lesson Hook(1- 2 minutes):** Begin byasking students to think about how theyorder their favorite pizza toppings. Explain that just like pizza toppings have a specific order, function arguments in Python also follow a specific sequence.
1. **MiniLesson (8 - 10 minutes):** Discuss positionalarguments:
   1. Explain that positionalarguments are passed to a function in the order theyappear in the function definition.
   1. Show examples of function calls with positionalarguments.
   1. Discuss the importance of matching the number of arguments with the function’s parameter count.
1. **Guided Practice (15 minutes):**

1\. Students work in pairs:

1. Write a function that calculates the area of a rectangle using length and width as positionalarguments.
1. Callthe function with different values and observe the results.

4\. **Station Rotation (15 minutes):**

1\. Set up three stations:

1. **Code Station:** Students write a function that calculates the volume of a cylinder using radius and height as positionalarguments.
1. **Discussion Station:** Discuss the advantages and limitations of using positionalarguments.
3. **Problem-Solving Station:** Given a real-world problem, students design a function with appropriate positionalarguments.
5. **Activities (5 minutes):** Share solutions from the stations and discuss common mistakes.
5. **Independent Practice (5 minutes):** Students write a function that computes the factorial of a given number using a positionalargument.
5. **Assessment (5 minutes):** Provide a simple problem where students applypositional arguments.
5. **Differentiation:**
1. **Advanced Students:** Explore variable-length positionalarguments (e.g., \*args).
1. **Struggling Students:** Focus on mastering basic positionalarguments.

9\. **Discussion Questions:**

1. What happens if you pass more or fewer arguments than expected to a function?
1. How can you handle default values for positionalarguments?

**Lesson Plan: Exploring Keyword Arguments**

**Key Terms and Concepts:**

- Keyword arguments
- Default parameter values

**Lesson Outline:**

1. **Lesson Hook(1- 2 minutes):** Present a scenario where students customize their coffee order at a localcafé. Explain that just like theycan use specific words to customize their coffee order at a coffee shop, Python allows us to use keyword arguments in function calls.
1. **MiniLesson (8 - 10 minutes):** Discuss keyword arguments:
   1. Explain that keyword arguments are passed with the parameter name followed by an equalsign (=).
   1. Show examples of function calls with keyword arguments.
   1. Introduce default parameter values.
1. **Guided Practice (15 minutes):**
1. Students modifythe rectangle area function from Lesson 1to accept keyword arguments for length and width.
1. Discuss the benefits of using keyword arguments when writing your script.

4\. **Station Rotation (15 minutes):**

1\. Similar to Lesson 1, but stations focus on keyword arguments:

1. **Code Station:** Write a function that calculates the volume of a cone using radius and height as keyword arguments.
1. **Discussion Station:** Compare positionaland keyword arguments.
1. **Problem-Solving Station:** Solve a real-world problem using keyword arguments.
5. **Activities (5 minutes):** Share solutions and discuss trade-offs.
5. **Independent Practice (5 minutes):** Students write a function that computes the area of a circle using a keyword argument for radius.
5. **Assessment (5 minutes):** Evaluate students’understanding of keyword arguments.
5. **Differentiation:**
1. **Advanced Students:** Explore variable-length keyword arguments (e.g., \*\*kwargs).
1. **Struggling Students:** Focus on mastering basic keyword arguments.

9\. **Discussion Questions:**

1. When would you choose to use keyword arguments over positionalarguments?
1. How can you set default values for function parameters using keyword arguments?

**Answers to the discussion questions:**

1. \*\*When to Use Keyword Arguments Over PositionalArguments:\*\*
- \*\*Keyword arguments\*\*are usefulin the following scenarios:
  - \*\*Clarity/Easier to read code:\*\*When calling a function with multiple arguments, using

keywords makes it easier to understand what each argument represents.

- \*\*Skipping OptionalParameters:\*\*If a function has optionalparameters, you can skip them by

using keyword arguments. This is especiallyhelpfulwhen you want to set onlyspecific parameters (instead of specifying allof them).

- \*\*Changing the Order:\*\*With positionalarguments, order matters. However, with keyword

arguments, you can rearrange the parameters in the function callwithout affecting the result.

2. \*\*Setting Default Values for Function Parameters Using Keyword Arguments:\*\*
- In Python, you can set default values for function parameters directlyin the function definition.

An example:

\```python

def greet(name, greeting="Hello"):

print(f"{greeting}, {name}!")

\# How to use in script:

greet("Alice") # Prints: Hello, Alice!

greet("Bob", greeting="Hi") # Prints: Hi, Bob!

\```

- In the example above, the `greeting`parameter has a default value of `"Hello"`. If no value is

provided for `greeting`, it uses the default value.

- You can override the default value bypassing a different value explicitly(as shown in the

second function callwhere you’re greeting Bob).
4
