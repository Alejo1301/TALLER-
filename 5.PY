# Tabla de multiplicar de un número: Genera la tabla de multiplicar de un 
# número dado del 1 al 10 utilizando un ciclo for. Por cada iteración, calcula el 
# producto y muéstralo

print("Ingrese el valor que desea calcular en la tabla de multiplicar(N):")
number=  int(input())

for i in range(1,11):
    product=number*i
    print(f"{number} x {i} = {product}")


