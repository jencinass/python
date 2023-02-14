
items = [
	{
		'product':'camisa',
		'price':100,
	},
	{
		'product':'pantalon',
		'price':300
	},
	{
		'product':'pantalon2',
		'price':320
	}
]

prices = list(map(lambda item: item['price'], items))

print(prices)

def add_taxes(item):
	new_item = item.copy()
	new_item['taxes'] = new_item['price'] * .19
	return new_item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)


def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)