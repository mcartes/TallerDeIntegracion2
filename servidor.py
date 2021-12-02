from flask import Flask, render_template, request, redirect, jsonify, url_for
import apPymongo as PyM
from werkzeug.utils import secure_filename
import json
import os
from datetime import date

Usuario = ""
Colection = "Documents"
colections = ""
act = False

os.makedirs('Save', exist_ok=True)

app = Flask(__name__)

#Guardar Archivos
app.config['UPLOAD_FOLDER'] = './Save'

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def start(): 
    global act
    return render_template("index.html", act = act)

#Editor
@app.route("/editor/<cat>/<doc>")
def editor(cat, doc):
    global Usuario, Colection, act
    documento = PyM.editar(Usuario, cat, doc)
    return render_template("editor.html", doc = documento, act = act)

#Pagina Principal
@app.route("/proyecto")
def index():
    global colections, Usuario, act
    if(Usuario != ""):
        colections = PyM.cat(Usuario)
        return render_template("proyecto.html", colections = colections, act = act)
    else:
        return redirect("/login")

# Inicio de Sesion
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/deslogin")
def deslogin():
    global Usuario, Colection, colections, act
    Usuario = ""
    Colection = "Documents"
    colections = ""
    act = False
    return redirect("/")
    
@app.route('/authenticate', methods=['POST'])
def Acceso():
    global Usuario, act
    user = request.form['username']
    password = request.form['password']
    valid = PyM.Acceso(user, password)

    if(valid[0] == 'success'):
        Usuario = valid[1]
        act = True
        return redirect("/proyecto")

    elif(valid == 'BadUser' ):
        return "<h1> El Usuario No Existe ,<a href=/login>intentelo de nuevo</a></h1>"

    elif(valid == 'BadPass'):
        return "<h1> La Contraseña esta Incorrecta,<a href=/login>intentelo de nuevo</a></h1>"

# Registro De Usuarios
@app.route("/singup")
def signup():
    return render_template("signup.html")

@app.route('/register', methods=['POST'])
def Registro():
    user = request.form['username']
    password = request.form['password']
    password_confirm =  request.form['password_confirm']
    if(password == password_confirm):
        return "<h1>"+PyM.Registro(user, password)+"</h1>"
    else:
        return "<h1> Las Contraseñas no son iguales, <a href=/singup>intentelo de nuevo</a></h1></h1>"

@app.route('/subir', methods=['POST'])
def ImportJson():
    global Usuario
    global Colection

    GetFile =  request.files.getlist("archivosubido")
    
    for file in GetFile:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        PyM.Import(filename, Usuario, Colection)
        
    return redirect("/proyecto")

#Consultas
@app.route('/sii', methods=['POST'])
def usuario():
    global Usuario, colections

    con = request.form['consulta']
    try:
        con = json.loads(con)
        GetConsulta = PyM.consultar(con, Usuario, colections['cat'])
        return jsonify(GetConsulta)

    except:
       return "Consulta erronea. EJEMPLO: {'data': 'Value'}"

@app.route('/coso', methods=['POST'])
def coso():
    global Usuario
    try:
        catselect = request.form['listGroupRadios'].split(',')
        #catselect = PyM.editar(Usuario, catselect[1], catselect[0])
        return redirect(url_for("editor", cat=catselect[1], doc=catselect[0] ))
    except:
        return redirect("/proyecto")

@app.route('/newdoc', methods=['POST'])
def newdoc():
    global Usuario
    doc = {
    "_id": "",
    "categoria": "",
	"fecha": date.today().isoformat(),
    "desc_categoria": "",
	"nombredoc": "",
    "desarrollo": ""
	}
    doc['nombredoc'] = request.form['nombredoc']
    Ncate = request.form['Ncate'].split('|')

    if(Ncate[0] == 'Nuevo'):
        newcat = request.form['newcat']
        desc_newcat = request.form['desc_newcat']
        doc['categoria'] = newcat
        Ncate[0] = newcat
        doc['desc_categoria'] = desc_newcat
    else:
        doc['categoria'] = Ncate[0]
        doc['desc_categoria'] = Ncate[1]
        if(Ncate[0] == "Documents"):
            doc['desc_categoria'] = "Archivos sin categoria"

    with open('./Save/new.json', 'w') as f:
        json.dump(doc, f)

    idd = PyM.Import('new.json', Usuario, Colection)

    return redirect(url_for("editor", cat=Ncate[0], doc=idd ))

@app.route('/save', methods=['POST'])
def save():
    global Usuario
    datos = request.form['value']
    cat = request.form['cat']
    doc = request.form['doc']

    return PyM.guardar(Usuario, cat, doc, datos)

@app.route('/delete/<doc>/<cat>')
def delete(doc, cat):
    global Usuario

    PyM.eliminar(Usuario, cat, doc)
    return redirect("/proyecto")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
