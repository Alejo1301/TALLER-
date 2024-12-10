# .Número más grande en una lista: Compara los números de una lista uno por 
# uno utilizando un ciclo for para encontrar el mayor de ellos

number_list=(5,8,3,9,40,20)
maximo=(0)
for number in number_list:
    if number > maximo:
        maximo=number
print(f"el numero mas grade de la lista es {maximo}")

