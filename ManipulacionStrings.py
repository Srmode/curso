s = 'pythongeek'
print (s[0:6]) # prints 'python'
print (s[6:]) 
print (s[2]) #le puedes decir que imprima la letra en la posicion 2 de la cadena, en este caso la letra t
print (s[-2]) # prints 'e'
#Variables:
#las variables tiene varias tipos de datos, como enteros, flotantes, cadenas, listas, tuplas, diccionarios, etc
#las cuales se pueden ver con la funcion type(), y asu vez se pueden convertir de un tipo a otro con las funciones int(),
#  float(), str(), list(), tuple(), dict(), etc.

#para ver el espacio de las variables en memoria se puede usar la funcion sys.getsizeof(), 
# para esto hay que importar el modulo sys

#tipo de datos:
#los tipos de datos mas comunes some: int, float, str, list, tuple, dict, set, bool
print(type(s)) #int
lst = [1, 2, 3, 4, 5,'boston']
print(type(lst)) #list
print(lst[2]) # prints 3
#para declarar una variable rango se puede usar la funcion range(), la cual genera una secuencia de numeros enteros, 
# y se puede especificar el inicio, el fin y el paso de la secuencia
rng = range(2,11,3)
print(type(rng)) #range
print(list(rng)) # prints [2, 5, 8]
mydict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(mydict['name']) # prints 'John'
print(mydict.keys()) # prints dict_keys(['name', 'age', 'city'])