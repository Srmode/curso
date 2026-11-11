### Strings ###
my_string = "my string"
my_other_string = 'my other string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
my_new_line_string = "This is a string\nwith a new line"
print(my_new_line_string)
my_tab_string = "\tThis is a string with a tab"
print(my_tab_string)
my_scape_string = "\\tThis is a string \\n with a tab"
print(my_scape_string)
#formateo
#para formatear un string con %s y %d, 
#para formatear y concatenar datos en string, se puede usar el metodo format() o el metodo f-string
#empezando con .format()
#se peude formatear poniendo una f al print y poniendo las variables entre llaves {}
name, surename, age = "Adan", "Ambriz", 22
print("mi nombre es {} {} y tengo {} años".format(name, surename, age))
print("mi nombre es %s %s y tengo %d años" %(name, surename, age))
print(f"mi nombre es {name} {surename} y tengo {age} años")

# Desempaquedo de variables
#el empaquetado de variables es cuando se asigna un valor a una variable, y el desempaquetado es cuando se asigna un valor a varias variables al mismo tiempo
lenguaje = "python"
a , b , c , d , e , f = lenguaje
print(a)
print(b)

#division 
lenguaje_slice = lenguaje[1:3] #el primer numero es el inicio y el segundo es el final, el final no se incluye
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:] 
print(lenguaje_slice)

#reverse
reverse_lenguaje = lenguaje[::-1] #el -1 es para invertir el string
print(reverse_lenguaje)

#funciones, para ver todas las funciones de un string se puede usar dir(string) y para ver la documentacion de una funcion se puede usar help(string.funcion)
#se puede usar la funcion capitalize() para poner la primera letra en mayuscula, upper() para poner todas las letras en mayuscula, lower() para poner todas las letras en minuscula, count() para contar cuantas veces aparece una letra, isnumeric() para saber si es un numero, isalpha() para saber si es una letra
#debes siempre poner un punto despues de la variable para poder usar las funciones, por ejemplo lenguaje.capitalize()
print(lenguaje.capitalize()) #la primera letra en mayuscula
print(lenguaje.upper()) #todas las letras en mayuscula
print(lenguaje.lower()) #todas las letras en minuscula
print(lenguaje.count("p")) #cuenta cuantas veces aparece la letra p
print(lenguaje.isnumeric()) #si es un numero
print(lenguaje.isalpha()) #si es una letra

