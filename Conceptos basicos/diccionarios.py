alumnos = {'Rafael': 20, 'Uriel': 20, 'Abraham':22, 'marcos': 40}
# agregar un elemento 
alumnos['Carlos'] = 23
#alumnos mayores de 22
mayores = [alumno for alumno, edad in alumnos.items() if edad >22]
print(mayores)
promedio = sum(alumnos.values()) / len(alumnos)
print (promedio)