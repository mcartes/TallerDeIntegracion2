from pymongo import MongoClient
import json
from bson.objectid import ObjectId

def Export(Ip):
    client = MongoClient('localhost')

    db = client['Registro']

    columna = db['Usuario']

    x = columna.find_one({"_id":Ip})

    x["_id"] = str(ObjectId())

    with open("xd.json", "w") as fp:
        json.dump(x, fp)

#Funcion para subir archivos .json a MongoDB
def Import(Archivo):

    client = MongoClient('localhost')

    db = client['Registro']

    columna = db['Usuario']

    with open('Archivo') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        columna.insert_many(file_data) 

    else:
        columna.insert_one(file_data)
    
#Funcion para subir usuarios a MangoDB 
def Up(columna, nombre, correo, password):

    #Revisa si el usuario existe...
    if(columna.find_one({"name": nombre}) != None):
        print("Usuario Existente...")

    #Revisa si el correo existe...
    elif(columna.find_one({"correo": correo}) != None):
        print("Correo Existente...")

    #Añade al usuario
    else:
        bomba = columna.insert_one({"_id":str(ObjectId()),"name": nombre, "correo": correo, "contra": password})
        print("Agregado Correctamente...")
        
#Conexion con MongoDB       
client = MongoClient('localhost')

#Base de datos
db = client['Registro']

#Coleccion de la base de datos
columna = db['Usuario']

Export("6147d8897e7f3556a6b4d11d")
#Import()

#Up(columna, "Xalodfhjsaf4", "Jual.cfdnsom", "wdyastv")
# Devolver $Oid
#x = columna.find_one({"name": "Xalo2312"},{})
#print(x["_id"])

#Creacion de Identificador 
#str(ObjectId())





