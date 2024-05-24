# Programmer: Bruce Provencher
# Date: 05 OCT 2020									
# Project: Python List Methods

'''
1. Create two lists -- an original and a copy.
2. Apply your list methods to the copy.
3. Print the original AND the modified list so you can see the differences between the two lists.
4. Also print/display the name of the method you applied to your (copied) list.

Demonstrate you know how to use these list methods:

* append ()
* insert ()
* remove ()
* count ()
* clear ()
* pop ()
* reverse ()

Also show you know how to use the DEL (delete) statement with your list.

See the Google slideshow 'Python List Methods 2' for more information
about Python list methods.

'''

# Create a list of animals
animals = ["tigers", "guinea pigs", "yaks", "leopards"]

# Use the copy method to make a copy of the original list
new_animals = animals.copy()

# Print the original and the copied list
print(f'''
	Original list: {animals}
	Copied list: {new_animals}
''')

# Applying the APPEND method 
# to the copied list
animal1 = 'grizzly bear'
new_animals.append(animal1)
print(f'''
	Original list: {animals}
	Modified list after APPEND: {new_animals}
''')


# Applying the INSERT method 
# to the copied list
animal2 = 'mountain lion'
new_animals.insert(2, animal2)
print(f'''
	Original list: {animals}
	Modifed list after INSERT: {new_animals}
''')
