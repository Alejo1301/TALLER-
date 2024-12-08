# Máximo común divisor (MCD): Encuentra el MCD de dos números utilizando 
# el algoritmo de Euclides con un ciclo while, que repite el cálculo del residuo 
# hasta que uno de los números sea cero


print("Vamos a calcular el MCD de dos números[MCD(A,B)] utilizando el algoritmo de euclides.")
print("Por favor ingrese el número A:")
A = int(input())
print("Por favor ingrese el número B:")
B = int(input())

a, b = A, B # Asigno los números a variables que pueden cambiar durante el ciclo while

#Debo asegurarme que A sea mayor que B para  que el algoritmo funcione de la forma simplificada
# Algoritmo de Euclides: Suponiendo que A es mayor que B se define como: MCD(A, B) es igual a:
# Si B = 0, entonces, A
# De lo contrario, MCD(B, A % B) que se lee como el MCD de B, y el residuo de A divido B.

if a < b:
    a, b = b, a # Invertimos los valores de las variables para garantizar que A sea mayor que B

while b > 0:
    a, b = b, a % b # Recalculo los valores de A y B para una nueva iteración
print (f"MCD({A}, {B}) = {a}")


