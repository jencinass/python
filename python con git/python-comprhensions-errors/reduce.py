
import functools

numbers = [2,2,3,4,5,19]

def accum(counter, item):
	print('counter ',counter)
	print('item ', item)
	return counter + item

result = functools.reduce(accum, numbers)

print(result)