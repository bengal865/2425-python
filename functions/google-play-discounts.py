def get_prices():
	prices = []
	for x in range(3):
		item_price = float(input(f'Please enter price for Item {x + 1}: (Example: 6.99)\n'))
		prices.append(item_price)
		
	return prices
	
def apply_ten_discount(order_total):
	discounted = order_total * 0.90
	return discounted
	
	
def apply_twenty_five_discount(order_total):
	discounted = order_total * 0.75
	return discounted
	
	
def apply_discount(order_total):
	if order_total <= 10:
		discounted_price = apply_ten_discount(order_total)
		discount_msg = f'With a 10% discount, your price today is: ${discounted_price:,.2f}'
	elif order_total > 10:
		discounted_price = apply_twenty_five_discount(order_total)
		discount_msg = f'With a 25% discount, your price today is: ${discounted_price:,.2f}'
	return discount_msg
	

my_list = get_prices()

# print(f'\n{sum(my_list):,.2f}\n')
my_total = sum(my_list)

output_msg = apply_discount(my_total)
print('Order Summary:')
print(f'\nTotal: ${my_total:,.2f}')
print(output_msg)
