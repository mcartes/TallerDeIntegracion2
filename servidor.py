from flask import Flask, render_template, request, redirect, jsonify, flash, url_for
import apPymongo as PyM
from werkzeug.utils import secure_filename
import json
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

Usuario = ""
Colection = "Documents"
colections = ""

os.makedirs('Save', exist_ok=True)

app = Flask(__name__)

#Guardar Archivos
app.config['UPLOAD_FOLDER'] = './Save'


#CKEditor
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.secret_key = 'secret string'
ckeditor = CKEditor(app)
app.config['CKEDITOR_PKG_TYPE'] = 'custom'
#app.config['CKEDITOR_EXTRA_PLUGINS'] = ['exportpdf', 'format']

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')


#inicio
@app.route("/")
def start(): 
    
    return render_template("index.html")


#Editor
@app.route("/editor")
def editor():
    global Usuario, Colection
    si = {}
    form = PostForm()
    xd = PyM.consultar(si, Usuario, Colection)
    return render_template("editor.html", form = form, xd=xd)

#Pagina Principal
@app.route("/proyecto")
def index():
    global colections, Usuario
    colections = PyM.cat(Usuario)
    return render_template("proyecto.html", colections = colections)

# Inicio de Sesion
@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route('/authenticate', methods=['POST'])
def Acceso():
    global Usuario
    user = request.form['username']
    password = request.form['password']
    valid = PyM.Acceso(user, password)

    if(valid[0] == 'success'):
        Usuario = valid[1]
        return redirect("/proyecto")

    elif(valid == 'BadUser' ):
        return("Usuario No Existe")
    
    elif(valid == 'BadPass'):
        return("Contraseña Incorrecta")

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
        PyM.Registro(user, password)
        return "<h1> Usuario agregado <h1>"
    else:
        return "<h1> La Contraseña no es igual <h1>"

# Botones Muestra de Datos  
@app.route('/titulo')
def titulo():
    global Usuario
    global Colection

    GetTitulo = PyM.Titulo(Usuario, Colection)
    a = ""
    for x in GetTitulo:
        a = a + x + '<br>'
    return a

@app.route('/categoria')
def categoria():
    global Usuario
    global Colection

    GetCategoria = PyM.Categoria(Usuario, Colection)
    a = ""
    for x in GetCategoria:
        a = a + x + '<br>'
    return a

@app.route('/parrafos')
def parrafos():
    global Usuario
    global Colection

    GetParrafo = PyM.Parrafo(Usuario, Colection)
    a = ""
    for x in GetParrafo:
        a = a + x + '<br>'
    return a

@app.route('/subir', methods=['POST'])
def ImportJson():
    global Usuario
    global Colection

    GetFile = request.files["archivosubido"]
    filename = secure_filename(GetFile.filename)
    # filename = 'sd.json'
    GetFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    PyM.Import(filename, Usuario, Colection)
    flash('Contact Updated Successfully')
    return redirect("/proyecto")

#Consultas 
@app.route('/sii', methods=['POST'])
def usuario():
    global Usuario
    global Colection

    con = request.form['consulta']
    try: 
        con = json.loads(con)
        GetConsulta = PyM.consultar(con, Usuario, Colection)
        return jsonify(GetConsulta)

    except:
        return "Consulta erronea. EJEMPLO: {'data': 'Value'}"
    
@app.route('/CrearA', methods=['POST'])
def CrearA():
    Cname = request.form['Cname'] 
    Ccategoria = request.form['Ccategoria']
    return redirect('/editor')

@app.route('/coso', methods=['POST'])
def coso():
    global Usuario
    catselect = request.form['listGroupRadios'].split(',')
    print(catselect[0])
    print(catselect[1])
    catselect = PyM.editar(Usuario, catselect[1], catselect[0])
    
    return jsonify(catselect)

@app.route('/newdoc', methods=['POST'])
def newdoc():
    global Usuario
    doc = {
    "_id": "1314",
    "categoria": "",
	"fecha": date.today().isoformat(),
    "desc_categoria": "",
	"nombredoc": "",
    "desarrollo": {}
	}
    doc['nombredoc'] = request.form['nombredoc']
    Ncate = request.form['Ncate'].split('|')

    if(Ncate[0] == 'Nuevo'):
        newcat = request.form['newcat']
        desc_newcat = request.form['desc_newcat']
        doc['categoria'] = newcat
        doc['desc_categoria'] = desc_newcat
    else:
        doc['categoria'] = Ncate[0]
        doc['desc_categoria'] = Ncate[1]
        if(Ncate[0] == "Documents"):
            doc['desc_categoria'] = "Archivos sin categoria"
            
    with open('./Save/new.json', 'w') as f:
        json.dump(doc, f)
        
    PyM.Import('new.json', Usuario, Colection)
    
    return jsonify(doc)

#prueba de arquetipos
@app.route('/arq')
def arquetipos():

    return render_template("arquetipos.html")



if __name__ == '__main__':
    app.run(debug=True, port=5000)


