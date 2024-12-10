# . Suma de los dígitos de un número: Recorre cada dígito de un número 
# (convirtiéndolo en una cadena de texto) y suma sus valores utilizando un 
# ciclo for.

print("ingrese un numero para sumar sus digitos")
number=input()
suma=0
for digit in number:
    suma=suma+int(digit)
print(f"la suma de los digitos de {number} es:{suma}")    

