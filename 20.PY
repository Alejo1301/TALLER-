# Promedio ponderado: Calcula el promedio ponderado de una lista de 
# calificaciones. Multiplica cada calificación por su peso en un ciclo for y divide 
# entre el total de pesos

calificaciones=[5,4,3,5,3,2]
pesos=[0.2,0.1,0.5,0.5,0,2,0,4]
promedio_ponderado=0

for i in range (len(calificaciones)):
    promedio_ponderado += calificaciones[i]*pesos[i]
print(f"El promedio ponderado es:{promedio_ponderado}")