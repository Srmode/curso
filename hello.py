#prueba de push
import string
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
#el == se utiliza para comparar variables, el = es para asignar un valor a una variable
#el != se utiliza para comparar variables si es diferente de otra variable
#para poder combinar operadores logicos se puede usar and, or, not
if num1 == num2 or num1 != 3:
    print("The numbers are equal")
elif num1 != num2:
    print("The numbers are not equal")
#el \ es para continaur el codigo en la siguiente linea, por ejemplo para poner comillas dentro de un print
#el \n es para hacer un salto de linea dentro de un print
print(' President said "I\'ll not run for re-election" ')
#el \t es para hacer un tabulador dentro de un print
#el \r es para hacer un retorno de carro dentro de un print
#el \b es para hacer un retroceso dentro de un print
#el \f es para hacer un salto de pagina dentro de un print
#el \v es para hacer un salto de linea vertical dentro de un print}
#el poner un numero desppues del paranteis es para repetir el print esa cantidad de veces ejemplo print(4*"Hello World\n") esto imprimira 5 veces Hello World
print(r'c:\Users\user\Desktop\python\hello.py')
#la f es para poder poner variables dentro de un print sin necesidad de concatenar con el signo +, solo se pone la variable entre llaves {}
print(f'newton discoverd {num1} and {num2} are equal')
