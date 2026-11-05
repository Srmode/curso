import sys
print('Programa para imprimir numeros pares del 1 al 100')
cnt = 0
lim = int(input('Ingrese un numero positivo para establecer un rango: '))
if lim < 0:
    print('El numero ingresado no es positivo')
    sys.exit()
while cnt <= lim:
    if cnt % 2 == 0:
        print(cnt,'es un numero par')
    cnt += 1
print('todos los numeros pares suben hasta',lim)

#for loop
lst = ['car', 'bus', 'bike', 'train']
for i in lst:
    print(i)

print('Programa para imprimir numero pares en un rango positivo')
startNum = int(input('Ingrese un numero positivo (bajo)')or 0)
endNum = int(input('Ingrese un numero positivo (alto)')or 0)
if startNum < endNum and startNum >= 0 and endNum >= 0:
    z = range(startNum, endNum + 1)#enNum +1 para incluir el numero final
    for i in z:
        if i % 2 == 0:
            print(i, 'es un numero par')
    #para los for tamvbien se puede usar un else, que se ejecuta cuando el for termina de iterar
    #el else se ejecuta si el for termina normalmente, es decir, sin un break y si hay un break, el else no se ejecuta
    else:
        print(f'El rango de numeros pares es de {startNum} a {endNum}')
else:
    print('El rango ingresado no es valido, el primer numero debe ser menor que el segundo y ambos deben ser positivos')