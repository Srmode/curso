### lists ###
my_list = list() #se puede crear una lista vacia con list() o con []
my_other_list = []
print(len(my_list)) #len() es para saber la longitud de la lista

my_list = [35, 24, 62, 52, 12]
print(my_list)
print(len(my_list))

my_other_list = [35, 35, 24, 62, 52, 12, "Adan", "Ambriz", 22.5, True]
print(my_other_list)
print(my_other_list[-1]) #para acceder a un elemento de la lista se puede usar el indice, empezando desde 0, y para acceder al ultimo elemento se puede usar -1
print(my_other_list[1])
print(my_other_list.count(35)) #count() es para contar cuantas veces aparece un elemento en la lista en el () se le pone el parametro que se quiere contar

#append() es para agregar un elemento al final de la lista
my_list.append("Python") 
print(my_list)

#insert() es para insertar un elemento en una posicion especifica de la lista, el primer parametro es el indice y el segundo es el elemento
my_list.insert(1, "Inserted") 
print(my_list)
#remove() es para eliminar un elemento de la lista, si hay varios elementos iguales, elimina el primero que encuentra
my_list.remove(62) 
print(my_list)

#el pop() es para eliminar un elemento de la lista por su indice, si no se le pone un indice, elimina el ultimo elemento
my_list.pop()
print(my_list)
#pop() es para eliminar un elemento de la lista por su indice
my_popped_element = my_list.pop(2) #si no se le pone un indice, elimina el ultimo elemento
print(my_popped_element)