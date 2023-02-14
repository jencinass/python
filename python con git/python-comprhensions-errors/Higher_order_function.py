
def increment(x):
	return x + 1

incrementv2 = lambda x: x + 1


def high_order_function(x, func):
	return x + func(x)

high_order_functionv2 = lambda x, func: x + func(x)

result = high_order_function(2, increment)
print(result)

result = high_order_function(2, incrementv2)
print(result)

result = high_order_functionv2(3, lambda x: x*2)
print(result)