from flask import Flask, render_template, request, redirect, jsonify
import apPymongo as xd

Usuario = ""
Colection = "Documents"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

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
    valid = xd.Acceso(user, password)

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
        xd.Registro(user, password)
        return "<h1> Usuario agregado <h1>"
    else:
        return "<h1> La Contraseña no es igual <h1>"

# Botones Muestra de Datos  
@app.route('/titulo')
def titulo():
    global Usuario
    global Colection

    zi = xd.Titulo(Usuario, Colection)
    a = ""
    for x in zi:
        a = a + x + '<br>'
    return a

@app.route('/categoria')
def categoria():
    global Usuario
    global Colection

    zi = xd.Categoria(Usuario, Colection)
    a = ""
    for x in zi:
        a = a + x + '<br>'
    return a

@app.route('/parrafos')
def parrafos():
    global Usuario
    global Colection

    zi = xd.Parrafo(Usuario, Colection)
    a = ""
    for x in zi:
        a = a + x + '<br>'
    return a

@app.route('/DocJson', methods=['POST'])
def DocJson():
    return

#Consultas 
@app.route('/sii', methods=['POST'])
def usuario():
    global Usuario
    global Colection

    con = request.form['consulta']
    zi = xd.consultar(con, Usuario, Colection)

    return jsonify(zi)
 
'''
@app.route("/edit")
def edicion():
    return render_template("manipulacion_archivo.html")

@app.route("/export")
def exportaciones(): #opcional
    return render_template("exportacion.html")
'''
if __name__ == '__main__':
    app.run(debug=True, port=5000)
