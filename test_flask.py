from flask import Flask, render_template, request, redirect, jsonify
import apPymongo as PyM
from werkzeug.utils import secure_filename
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField

Usuario = ""
Colection = "Documents"

app = Flask(__name__)

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

#Prueba CKEditor
@app.route("/testck")
def testck():
    global Usuario, Colection
    si = {}
    form = PostForm()
    xd = PyM.consultar(si, Usuario, Colection)
    return render_template("doc.html", form = form, xd=xd)

#Pagina Principal
@app.route("/Inicio")
def index():
    return render_template("index.html")

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
        return redirect("/Inicio")

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
    PyM.Import(filename, Usuario, Colection)

    return redirect("/Inicio")

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
    return

if __name__ == '__main__':
    app.run(debug=True, port=5000)
