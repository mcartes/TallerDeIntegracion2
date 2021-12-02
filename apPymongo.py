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
        return("<h1>Usuario Existente,<a href=/singup>Vuelva a intentarlo Aqui</a></h1>")

    else:
        a = columna.insert_one({"_id":str(ObjectId()),"name": nombre, "contra": password})
        dou = columna.find_one({"name": nombre})
        db = client[dou["_id"]]
        columna = db["Documents"]
        columna.insert_one({"_id":1, "Bienvenida": "Un gusto recibirte"})
        columna.delete_one({"_id":1})
        return"<h1> Usuario agregado, <a href=/login>Presione aqui para iniciar seccion</a></h1></h1>"


def consultar(con, Base, Colec):
    client = MongoClient('localhost')
    db = client[Base]
    user = {"datos": []}
    for x in range(len(Colec)):
        for y in db[Colec[x]].find(con):
            user["datos"].append(y)
           
    return list(user["datos"])


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

def eliminar(Base, Colec, doc):
    client = MongoClient('localhost')
    db = client[Base]
    columna = db[Colec]

    columna.delete_one({'_id': doc})

    return 'Se ha eliminado correctamente'






