import csv
import matplotlib.pyplot as plt
def isAltaDemanda(cant):
    if cant > 50:
        return "Alta Demanda"
    return "Baja Demanda"
inventario = {"Papel": 40, "Lapiz": 32,"Borrador":90, "Regla": 12,
              "Colores":25, "Pegamento":50,"Tijeras":60, "Mochila":16,
              "Cuadernos":80, "Carpetas":20}
total = sum(inventario.values())
maxProd = max(inventario.values())
minProd = min(inventario.values())
data = []
for name, cant in inventario.items():
    data.append({"Producto": name,
                 "Cantidad": cant,
                 "Demanda": isAltaDemanda(cant)})
# acompletar datos
data.append({"Producto": "Total",
             "Cantidad": total,
             "Demanda": "indefinido"})
data.append({"Producto": "Producto mas demandado",
             "Cantidad": maxProd,
             "Demanda": "indefinido"})
data.append({"Producto": "Producto menos demandado",
             "Cantidad": minProd,
             "Demanda": "indefinido"})
# guardar csv
with open("tienda.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Producto", "Cantidad", "Demanda"])
    writer.writeheader()
    writer.writerows(data)
print("csv impreso")
with open("calificaciones.csv",newline="",encoding="utf-8")as archivo:
    lector = csv.DictReader(archivo)
    datos = list(lector)

plt.bar([fila["Producto"] for fila in data], [int(fila["Cantidad"]) for fila in data], color="skyblue", edgecolor="black")
plt.title("Ventas por producto")
plt.xlabel("Productos")
plt.ylabel("Cantidad")

# mostrar la tabla
plt.show()
