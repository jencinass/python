try:
	print(0/0)
	assert 1 != 1, 'uno no es diferente que uno'
	age = 10
	if age < 18:
		raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
	print('this is an error')
except AssertionError as error:
	print(error)
except Exception as error:
	print(error)

print('running...')