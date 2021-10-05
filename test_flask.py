<<<<<<< Updated upstream
from flask import Flask, render_template, request
import apPymongo as xd
#variables
=======
from flask import Flask
from flask import render_template

>>>>>>> Stashed changes








from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import apPymongo as xd

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Registro"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/login')
def template():
    return render_template("index.html")

@app.route('/sii', methods=['POST'])
def usuario():

    con = request.form['consulta']
    
    carac = " '{}"
    
    for i in range(len(carac)):
        con = con.replace(carac[i],"")
  
    
    con = con.strip()
    con = con.split(":")
    user = db.Usuario.find({con[0]:con[1]})

  
    
    return str(list(user))
    

if __name__ == '__main__':
    app.run(debug=True)
#variables

#usuario = ""

#fin variables

#enlaces


'''
@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route('/authenticate', methods=['POST'])
def Inicio():
    user = request.form['username']
    password = request.form['password']

    return xd.Acceso(user, password)

@app.route("/singup")
def signup():
    return render_template("signup.html")
<<<<<<< Updated upstream

@app.route('/register', methods=['POST'])
def Registro():
    user = request.form['username']
    password = request.form['password']
    xd.Registro(user, password)
    return "<h1> Usuario agregado <h1>"

@app.route('/sii', methods=['POST'])
def usuario():
    con = request.form['consulta']
    con = con.replace("'","")
    con = con.replace('"',"")
    con = con.replace("","")
    con = con.replace("{","")
    con = con.replace("}","")
    con = con.replace(" ","")
    con = con.strip()
    con = con.split(":")

    #REQUIERE MODIFICACIÓN 
    # user = db.Usuario.find({con[0]:con[1]})
    # return str(list(user))
=======
  '''  
>>>>>>> Stashed changes
'''
@app.route("/edit")
def edicion():
    return render_template("manipulacion_archivo.html")

@app.route("/export")
def exportaciones(): #opcional
    return render_template("exportacion.html")

@app.route("/")
def  
'''

#fin enlaces
'''
#ejecucion 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
#fin ejecucion '''