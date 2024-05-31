# Lesson Plan: Building a Text Adventure 
**Grade Level:** 11th & 12th Grade
**Time Allotment:** 45 minutes
**Michigan State Standards:**

- CP.A2.2.2: Design and implement algorithms using fundamental data structures, such as lists and arrays.
- CP.A3.2.2: Apply selection control structures (if statements) to be introduced in Lesson 2.

**Key Terms & Concepts:**

- Lists
- Text adventure game
- Index number (for a Python list)
- Generating random numbers in Python

**Lesson Outline:**

**Introduction (Hook - 5 minutes)**

- Play a short, simple text adventure game with the class, where some events are triggered randomly (e.g., encountering a monster, finding a hidden item, etc.). After playing the game, ask students:
- How do you think the game chooses what happens next?
- What else could you do to make the game more exciting or challenging?

**Mini Lesson (8 minutes)**

- Explain text adventure games as a type of program that relies on user input and pre-defined options.
- Introduce lists as a way to store information in an ordered way.
- Demonstrate how a list can be used to store the different locations and descriptions in a text adventure game. (e.g., locations = ["forest", "cave", "castle"])

**Resources:**

- <https://www.w3schools.com/python/python_lists.asp>
- [Text-based adventure game in 11 minutes](https://youtu.be/ORsJn-71__0?feature=shared)
- [Playlist on YT: Text-based adventure game using functions](https://youtube.com/playlist?list=PLES3Y8j562C2ncjly27QLCz3TWuFlzKVq&feature=shared)
- [GitHub: Writing a Text-Based Adventure Game in Python](https://gist.github.com/dougmcnally/06fa0533a893b6e85222bb4f4645940f)
- [YT: Writing a Text-Based Adventure Game in Python](https://youtu.be/miuHrP2O7Jw?feature=shared)
- [Leon Mardsen/Making an Adventure Game in Python YT](https://youtu.be/EbAdsK8s0-U?feature=shared)

**Guided Practice Activities (22 minutes):**

- (10 minutes) Students will work in pairs. Each pair will create a list containing 3-5 locations for their own text adventure game. Encourage them to describe each location in a sentence within the list. (e.g., locations = ["forest (a dark and mysterious place)", "village (bustling with
activity)", "mountain peak (stunning views)"])

- (12 minutes) As a class, discuss how to use index numbers to access specific elements within a list. Demonstrate how to use positive and negative index numbers. Introduce the `random.randint()` function in Python for generating random numbers.

**Activity (10 minutes):**

- Have students brainstorm and write a short piece of code (2-3 lines) that uses the `random.randint()` function to access a random location from their list. Have students print the location associated with the selected index.

**Sample Code (Explanation provided in class):**

**Independent Practice (Approximately 15 minutes):**

- Students will begin working on their own simple text adventure game.
- Task 1: Create a list containing at least 3 locations for their game. Write comments in their code to explain what each list element represents.
- Task 2: Add code to their game that uses `random.randint()` to choose a starting location from their list; print the corresponding description.

**Assessment:**

- Review student-created lists, comments, and starting location code during the next class. **Differentiation:**
- **Advanced Students:** Challenge them to create a nested list within their location list. The nested list could hold additional details about each location (e.g., locations = ["forest (a dark and mysterious place, [monster: goblin, item: rusty sword])", ...]) They can also explore using random numbers to access elements within the nested list.
- **Struggling Students:** Provide lists of locations and descriptions for students to use in their game. Offer additional support as needed to help students understand how to use the `random.randint()` function.

  **Discussion Questions:**

1. Why might a list be a useful way to store data for a text adventure game? (**Possible Answer:** Lists allow us to store information in an organized way and easily access specific pieces of data you'd use in the game.)
1. How can indexing help us navigate through our list of locations? (**Possible Answer:** Indexing allows us to access specific locations in the list using their index number.)
1. How can we use random numbers to add an element of surprise to our text adventure game? (**Possible Answer:** We can use functions like random.randint() to randomly access elements within our lists, which introduces randomness and unpredictable outcomes in the game.)
