numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(len(numbers)):
	if x == 0:
		print(f'{numbers[x]}st')
	elif x == 1:
		print(f'{numbers[x]}nd')
	elif x == 2:
		print(f'{numbers[x]}rd')
	else:
		print(f'{numbers[x]}th')
	
