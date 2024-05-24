# Garrett Sedwick
# APR 16 2021
# Dictionaries practice

import random;
favorite_language = {"name": '',
"language": ''};
i = 0;
names = ["John", "Dave", "Rose", "Jade", "Jake", "Dirk", "Roxy", "Jane"];
languages = ["python", "Java", "Html", "Css", "Javascript"];

while i < 5 :
	favorite_language["name"] = random.choice(names)
	favorite_language["language"] = random.choice(languages)
	i = i + 1
	print(f"{favorite_language['name']}'s favorite language is {favorite_language['language']}")

