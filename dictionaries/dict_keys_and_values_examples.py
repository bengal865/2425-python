# Bruce Provencher
# 11 JAN 2019
# Dictionary Keys & Values Examples

foreign_languages = {'Joe' : 'Spanish', 'Alyssa' : 'Chinese', 'Nick' : 'German'}

# Print all the keys using a FOR loop

print("The students studying a foreign language this year are:")
for speaker in foreign_languages.keys():
	print(speaker)

print()
print()

# Print the keys in order (sort the keys)
for speaker in sorted(foreign_languages.keys()):
	print(f"{speaker} is studying a foreign language this year.")

print()
print()

# Loop through dictionary and print just the values (not the keys)
print("This year, students are studying the following languages:")
for lang in foreign_languages.values():
	print(lang)