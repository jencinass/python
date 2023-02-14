numbers = []

for element in range(1,11):
	numbers.append(element * 2)

print(numbers)

#List compprhensions
numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)