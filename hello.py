#prueba de push
import string
vMundo = "El mundo es gay"
print(vMundo)
#-----Parte del curso de udemy
#-----Program for adding two numbers 
print("Enter two numbers to add")
#el input es para pedir una variable al usuario en consola
cadena = input("Enter your name: ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# Adding two numbers
#el int() es para convertir la variable a un entero, aqui puede cambiarse a float() para convertir a decimal
sum = int(num1) + int(num2)
#para concatenar variables y texto se puede usar la coma o el signo +, pero con el signo + hay que convertir las variables a string
#capwords es para poner la primera letra de cada palabra en mayuscula 
print(string.capwords(cadena), num1, "and", num2, "is", sum)