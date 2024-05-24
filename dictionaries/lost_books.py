lost_books = {"The Bitter Glass": ["Eilís Dillon", "$11.88"], "If I Stay": ["Gayle Forman", "$17.00"], "Moonwalking with Einstein": ["Joshua Foer", "$34.95"]}
for key,value in lost_books.items():
	print(key, "by", value[0], "can be bought on Amazon for", value[1])
print()
print (lost_books["The Bitter Glass"])
print()
ssn = lost_books.get("ssn", "That key does not exist")
print(ssn)
print()
del lost_books["Moonwalking with Einstein"]
for key,value in lost_books.items():
	print(key, "by", value[0], "can be bought on Amazon for", value[1])
