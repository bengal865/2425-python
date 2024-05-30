##
Lesson Title: Defining and Using Classes in Python

**Grade Level:** 11th/12th Grade

**Subject:** Computer Science

**Time Allotment:** 45 minutes

**Michigan Computer Science Standards Addressed:**

- CP.A2.1.2: Design solutions using classes and objects.
- CP.A2.2.1: Develop and use classes with appropriate attributes and methods.

**Key Terms and Concepts:**

- Class: A blueprint for creating objects that define data (attributes) and behaviors (methods).
- Object: An instance of a class that holds specific values for the attributes defined in the class.
- Attribute: A variable that holds data specific to an object.
- Method: A function defined within a class that describes the behavior of the object.
- Instance: The creation of an object from a class blueprint.

**Lesson Outline:**

**1. Lesson Hook (1-2 minutes):**

- Begin by showing students a real-world example of a blueprint, such as one for a house.
- Ask them: How does a blueprint help builders? (It provides a detailed plan to construct something specific.)
- Explain that in Python, classes act as blueprints for creating objects.

**2. Mini Lesson (8-10 minutes):**

- Pose the following scenario: Imagine we want to create a program to manage information about different types of pets. What kind of information might we want to store for each pet (e.g., name, breed, age)?
- Facilitate a discussion about how we could organize this data in Python using variables and lists.
- Introduce the concept of a class – a more efficient way to manage similar data structures.

**3. Guided Practice Activities (15 minutes):**

- **Activity 1 (5 minutes):** Teacher-led demonstration. Show students the basic syntax for defining a class in Python:


```
class Pet:
def __init__(self, name, breed, age):  # This is the constructor method
  self.name = name
  self.breed = breed
  self.age = age
```
- Explain each part:
  - class Pet: defines the class name.
  - def __init__(self, name, breed, age): defines the constructor method (__init__) that initializes attributes for each object (pet) created from this class.
  - self.name = name, etc.: assign values passed during object creation to the corresponding attributes.
- **Activity 2 (10 minutes):** Students practice with the teacher.
  - Provide students with a half-written class definition for another object type (e.g., Book) and ask them to complete it by defining the constructor method with appropriate attributes.

**4. Station Rotations (15 minutes):**

- Set up three stations around the classroom, each focusing on a different aspect of classes and objects.
- Divide students into small groups and have them rotate through the stations, spending 5 minutes at each.
  - **Station 1: Creating Instances (Objects):**
    - Students are given a completed class definition (e.g., Pet) and write code to create instances (objects) of that class with specific values for the attributes.
  - **Station 2: Accessing Object Attributes:**
    - Students are presented with code that creates objects and then write code to access and print the values of the object's attributes.
  - **Station 3: Method Madness (Optional):**
    - (For advanced students) Introduce the concept of methods in a class. Briefly explain how methods define behaviors for objects and show an example. Students are challenged to write a simple method within the class definition (e.g., a speak() method for the Pet class).

**5. Activities (5 minutes):**

- As a class, discuss key takeaways from the station rotations. Briefly revisit the purpose of classes and objects.

**6. Independent Practice (5 minutes):**

- Provide students with a short independent coding activity where they can create their own class definition and objects based on a scenario (e.g., design a class to manage information about students in a course).

**7. Assessment (Ongoing):**

- Observe students' participation during discussions and guided practice activities.
- Review their work at each station during rotations.
- Collect and assess the independent coding activity.

**8. Differentiation:**

- **Advanced Students:** Challenge them to write methods within the class definition (Station 3) or explore inheritance in Python (creating subclasses from existing classes).
- **Struggling Students:** Provide additional support during guided practice and station rotations. Offer scaffolding questions.


**Discussion Questions:**
1. Why would you use a class in Python instead of just variables and lists? (Classes promote code reusability, organization, and encapsulation of data and behavior.)
2. What is the difference between a class and an object? (A class is the blueprint, while an object is a specific instance created from that blueprint.)
3. Briefly explain the role of the constructor method (__init__) in a class. (The constructor initializes the attributes for each object created from the class.)
