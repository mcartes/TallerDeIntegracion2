from pymongo import MongoClient
import json

#Funcion para subir archivos .json a MongoDB
def jsonUp():

    client = MongoClient('localhost')

    db = client['Registro']

    columna = db['Usuario']

    with open('Usuario3.json') as file:
        file_data = json.load(file)

    print(file_data)
    if isinstance(file_data, list):
        columna.insert_many(file_data)  
    else:
        columna.insert_one(file_data)
    
#Funcion para subir usuarios a MangoDB 
def Up(columna, nombre, correo, password):

    #Revisa si el usuario existe...
    if(columna.find_one({"name": nombre}) != None):
        print(columna.find_one({"name": nombre},{}))
        print("Usuario Existente...")

    #Revisa si el correo existe...
    elif(columna.find_one({"correo": correo}) != None):
        print("Correo Existente...")

    #Añade al usuario
    else:
        bomba = columna.insert_one({"_id":columna.count_documents({})+1,"name": nombre, "correo": correo, "contra": password})
        print(bomba.inserted_id)
        print("Agregado Correctamente...")
        
#Conexion con MongoDB       
client = MongoClient('localhost')

#Base de datos
db = client['Registro']

#Coleccion de la base de datos
columna = db['Usuario']

# Devolver $Oid
#x = columna.find_one({"name": "Xalo5"},{})
#print(x["_id"])






