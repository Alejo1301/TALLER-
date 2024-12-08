# Factorial de un número dado: Encuentra el factorial de un número 
# multiplicando todos los números desde 1 hasta ese número con un ciclo for. 
# Asegúrate de inicializar la variable acumuladora en 1

print("Ingrese el numero factorial (N):")
j=  int(input())
factorial=1
for i in range(1, j+1):
    factorial=factorial*i
print(f"El factorial de {j} es :",factorial)
