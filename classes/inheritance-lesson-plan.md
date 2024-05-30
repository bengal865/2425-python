# Lesson Plan: Inheritance in Python

**Target Audience:** 11th & 12th Grade Computer Science 
**Time Allotment:** 45 minutes
**Standards:**

- MCR-CS.3.AP.1 - Develop and use classes and objects
- MCR-CS.3.CR.2 - Design solutions that reuse existing code

**Key Terms & Concepts:**

- Inheritance: A way to create new classes (subclasses) that inherit properties (attributes and methods) from existing classes (superclasses)
- Superclass (Parent Class): The original class from which new classes inherit properties.
- Subclass (Child Class): A new class that inherits properties from a superclass.
- Attribute: A variable associated with an object (data).
- Method: A function associated with an object (behavior).
- Override: To redefine a method inherited from the superclass in the subclass.

**Lesson Outline:**

1. **Lesson Hook (1-2 minutes):**
- Show students a family tree visualization. Explain how children inherit traits from their parents.
- Ask: How can we achieve a similar concept in our Python code?
2. **Mini Lesson (8-10 minutes):**
- Briefly introduce inheritance as a way to reuse code and create hierarchical relationships between classes.
- Use an analogy like animals (Superclass: Animal, Subclasses: Dog, Cat) to explain inheritance.
- Show a simple example of a Shape superclass with attributes like color and a method to get\_area().
3. **Guided Practice (15 minutes):**
- Activity 1 (5 minutes):
  - Walk students through creating the Shape superclass with basic attributes and methods.
  - Emphasize using self to access object attributes within methods.
- Activity 2 (10 minutes):
- Guide students in creating a subclass Square that inherits from Shape.
- Show how to define additional attributes specific to squares (e.g., side\_length).
- Explain how Square can inherit the get\_area() method from Shape but potentially override it later.
4. **Station Rotation (15 minutes):**
- Implement 3 stations with different activities related to inheritance. Students rotate through each station in small groups (3-4 students).
- Station 1: Override Challenge (5 minutes)
  - Students are given a pre-written Shape class and a Circle subclass.
  - They need to override the get\_area() method in Circle to calculate the area of a circle (πr^2).
- Station 2: Inheritance Hierarchy (5 minutes)
  - Students are presented with a scenario (e.g., building a game) and need to design a class hierarchy using inheritance. (e.g., GameObject -> Character -> Player, Enemy)
- Station 3: Mystery Code (5 minutes)
- Students analyze a short code snippet with inheritance concepts (e.g., accessing attributes from the superclass, method overriding) and explain the functionality.
5. **Activities (5 minutes):**
- Briefly discuss key takeaways from the station rotations.
- Reinforce the concept of method overriding with a quick example.
6. **Independent Practice (5 minutes):**
- Provide students with a short independent coding activity to solidify the learned concepts.
- Example: Create a Vehicle superclass with attributes like make and model. Define subclasses Car and Truck that inherit from Vehicle and have additional specific attributes (e.g., Car could have num\_doors).
7. **Assessment (Ongoing):**
- Observe students' participation during guided practice and station rotations.
- Review their independent practice code and ensure they understand inheritance concepts.
- Ask open-ended questions throughout the lesson to gauge understanding.
8. **Differentiation:**
- Advanced Students:
  - Challenge them to explore different types of inheritance (multilevel, multiple).
  - Encourage them to implement abstract classes to define a general structure for subclasses.
- Struggling Students:
- Provide additional support during guided practice activities.
- Offer simpler examples for independent practice initially.

**Discussion Questions:**

1. Why is inheritance a useful concept in object-oriented programming? (**Answer:** It promotes code reuse, reduces redundancy, and allows for creating specialized classes from general ones.)
2. What happens when a method is overridden in a subclass? (**Answer:** The subclass's definition of the method takes precedence over the inherited version from the superclass.)
3. Can a subclass access attributes and methods defined in the superclass? (Answer: Yes, a subclass inherits all attributes and methods from the superclass. It can access and use them directly, or override them if needed.)
