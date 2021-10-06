from pymongo import MongoClient
import json
from bson.objectid import ObjectId

def Export(Ip, Base, Colec):
    client = MongoClient('localhost')

    db = client[Base]

    columna = db[Colec]

    x = columna.find_one({"_id":Ip})

    x["_id"] = str(ObjectId())

    with open("xd.json", "w") as fp:
        json.dump(x, fp)

#Funcion para subir archivos .json a MongoDB
def Import(Archivo, Base, Colec):
    client = MongoClient('localhost')

    db = client[Base]

    columna = db[Colec]

    with open(Archivo, encoding = 'utf8') as file:
        file_data = json.load(file)

    #print(file_data['_id'])

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
            return('success', dou["_id"])
        else:
            return('BadPass')
    else:
        return('BadUser')
     

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


def consultar(con, Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]

    con = con.replace("'","")
    con = con.replace('"',"")
    con = con.replace("","")
    con = con.replace("{","")
    con = con.replace("}","")
    con = con.replace(" ","")
    con = con.strip()
    con = con.split(":")
   
    user = columna.find({con[0]:con[1]})

    return list(user)

def Bdato( Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]

    user = columna.find({})
    print(user[""])
    return user

#Conexion con MongoDB       
#client = MongoClient('localhost')
#ad = input("Ingrese: ")
#consultar('PALEONTOLOGÍA', "6157bb5d19fc18bae9f6eab7", "Documents")

Bdato("6157bb5d19fc18bae9f6eab7","Documents")

# #Base de datos
#db = client['Registro']

# #Coleccion de la base de datos
#columna = db['Usuario']

#Export("6147d8897e7f3556a6b4d11d")
#Import("jsontaller2.json", "6157bb5d19fc18bae9f6eab7", "Documents")

#Up(columna, "Ññ", "Jfdnsom", "wastv")
# Devolver $Oid
#x = columna.find_one({"name": "Xalo2312"},{})
#print(x["_id"])

#Creacion de Identificador 
#str(ObjectId())





