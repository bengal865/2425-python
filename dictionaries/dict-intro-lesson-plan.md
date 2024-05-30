**Lesson Plan: Introduction to Python Dictionaries Time Allotment:** 45 Minutes

**Michigan State Standards:**

- CSP.02 - Data Structures and Algorithms
- CSP.04 - Problem Solving

**Key Terms and Concepts:**

- Dictionary
- Key-Value Pair
- Accessing Values
- Adding Key-Value Pairs

**Lesson Outline:**

**Introduction (Hook - 5 minutes):**

- Play a quick game of "20 Questions" with the class. Explain how keeping track of the yes/no answers would be easier with a data structure that uses keywords (categories) to access information (answers).

**Mini Lesson (8 minutes):**

- Briefly introduce the concept of dictionaries as a data structure similar to a real-world dictionary with key-value pairs.
- Use an analogy like a phonebook (key: name, value: phone number) to illustrate.

**Resources:**

- Video: Intro to Python Dictionaries[ YouTube](https://www.youtube.com/watch?v=daefaLgNkw0)
- Article: [Python Dictionaries on Digital Ocean ](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)site
- **Guided Practice (15 minutes):**
- **Activity 1 (5 minutes):** Have students write down a short list of 5 items and their descriptions (e.g., "apple: fruit", "banana: fruit"). Discuss how this list can be represented as a dictionary.
- **Activity 2 (10 minutes):** Introduce the syntax for creating dictionaries using curly braces {} and colon : to separate keys and values. Demonstrate creating a simple dictionary and how to access its values using square bracket notation [].

**Station Rotation (10 minutes - Dr. Catlin Tucker's Model):**

- **Station 1 (Dictionary Creation):** Students practice creating dictionaries with different data types (strings, integers) as keys and values.
- **Station 2 (Value Access):** Students write code snippets to access values from predefined dictionaries using keys.
  - Willget error ifyou ask for a key that doesn’t exist
  - SOLUTION:Use the **get ( ) method**, which allows the user to set a default value that is returned ifthe requested key doesn’t exist
  - Practice setting up and using the get ()method to handle instances when a reque
- **Station 3 (Challenge):** Students are given a scenario (e.g., representing student information with names and grades) and asked to create a dictionary to model it.

**Activities (5 minutes):**

- As a class, brainstorm real-world examples of where dictionaries might be useful (e.g., online shopping carts, user profiles).

**Independent Practice (5 minutes):**

- Students are given a worksheet with basic exercises on creating and accessing values in dictionaries.

**Assessment (5 minutes):**

- Exit ticket: Students answer a short question about key-value pairs in dictionaries and write a simple example.

**Differentiation:**

- **Advanced Students:** Can explore nested dictionaries or dictionary methods like keys() and values().
- **Struggling Students:** Can work with a partner during guided practice and receive additional support during stations.

**Discussion Questions:**

1. What are the advantages of using dictionaries compared to lists? (**Possible Answer**: Easier to access specific information using keywords)
1. Can duplicate keys exist in a dictionary? Why or why not? (Possible Answer: No, keys must be unique to identify values)
1. How can we access a value in a dictionary ifwe don't know its position? (**Possible Answer**: Use the key within square brackets [])

```python
# Remember: Dictionaries store info in key-value pairs.  The key acts like a label that uniquely identifies the associated value.  So, to access a value in a dictionary, you don't need to know its position; you simply need the correct key.
my_dictionary["key_name"]
```

