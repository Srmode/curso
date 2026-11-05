import sys
print('Programa que compara numeros')
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
if num1 > num2:
    print(f'El numero {num1} es mayor que {num2}')
elif num1 < num2:
    print(f'El numero {num1} es menor que {num2}')
else:
    print(f'El numero {num1} es igual que {num2}')
#en los if siempre se pone : para indicar que se va a ejecutar un bloque de codigo, y 
# el bloque de codigo se indica con una sangria, es decir, un tabulador o 4 espacios
#demostratio of if with minimal code
r = 'son dos nuemros iguales' if (num1 == num2) else 'no son dos numeros iguales'
print(r)
#.upper() convierte a mayusculas
country = input('input country - A OR B: ').upper() or ' '
weigth = int(input('input parcel weigth in kgs : ') or '0')
if country in ['A', 'B'] and weigth > 0:
    if country == 'A':
        if weigth <= 5:
            print('The cost of shipping is $10')
        elif weigth <= 10:
            print('The cost of shipping is $20')
        else:
            print('The cost of shipping is $30')
    elif country == 'B':
        if weigth <= 5:
            print('The cost of shipping is $15')
        elif weigth <= 10:
            print('The cost of shipping is $25')
        else:
            print('The cost of shipping is $35')
else:
    print('Invalid input. Please enter a valid country (A or B) and a positive weight.')
    sys.exit()