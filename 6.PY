# . Verificación de número primo: Usa un ciclo for para verificar si un número es 
# divisible por algún número entre 2 y su raíz cuadrada. Si no tiene divisores, es 
# primo.
# Importo la funcion sqrt de la libreria standar math.
from math import sqrt
# Informo al usuario que debe ingresar un numero
print("Ingrese el numero que desea consultar si es primo(N):")
# Leo el numero ingresado por el usuario en la consola
number=  int(input())
# Inicializo un contador de divisores, los contadores generalmente se inician en cero.
divisors=0
# calulo la raiz cuadrada
sqr=int(sqrt(number))
# iterar entre 2 y la raiz cuadrada para contar los divisores del numero, si los tiene
for i in range(2,sqr+1):
    if number%i ==0: # utilizo la funcion modulo para saber si el numero es divisible por el nro actual en el for
        divisors=divisors+1 # aumento el contador de divisores
# Finalizado el for, verifico si se encontraron divisores o no, si no se encontraron divisores el numero es primo
# De lo contrario NO es primo.
if divisors==0:
    print("SI ES PRIMO")
else: 
    print("NO ES PRIMO")  





