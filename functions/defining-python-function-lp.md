# Lesson Plan: Introduction to Python Functions

## Key Terms and Concepts
- **Function**: A reusable piece of code that performs a specific task.
- **Parameters**: Variables declared in a function definition that represent the input values.
- **Arguments**: Actual values passed to a function when it is called.
- **Return value**: The result or output produced by a function.

## Lesson Outline

### Lesson Hook (1 - 2 minutes)
Start with a simple riddle or puzzle related to functions. For example: "What do you call a reusable piece of code that performs a specific task?"

### Mini Lesson (8 - 10 minutes)
- Explain what a function is and why it’s essential in programming.
- Discuss the difference between parameters and arguments.
- Introduce the concept of return values.

### Guided Practice (15 minutes)
1. Write a basic Python function together on the board (e.g., a function that calculates the area of a rectangle).
2. Ask students to identify the parameters and arguments in the function.

### Station Rotation (10 minutes)
- Set up stations where students practice writing simple functions with different parameters and return values.
- Rotate students through the stations. (See example code at the bottom of the document)

### Activities (5 minutes)
- Have students work in pairs to create their own small functions (e.g., a function that converts Fahrenheit to Celsius).

### Independent Practice (5 minutes)
- Assign a short coding exercise where students write a function to find the maximum of two numbers.

### Assessment
- Ask students to write a function that calculates the factorial of a given number.

## Differentiation
- **For advanced students**:
  - Discuss real-world scenarios where functions are used (e.g., calculating taxes, converting units, or processing data). Encourage students to think about how they can apply functions in their daily lives.
- **For struggling students**:
  - Pair up students with varying levels of expertise. Have them work together on coding exercises, with the more experienced student guiding the other.

## Discussion Questions
1. What is the purpose of using parameters in a function?
2. How can you determine the return value of a function?

**FOR STATION ROTATIONS**

```python
def calculate_sum(a, b):
    sum = a + b
    return sum

# Example function call
print(calculate_sum(2, 3))  # Output: 5

def multiply(a, b=10):  # Defining a default parameter
    return a * b

print(multiply(12))  # Output: 120
print(multiply(2, 3))  # Output: 6

def calculate_area(name):
    name = name.lower()
    if name == "rectangle":
        length = int(input("Enter rectangle's length: "))
        breadth = int(input("Enter rectangle's breadth: "))
        rect_area = length * breadth
        print(f"The area of rectangle is {rect_area}.")
    elif name == "square":
        side = int(input("Enter square's side length: "))
        sqt_area = side * side
        print(f"The area of square is {sqt_area}.")
    elif name == "triangle":
        height = int(input("Enter triangle's height length: "))
        base = int(input("Enter triangle's base length: "))
        tri_area = 0.5 * base * height
        print(f"The area of triangle is {tri_area}.")
    elif name == "circle":
        radius = int(input("Enter circle's radius length: "))
        pi = 3.14
        circ_area = pi * radius * radius
        print(f"The area of circle is {circ_area}.")
    elif name == "parallelogram":
        base = int(input("Enter parallelogram's base length: "))
        height = int(input("Enter parallelogram's height length: "))
        para_area = base * height
        print(f"The area of parallelogram is {para_area}.")
    else:
        print("Sorry! This shape is not available")

if __name__ == "__main__":
    print("Calculate Shape Area")
    shape_name = input("Enter the name of the shape whose area you want to find: ")
    calculate_area(shape_name)

SALES_TAX_RATE = 0.07

def calculate_total_cost(item_price):
    tax_amount = item_price * SALES_TAX_RATE
    total_cost = item_price + tax_amount
    return total_cost

if __name__ == "__main__":
    item_price = float(input("Enter the item price: "))
    total_cost = calculate_total_cost(item_price)
    print(f"Total cost (including tax) is ${total_cost:.2f}")
```

