
def calculate_state_tax(price):
    state_sales_tax_rate = .05
    return price * state_sales_tax_rate

def calculate_grand_total(price):
    state_sales_tax_rate = .05
    return price + (price * state_sales_tax_rate)

def display_totals(price):
    print(f'Purchase Price: ${price:,.2f}')
    state_tax = calculate_state_tax(price)
    grand_total = calculate_grand_total(price)
    print(f'State Sales Tax: ${state_tax:,.2f}')
    print(f'Grand Total: ${grand_total:,.2f}')

def main():
    price = float(input('Enter the price of the item you purchased (Example: 6.99): '))
    display_totals(price)
    
main()