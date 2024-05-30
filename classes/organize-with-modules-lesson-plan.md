# Lesson Plan: Organizing Your Code with Modules in Python

**Grade Level:** 11th & 12th Grade (Computer Science)

**Subject:** Storing and Importing Classes in Python Modules

**Time Allotment:** 45 minutes

**Alignment:** Michigan K-12 Computer Science Standards (CS.HS.204, CS.HS.220)

**Key Terms & Concepts:**

- Module
- Class
- Import statement
- Namespace
- Alias
- from statement
- import statement

**Lesson Objectives:**

- Students will be able to explain the purpose of modules in Python.
- Students will be able to create Python modules containing classes.
- Students will be able to import single and multiple classes from a module.
- Students will be able to import an entire module and use aliases for organization.

**Lesson Hook (1-2 minutes):**

Start with a real-world scenario. Imagine you're building a game with different characters (e.g., Warrior, Mage). Each character has its own attributes and behaviors. How can you organize the code for each character efficiently and avoid repetition? Briefly introduce the concept of modules as a way to store and reuse code.

**Mini Lesson (8-10 Minutes):**

1. **Brainstorming Activity (5 minutes):**
- Divide the class into small groups. Ask them to list the benefits of organizing code into separate modules.
- Discuss their responses as a class, highlighting benefits like code reusability, reduced redundancy, and improved project structure.
2. **Simple Module Creation (5 minutes):**
- Briefly demonstrate how to create a Python module (.py file) containing a simple class (e.g., Animal class with attributes like name and species).

**Guided Practice Activities (~20 Minutes):**

1. **Importing Single Class (5 minutes):**
- Guide students through importing a single class from the created module using the from statement (e.g., from animals import Animal).
- Create a short script that instantiates an Animal object and demonstrates accessing its attributes.
2. **Importing Multiple Classes & Aliases (5 minutes):**
- Expand the previous activity by showing them how to import multiple classes using comma separation (e.g., from animals import Animal, Dog, Cat).
- Introduce the concept of using aliases for clarity (e.g., from animals import Animal as Creature).
3. **Importing Entire Module & All Classes (5 minutes):**
- Demonstrate importing the entire module using the import statement (e.g., import animals).
- Briefly discuss how this approach allows access to all functionalities within the module (classes, functions, etc.) using dot notation (e.g., animals.Animal).
- Introduce the concept of namespace collision and the potential need for explicit imports to avoid conflicts.

**Station Rotations (15 Minutes): (Adapt based on classroom resources) Station 1: Module Creation Challenge (5 minutes):**

- Students create a module containing different geometric shape classes (e.g., Circle, Square) with relevant attributes (radius, side length).

**Station 2: Import Extravaganza (5 minutes):**

- Provided with various pre-written modules (e.g., math, random), students write short scripts demonstrating different import techniques (single class, multiple classes with aliases, entire module).

**Station 3: Code Organization Showdown (5 minutes):**

- Students analyze a provided messy script with repetitive code and propose how to improve its organization using modules and appropriate import statements.

**Activities (5 Minutes):**

- Students complete a short quiz individually to assess their grasp of module imports (single class, multiple classes, entire module).

**Independent Practice (10 Minutes):**

- Students work on a project where they create separate modules for different functionalities (e.g., one for game mechanics, another for user interface) and demonstrate importing and using classes in their main program.

**Assessment:**

- Review student performance in the guided practice activities, station rotations, and the

  individual quiz.

- Assess the final project for proper module creation, use of import statements, and code organization.

**Differentiation:**

- **Advanced Students:** Challenge them to explore advanced module concepts like relative imports and package structures. Encourage them to research best practices for module organization in larger projects.
- **Struggling Students:** Provide additional support during guided practice activities. Offer scaffolded activities with pre-written modules for initial practice. Encourage peer collaboration during station rotations.

**Discussion Questions:**

1. What are the advantages of using modules in your Python projects? (Answers: There are several advantages: improved code organization, easier to reuse code across projects, reduced redundancy, and easier to share code with co-workers on large projects.)

2. Explain the difference between using from and import statements for importing classes from a module. (Answers: The from statement allows you to import specific classes directly into your current namespace, which means you don't have to use the module name as a prefix. The import statement imports the entire module, and you access classes using dot notation together with the module name.)

3. Why might you use an alias when importing a class from a module? (Answers: Aliases are helpful because the make the code easier to read and help avoid naming conflicts. If a class name is long or there's chance a class name might conflict with another class name in your script, using a shorter or more specific alias makes the code clearer.)
