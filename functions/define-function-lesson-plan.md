# Lesson Plan: Introduction to Python Functions
**Key Terms & Concepts:**
- Function
- Parameters
- Arguments
- Return value
### Lesson Outline:
1. **Lesson Hook (1 - 2 minutes):**
   1. Start with a simple riddle or puzzle related to functions. For example: “What do you call a reusable piece of code that performs a specific task?”
1. **Mini Lesson (8 - 10 minutes):**
   1. Explain what a function is and why it’s essential in programming.
   1. Discuss the difference between parameters and arguments.
   1. Introduce the concept of return values.
1. **Guided Practice (15 minutes):**
   1. Write a basic Python function together on the board (e.g., a function that calculates the area of a rectangle).
   1. Ask students to identify the parameters and arguments in the function.
1. **Station Rotation (10 minutes):**
   1. Set up stations where students practice writing simple functions with different parameters and return values.
   1. Rotate students through the stations. (See example code at bottom of document)
1. **Activities (5 minutes):**
   1. Have students work in pairs to create their own small functions (e.g., a function that converts Fahrenheit to Celsius).
1. **Independent Practice (5 minutes):**
   1. Assign a short coding exercise where students write a function to find the maximum of two numbers.
1. **Assessment:**
   1. Ask students to write a function that calculates the factorial of a given number.
1. **Differentiation:**
   1. For advanced students
      1. Real-World Applications: Discuss real-world scenarios where functions are used (e.g., calculating taxes, converting units, or processing data). Encourage students to think about how they can apply functions in their daily lives.
   1. For struggling students
      1. Pair up students with varying levels of expertise. Have them work together on coding exercises, with the more experienced student guiding the other.
1. **Discussion Questions:**
   1. What is the purpose of using parameters in a function?
   1. How can you determine the return value of a function?

**For Station Rotations:**

```
python
def calculate\_sum(a, b):

   sum = a + b

   return sum

# Example function call

print(calculate\_sum(2, 3))  # Output: 5



def multiply(a, b=10): # Defining a default parameter

   return a \* b

print(multiply(12))  # Output: 120

print(multiply(2, 3))  # Output: 6



def calculate\_area(name):

   name = name.lower()

   if name == "rectangle":

   length = int(input("Enter rectangle's length: "))

   width = int(input("Enter rectangle's width: "))

   rect_area = length \* width

   print(f"The area of rectangle is {rect_area}.")

   elif name == "square":

   side = int(input("Enter length of the square's side: "))

   sqt_area = side \* side

   print(f"The area of square is {sqt_area}.")

   elif name == "triangle":

   height = int(input("Enter triangle's height length: "))

   base = int(input("Enter triangle's base length: "))

   tri_area = 0.5 * base * height

   print(f"The area of triangle is {tri_area}.")

   elif name == "circle":

   radius = int(input("Enter circle's radius: "))

   pi = 3.14

   circ_area = pi * radius * radius

   print(f"The area of circle is {circ_area}.")

   elif name == "parallelogram":

   base = int(input("Enter parallelogram's base: "))

   height = int(input("Enter parallelogram's height: "))

   para_area = base * height

   print(f"The area of parallelogram is {para_area}.")

   else:

   print("Sorry! This shape is not available")

if __name__ == "__main__":

   print("Calculate Shape Area")

   shape_name = input("Enter the name of shape whose area you want to find: ")

   calculate_area(shape_name)



SALES_TAX_RATE = 0.07

def calculate_total_cost(item_price):

   tax_amount = item_price * SALES_TAX_RATE

   total_cost = item_price + tax_amount

   return total_cost

if __name__ == "__main__":

   item_price = float(input("Enter item cost in dollars (0 to quit): "))

   full_total = 0

   while item_price != 0:

   total_with_tax = calculate_total_cost(item_price)

   print(f"Tax amount on this item: ${tax_amount:.2f}")

   print(f"Total payment: ${total_with_tax:.2f}")

   full_total += total_with_tax

   item_price = float(input("Enter item cost in dollars (0 to quit): "))

   print(f"Your full total today is ${full_total:.2f}")



def greet(name1, name2, name3):

   print(f"Hello {name1}, {name2}, and {name3}!")

greet("Steve", "Bill", "Mikey")  # Output: Hello Steve, Bill, and Mikey!



def greet(name, greeting="Hello"):

   return f"{greeting}, {name}!"

message1 = greet("Alice")

print(message1)  # Output: Hello, Alice!
```


