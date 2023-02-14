def increment(x):
	return x + 1

#Funcion tipo lambda
increment_v2  = lambda x : x + 1

result = increment_v2(120)
print(result)

full_name = lambda name,last_name : f'full name es {name.title()} {last_name.title()}'

text = full_name('nicolas','encinas')
print(text)