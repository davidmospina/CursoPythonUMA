from matplotlib.collections import Collection
from pymongo import MongoClient

cliente = MongoClient()
print(cliente.list_database_names())

db = cliente.Ejemplo1
print(db.list_collection_names())


# db.coleccion.insert_one({"nombre": "Enrique Soler", "profesion": "profesor", "correo": "esc@lcc.uma.es", "temas":[2,6]})

# otrosProfes = [
# {"nombre": "Luis Llopis", "profesion": "profesor", "correo":"luisll@lcc.uma.es", "temas" : [1,5,7]},
# {"nombre": "Daniel Garrido", "profesion": "profesor", "correo":"dgarrido@lcc.uma.es", "temas" : [3,4]}]

# db.coleccion.insert_many(otrosProfes)

# alumnos = [
# {"nombre": "Victor Mento", "estudios": "Ing. Mecánico", "correo": "vmento@uma.es" },
# {"nombre": "Lola Mento", "estudios": "Ing. Mecánico", "correo": "lmento@uma.es" },
# {"nombre": "Aitor Tilla", "estudios": "GIERM", "correo": "atilla@uma.es" },
# {"nombre": "Borja Mon de York", "estudios": "Ing. Electrónica", "correo": "byork@uma.es" },
# {"nombre": "Armando Adistancia", "estudios": "Ing. Electrónica", "correo": "adist@uma.es" }
# ]
# db.coleccion.insert_many(alumnos)

todos = db.coleccion.find()
print ("Mostramos todos")
for persona in todos:
    print(persona)

print ("Buscamos a Luis, pero solo nombre y correo")
unprofe = db.coleccion.find_one({"nombre": "Luis Llopis"},{"nombre":1, "correo": 1})
print(unprofe)


# db.coleccion.delete_many({})