import matplotlib.pyplot as plt
edades = [20,22,19,31,44,23,19,18,24,25,24]

# metodo para crear un histograma apartir 
plt.hist(edades, bins=5, edgecolor="black")

#personalizar grafica
plt.title("Distribucion de las edades")

plt.xlabel("Edad")

plt.ylabel("Frecuencia")

# mostrar la tabla 
plt.show()
