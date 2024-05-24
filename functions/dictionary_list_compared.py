# Dictionaries and Lists Compared

languages = ['python', 'c++', 'java', 'ruby']

print('Output from the list:\n')
print(f"Jen's favorite language is {languages[0].title()}.")
print(f"Sarah's favorite language is {languages[1].title()}.")
print(f"Phil's favorite language is {languages[2].title()}.")
print(f"Ben's favorite language is {languages[3].title()}.")

# Print two blank lines for spacing purposes
print()
print()

favorite_languages = {	
	"jen" : "python",
	"sarah" : "c++",
	"phil" : "java",
	"ben" : "ruby"
}

for key in favorite_languages.keys():
	print(f'- {key}')

print()
print()
for value in favorite_languages.values():
	print(f'> {value}')

print()
print()

for key, value in favorite_languages.items():
	print(f'Key is: {key.title()}')
	print(f'Value is: {value.title()}\n')


print()
print()
# print()
# print('Output from the dictionary:\n')
# print(f"Jen's favorite language is {favorite_languages['jen'].title()}.")
# print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")
# print(f"Phil's favorite language is {favorite_languages['phil'].title()}.")
# print(f"Ben's favorite language is {favorite_languages['ben'].title()}.")
# print()
# print('Printing all the dictionary items...')
# print(favorite_languages.items())
# print()
# print('Printing only the dictionary keys...')
# print(favorite_languages.keys())
# print()
# print('Printing only the dictionary values...')
# print(favorite_languages.values())
# print()