# . Media de una lista de números: Recorre cada elemento de una lista con un 
# ciclo for, acumula su suma y divide entre el número total de elementos para 
# calcular la media.


print("Ingrese la lista de números separados por coma, sin espacios")
number_list = input()
numbers = number_list.strip().split(',')
suma=0

print(numbers)
cuenta=0
for number in numbers:
    suma=suma+int(number) 
    cuenta=cuenta+1
    
if cuenta > 0: 
    promedio=suma/cuenta
    print(f"El promedio de la lista de numeros es  {promedio} ")

  




