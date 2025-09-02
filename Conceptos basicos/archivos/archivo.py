# leer csv
import csv

with open("data.csv",newline="",encoding="utf-8")as archivo:
    lector = csv.DictReader(archivo)
    datos = list(lector)
# calcular la edad promedio
edades = [int(fila["Edad"]) for fila in datos]
promedio = sum(edades) / len(edades)
print("la edad promedio es: ", promedio)