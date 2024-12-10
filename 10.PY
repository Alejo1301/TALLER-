# Cantidad de dígitos de un número: Usa un ciclo for para recorrer los 
# caracteres de un número convertido a cadena de texto y cuenta cuántos tiene.


number=str(123456789)   
cadena=str(number)
contar=0
for texto in cadena:
    contar+=1
print(f"la cantidad de digitos en el numero es {contar}")

