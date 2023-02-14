

#Funciones
##
def my_print(text):
	print(text)

my_print('hi my friend')

def suma(a,b):
	print(a+b)

suma(15.45, 0.5)



def suma_with_range(a,b):
	print(a,b)
##RETURN
	suma = 0
	for x in range(a,b):
		suma += x
	return suma

sum_total = suma_with_range(5,15)

print(sum_total)







