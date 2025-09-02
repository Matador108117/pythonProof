#lista de calificaciones

calificaciones = [8,9,9,10,10,10,10,10,8,8,9,9,10]
#calcular el promedio
promedio = sum(calificaciones)/len(calificaciones)
print('El promedio es:'+str( promedio))
    
    # maximo y minimo 
print(max(calificaciones), min(calificaciones))

    # imprimir el numero de aprobados 
aprobados = 0
for c in calificaciones:
    if c >= 7:
            aprobados += 1
print('El numero de aprobados es: '+ str(aprobados))
