# 3. Números pares del 1 al 100: Usa un ciclo for para recorrer los números del 1 
# al 100 e imprime solo aquellos que sean divisibles entre 2 (números pares)
print("los numeros pares del 1 al 100 son:")
cuenta=0
for value in range(1,101):
    if value % 2==0:
        cuenta=cuenta+1
        print(value)
print(f"la cantidad de numeros pares es de: {cuenta}")















































