from pymongo import MongoClient
import json
from bson.objectid import ObjectId

def cat(Base):
    client = MongoClient('localhost')
    db = client[Base]
    contenido = {'cat': [],
                 'desc':[],
                 'Ndocu':[],
                 'Total':[],
                 'docu': []}
    
    for x in db.list_collection_names():
        if(db[x].count_documents({}) == 0):
            if(x != 'Documents'):db[x].drop()
   
    for x in db.list_collection_names():
        contenido['cat'].append(x)
        contenido['Ndocu'].append(db[x].count_documents({}))
        xd = db[x].find_one()
        if(xd != None):
            contenido['desc'].append(xd['desc_categoria'])
            for y in db[x].find(): 
                contenido['docu'].append(y) 
        else:
            contenido['desc'].append('Sin archivos...')
            
    contenido['Total'].append(sum(contenido['Ndocu']))
    return contenido

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
    Archivo = './Save/' + Archivo
    db = client[Base]

    with open(Archivo, encoding = 'utf8') as file:
        file_data = json.load(file)
    
    file_data['_id'] = str(ObjectId())
    columna = db[file_data['categoria']]

    if isinstance(file_data, list):
        columna.insert_many(file_data) 

    else:
        columna.insert_one(file_data)
    
    return file_data['_id']

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
        columna.insert_one({"_id":1, "Bienvenida": "Un gusto recibirte"})
        columna.delete_one({"_id":1})


def consultar(con, Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]

    # con = con.replace("'","")
    # con = con.replace('"',"")
    # con = con.replace("","")
    # con = con.replace("{","")
    # con = con.replace("}","")
    # con = con.replace(" ","")
    # con = con.strip()
    # con = con.split(":")
   
    #user = columna.find({con[0]:con[1]})
    user = columna.find(con)

    return list(user)

def Titulo(Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]
    Array = []

    for x in columna.find({}):
        for y in x['documentos']:
            Array.append("TITULO: " + (y['titulo']))
            Array.append("SUBTITULO: " + (y['subtitulo']))
            Array.append("FECHA: " + (y['fecha']) + "<br>")
            
    return list(Array)

def Categoria(Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]
    Array = []

    for x in columna.find({}):
        Array.append("CATEGORIA: " + (x['categoria']))
        Array.append("DESC_CATEGORIA: " + (x['desc_categoria']) + "<br>")
            
    return list(Array)

def Parrafo(Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]
    Array = []

    for x in columna.find({}):
        for y in x['documentos']:
            for a in y["desarrollo"]:
                Array.append("TITULO: " + (a['titulo_parrafo']))
                Array.append("PARRAFO: " + (a['parrafo']) + "<br>")
            
    return list(Array)

def editar(Base, Colec, doc):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]
    
    x = columna.find_one({'_id': doc})
    
    return x

def guardar(Base, Colec, doc, contenido):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]
    
    columna.update_one({'_id': doc}, {"$set": {'desarrollo': contenido}})
    
    return 'Se ha guardado correctamente'
#Conexion con MongoDB       
#client = MongoClient('localhost')
#ad = input("Ingrese: ")
#consultar('PALEONTOLOGÍA', "6157bb5d19fc18bae9f6eab7", "Documents")

#Bdato("6157bb5d19fc18bae9f6eab7","Documents")

# #Base de datos
#db = client['61a6a47f3a7f11d36393d548']



# #Coleccion de la base de datos
#columna = db['astronomía']

# Contador de documentos 
#rint(columna.count_documents({}))

#Export("6147d8897e7f3556a6b4d11d")
#Import("JsonSimple2.json", "617892c28f62b61c3236cd6b", "Documents")

#Up(columna, "Ññ", "Jfdnsom", "wastv")
# Devolver $Oid
#x = columna.find_one({"name": "Xalo2312"},{})
#print(x["_id"])

#Creacion de Identificador 
#str(ObjectId())

#cat('61a6a47f3a7f11d36393d548')





