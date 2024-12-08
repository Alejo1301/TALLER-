#Suma de los primeros n números naturales:
#Calcula la suma de los números desde 1 hasta n utilizando un ciclo for.
#Itera sobre los números en el rango de 1 a n y acumula su suma.

print("Ingrese el valor final (N):")
J=  int(input())
suma=0
for i in range(1, J+1):
     print(i)
     suma=suma+i    
print("la suma es:",suma)


