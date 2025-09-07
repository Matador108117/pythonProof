import csv 
data = [{"nombre": "Rafael","equipo": "cruza azul", "goles": 10, "edad":21 },
        {"nombre": "Marcos","equipo": "Pumas", "goles":3, "edad":20},
        {"nombre": "Luis", "equipo": "Chivas", "goles": 5, "edad":34},
        {"nombre": "Carlos", "equipo": "Monterrey", "goles": 8, "edad":22},
        {"nombre": "Javier", "equipo": "Santos", "goles": 2, "edad":18},
        {"nombre": "Miguel", "equipo": "Toluca", "goles": 4, "edad":19},
        {"nombre": "Fernando", "equipo": "Leon", "goles":5, "edad":32},
        {"nombre": "Andres", "equipo": "Tigres", "goles":3, "edad":27},
        {"nombre": "Juan", "equipo": "Atlas", "goles":2 , "edad":28},
        {"nombre": "Pedro", "equipo": "Puebla", "goles":1, "edad":29}
        ]
maxGolesPlayer = {"nombre": "","equipo": "nada", "goles": 0, "edad":0}
for player in data:
    if player ["goles"] > maxGolesPlayer["goles"] :
        maxGolesPlayer = player
minEdadesPlayer = {"nombre": "","equipo": "nada", "goles": 0, "edad":100}
for player in data: 
    if player ["edad"] < minEdadesPlayer["edad"]:
        minEdadesPlayer = player
for player in data:
    print(str(player))
promedioGoles = sum(player["goles"] for player in data) / len(data)
promedioEdad = sum(player["edad"] for player in data) / len(data)

datas = []
datas.append({"tipo": "Máximo de goles", **maxGolesPlayer})
datas.append({"tipo": "Mínima edad", **minEdadesPlayer})
datas.append({"tipo": "Promedio de goles", "nombre": "", "equipo": "", "goles": promedioGoles, "edad": ""})
datas.append({"tipo": "Promedio de edad", "nombre": "", "equipo": "", "goles": "", "edad": promedioEdad})

with open("jugadores.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["tipo","nombre", "equipo", "goles","edad"])
    writer.writeheader()
    writer.writerows(data)
