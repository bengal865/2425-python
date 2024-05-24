# Programmer: Bruce Provencher
# Date: 01 NOV 2016
# Favorite Programming Languages

favorite_languages = {

    'Noa':['python', 'ruby'],
    'Martin':['c++', 'ruby on rails'],
    'Hannah':['ruby', 'javascript'],
    'James':['perl', 'java', 'c#']
}

print("Printing the contents of the dictionary...\n")
print(favorite_languages, "\n") # Print original dictionary
# Deleting a KEY also deletes the value linked to that key
del favorite_languages['Noa']

print("Printing the dictionary after deleting 1 key:value pair...\n")

print(favorite_languages) # Reprint the modified dictionary

print()

print("End of script!")


