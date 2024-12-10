# Cantidad de vocales en una cadena: Recorre cada carácter de una cadena 
# de texto con un ciclo for y cuenta cuántos de ellos son vocales.

text= "Primero resuelve el problema y después escribe el código"
Contador= 0
for caracter in text:
         if caracter == "a":
             Contador +=1
         if caracter == "e":
             Contador +=1
         if caracter == "i":
             Contador += 1
         if caracter == "o":
             Contador +=1
         if caracter == "u" :
             Contador +=1
print(f"la cantidad de vocales en el texto son : {Contador}")
 

