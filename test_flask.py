from flask import Flask
from flask import render_template

#variables

usuario = ""

#fin variables

#enlaces

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/singup")
def signup():
    return render_template("signup.html")
    
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

#ejecucion 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
#fin ejecucion 