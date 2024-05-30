# Lesson Plan: Working with Classes and Instances in Python 
**Target Audience:** 11th & 12th Grade Computer Science 
**Time Allotment:** 45 minutes
**Standards:** This lesson aligns with the following Michigan K-12 Computer Science Standards:

- CR.I.2: Design and implement solutions using object-oriented programming.
- CR.A.1: Demonstrate understanding of data structures (e.g., classes and objects).

**Key Terms and Concepts:**

- Class: A blueprint for creating objects.
- Instance (Object): A specific realization of a class.
- Attribute: A variable associated with a class or instance.
- Method: A function defined within a class.
- Constructor (init method): A special method used to initialize attributes when creating an object.
- Class Attribute: An attribute defined at the class level, shared by all instances of that class.
- Instance Attribute: An attribute defined within a method, specific to a particular instance.

**Lesson Outline:**

1. **Lesson Hook (1-2 minutes):**
- Begin by showing students a real-world example of a class and its instances. For instance, a "Car" class as a blueprint and individual cars (e.g., your car and your friend's car) as instances.
- Briefly discuss the idea of shared characteristics (attributes) and how specific instances can have variations.
2. **Mini Lesson (8-10 minutes):**
- Introduce classes and instances using Python syntax. Explain how classes define attributes and methods, and instances are created from those classes.
- Demonstrate creating a simple class like Dog with attributes like breed and name.
- Briefly discuss instance attributes by creating objects and assigning unique names to each dog instance.
3. **Guided Practice Activities (15 minutes):**
- **Activity 1 (5 minutes): Setting Default Values for Class Attributes (CR.A.1)**
- Explain the concept of default class attributes and their importance in consistency.
- Guide students through modifying the Dog class to add a default attribute age=0.
- Discuss how this sets the initial age for all dog instances unless explicitly changed.
- **Activity 2 (5 minutes): Modifying Class Attributes Directly (CR.I.2)**
- Demonstrate modifying a class attribute directly outside of methods (e.g., Dog.age = 1).
- Explain how this change will affect all existing and future dog instances.
- Discuss potential drawbacks of modifying class attributes directly.
- **Activity 3 (5 minutes): Using a Method to Modify Class Attributes (CR.I.2)**
- Introduce the concept of using methods to change class attributes in a controlled manner.
- Show students how to create a method (e.g., grow()) that increments the age attribute for a specific dog instance.
4. **Station Rotations (10 minutes):**
- Divide the class into small groups and set up 3 stations:
  - Station 1: "Dog Park" (Challenge: Create multiple dog instances with different breeds and ages using the modified Dog class.)
  - Station 2: "Growth Spurt" (Challenge: Implement the grow() method to increase the age of a dog instance by a specified amount.)
  - Station 3: "Attribute Mystery" (Challenge: Write a short program demonstrating the difference between modifying a class attribute directly vs. using a method.)
- Allow students to rotate through stations, working on each challenge for a few minutes.
5. **Activities (5 minutes):**
- Briefly discuss key takeaways from each station rotation.
- Allow students to share their code snippets and address any questions.
6. **Independent Practice (5 minutes):**
- Provide an exit ticket with a short coding exercise that combines concepts learned throughout the lesson (e.g., creating a class for a product with attributes like name, price, and stock, and including methods to update the stock level).
7. **Assessment:**
- Review student participation in activities and discussions.
- Collect and review exit tickets to gauge understanding.
8. **Differentiation:**
- **Advanced Students:** Challenge them to explore inheritance and create subclasses from the Dog class (e.g., Puppy with a unique play() method).
- **Struggling Students:** Provide additional support during guided practice activities. Offer alternative representations (diagrams) to explain class attributes.

**Discussion Questions:**

1. What are the advantages of setting default values for class attributes? (Reduced redundancy, consistency)
1. When might it be necessary to modify a class attribute directly outside of a method? (e.g., resetting a global counter)
1. How can using methods to modify class attributes contribute to better
