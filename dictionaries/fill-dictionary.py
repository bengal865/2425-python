# Fill dictionary with terms and definitions

glossary = {}

# Set flag for while loop
keep_looping = True
while keep_looping:
    # Prompt user for term and corresponding defintion
    term = input('Please enter a term you wish to add to the glossary: (Example: dog)\n')
    definition = input('Enter a brief definition of the term:\n')

    # Store response in dictonary
    glossary[term] = definition

    # Add more terms and definitions to the glossary?
    repeat = input('Do you wish to add another term to the glossary? (y/n)\n').lower()
    if repeat in ['n', 'no']:
        keep_looping = False

# User doesn't want to add any more terms, so show
# the contents of the glossary
print('\n----- Glossary Contents -----')
for term, definition in glossary.items():
    print(f'{term}: {definition}')