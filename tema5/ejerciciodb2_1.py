from pymongo import MongoClient

cliente = MongoClient()
db = cliente.ParticulasDB

query1 = db.Iniciales.find({"pos.2":0})

print ("Z = 0: \n")

for particula in query1:
    
    print(particula)


query2 = db.Iniciales.find ({"$or":[{"vel.2":0},{"vel.0":0},{"vel.1":0}]})

print ("Z = 0 o X = 0 o Y = 0: \n")

for particula in query2:
    print(particula)

    


query3 = db.Iniciales.find({"$and":[{"pos.0":{"$gt":0}},{"pos.0":{"$lt":1.2}}]})

print ("X in (0,1.2): \n")

for particula in query3:
    print(particula)



query4 = db.Iniciales.find({"$and":[{"vel.0":0},{"vel.1":0},{"vel.2":0}]})

print (" Vxyz ) 0: \n")

for particula in query4:
    print(particula)

