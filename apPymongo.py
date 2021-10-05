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

    with open(Archivo, encoding = 'utf8') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        columna.insert_many(file_data) 

    else:
        columna.insert_one(file_data)

def Acceso(user, password):
    client = MongoClient('localhost')

    db = client['Registro']

    columna = db['Usuario']

    dou = columna.find_one({"name": user})

    if(dou != None):
        if(dou["contra"] == password):
            return("Acceso confirmado...")
        else:
            return("Contraseña incorrecta...")
    else:
        return("Usuario No Registrado...")
     

#Funcion para subir usuarios a MangoDB 
def Registro(nombre, password):
    client = MongoClient('localhost')

    db = client['Registro']

    columna = db['Usuario']
    #Revisa si el usuario existe...
    if(columna.find_one({"name": nombre}) != None):
        print("Usuario Existente...")

    #Revisa si el correo existe...
    # elif(columna.find_one({"correo": correo}) != None):
    #     print("Correo Existente...")

    #Añade al usuario
    else:
        a = columna.insert_one({"_id":str(ObjectId()),"name": nombre, "contra": password})
        print("Agregado Correctamente el Usuario: ", nombre)
        dou = columna.find_one({"name": nombre})
        db = client[dou["_id"]]
        columna = db["Documents"]
        columna.insert_one({"_id":str(ObjectId()),"Bienvenida": "Un gusto recibirte"})


def consultar(a):
    client = MongoClient('localhost')

    db = client['Registro']

    columna = db['Usuario']

    x = columna.find(a)
    
    print(str(list(x)))

#Conexion con MongoDB       
#client = MongoClient('localhost')
#ad = input("Ingrese: ")
#consultar(ad)

# #Base de datos
#db = client['Registro']

# #Coleccion de la base de datos
#columna = db['Usuario']

#Export("6147d8897e7f3556a6b4d11d")
#Import("jsontaller2.json")

#Up(columna, "Ññ", "Jfdnsom", "wastv")
# Devolver $Oid
#x = columna.find_one({"name": "Xalo2312"},{})
#print(x["_id"])

#Creacion de Identificador 
#str(ObjectId())

Up(db['Usuario'],"Francisco", "skdjskdj@gmail.com","sexo123")






