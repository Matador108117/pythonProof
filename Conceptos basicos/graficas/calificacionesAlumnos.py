import csv
import matplotlib.pyplot as plt
def isAprobado(calf):
    if calf > 5:
        return "Aprobado"
    return "Reprobado"
calificaciones = {"Nancy": 10, "Ernesto": 9,"Rafael": 9, "Abraham": 8,
                  "Mauricio": 10, "Ricardo": 9, "Carlos":6, "Carmen": 5,
                  "Andres": 4, "Marcos": 8}

maxcalf = max(calificaciones.values())
mincalf = min(calificaciones.values())
promedio = sum(calificaciones.values()) / len(calificaciones.values())
data = []
for name, calf in calificaciones.items():
    data.append({
        "Nombre": name,
        "Calificacion": calf,
        "Estatus": isAprobado(calf)
    })

# acompletar datos 
data.append({
    "Nombre": "Promedio",
    "Calificacion": promedio,
    "Estatus": "indefinido"
})
data.append({
    "Nombre": "Calificacion maxima",
    "Calificacion": maxcalf,
    "Estatus": "indefinido"
})
data.append({
    "Nombre": "Calificacion minima",
    "Calificacion": mincalf,
    "Estatus": "indefinido"
})

# guardar csv
with open("calificaciones.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Nombre", "Calificacion", "Estatus"])
    writer.writeheader()
    writer.writerows(data)

print("csv impreso")

# leer csv
with open("calificaciones.csv",newline="",encoding="utf-8")as archivo:
    lector = csv.DictReader(archivo)
    datos = list(lector)

plt.bar([fila["Nombre"] for fila in datos], [float(fila["Calificacion"]) for fila in datos], color="skyblue", edgecolor="black")
plt.title("Calificaciones por Alumno")
plt.xlabel("Alumnos")
plt.ylabel("Calificación")

# mostrar la tabla
plt.show()

