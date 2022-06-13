price = float(input('Enter price of item: '))
tax_percentage = float(input('Enter tax percentage: '))

def price_compare(price, tax_percentage):
  tax_rate = tax_percentage / 100
  item_tax = tax_rate * price
  item_with_tax = item_tax + price

  return "Base price: ${:.2f}. With Tax: ${:.2f}".format(price, item_with_tax)

print(price_compare(price, tax_percentage))