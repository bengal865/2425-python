def printDictionary(li):
	for key, value in li.items():
		print(f'{key}: {value}')

lost_books = {
'book1': ['Grudge Bearer', 'Gavin Thorpe', '$4.69'],
'book2': ['Dragons of Autumn Twilight', 'Tracy Hickman & Margaret Weis', '$29.95'],
'book3': ['Dragons of Winter Night', 'Tracy Hickman & Margaret Weis', '$24.74']
}

printDictionary(lost_books)

print(lost_books['book1'])
print(lost_books.get('book4'))

del lost_books['book3']

printDictionary(lost_books)
