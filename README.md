# LeFrogé
Es un proyecto web donde se crea un entorno digital estructurado en base al proceso científico para crear, escribir, editar, guardar y exportar artículos científicos. 
## Pre-requisitos 🔧
Antes de iniciar, Es necesario tener instalado
- Python versión 3.x (Para el desarrollo se utilizó la versión 3.9) https://www.python.org/downloads/
- MongoDB localmente (https://www.mongodb.com/try/download/community)
- Editor de texto de preferencia. Para el proyecto se utilizó "Visual studio code" (https://code.visualstudio.com/download)
## Pasos Para instalar el programa 🛠

Ya instalados los Pre-requisitos, mediante el sistema de gestión de paquetes "pip", que generalmente viene por defecto en la instalación de Python instalaremos las librerías de python necesarias para ejecutar el proyecto, por lo que es necesario abrir la terminal, (Símbolo del sistema en windows) y ejecutaremos el siguiente comando:
```
pip install pymongo flask werkzeug bson
```
## Iniciando el Programa📖
Lo primero que se necesita es dirigirse a la carpeta donde instalamos el MongoDB y ejecutamos el archivo llamado "mongod.exe" (generalmente se encuentra en el directorio C:\Program Files\MongoDB\Server\5.0\bin), el cual abrirá una terminal iniciando el proceso de mongodb.

![imagen](https://user-images.githubusercontent.com/44407924/148454442-2112420d-cb21-4149-ab0a-1fc77019b86b.png)

o también en la consola de comandos copiamos las 2 lineas de código (reemplazando por la versión que tenga instalada)
```
cd C:\Program Files\MongoDB\Server\5.0\bin
mongod
```
Finalmente, vamos a la carpeta contenedora de nuestro proyecto y ejecutamos el archivo **servidor.py**

![imagen](https://user-images.githubusercontent.com/44407924/148455176-3c617101-0287-4874-8df8-1d6de5d59bb8.png)

Que abrirá una terminal, iniciando el servidor local.
![imagen](https://user-images.githubusercontent.com/44407924/148455268-9a3cacfb-c73c-4820-b009-ee7b3aafccd7.png)


## Una vez completado todo ✅
Se podrá ver el inicio correctamente en el servidor local http://127.0.0.1:5000/
![imagen](https://user-images.githubusercontent.com/44407924/147611389-9f0958a2-7a2d-45b2-a737-546adec27694.png)
### Donde:
El usuario podrá iniciar sesión o crearse una cuenta nueva.
![imagen](https://user-images.githubusercontent.com/44407924/147611531-f5413169-1d43-4277-8874-ff082e61246b.png)
Una vez iniciado podrá ver sus proyectos.
![imagen](https://user-images.githubusercontent.com/44407924/147611807-7b6c147a-7b94-4fa2-b009-c3e1e606efbe.png)
Así mismo como editarlos de una manera cómoda y amigable para el usuario y guardarlos en diversos formatos!.
![imagen](https://user-images.githubusercontent.com/44407924/147611894-89037b08-a88d-4394-a855-1067cdf0f626.png)
## Para editar ✍🏻
Una vez ya descargado y completado los pasos para instalar, se podrá entrar en el ambiente de programación, por lo que le daremos clic derecho a la carpeta contenedora del proyecto y seleccionamos "Abrir con Code"

![imagen](https://user-images.githubusercontent.com/44407924/148456488-94ef57f0-574f-4d19-8581-477b88a3bf96.png)

Una vez abierto se podrá instalar la extensión de python para Visual studio code (opcional)
![imagen](https://user-images.githubusercontent.com/44407924/148456786-27c75e59-9cfe-4425-b99f-2270553566cf.png)

Ya en la vista de las carpetas con los archivos, podremos elegir si queremos personalizar el frontend o el backend.
### Para el Frontend
- Se encontrará la carpeta "static" que es la contendrá los archivos css, Javascript y las imágenes.

![imagen](https://user-images.githubusercontent.com/44407924/148457175-25642b3d-d223-4e1b-83c6-ca0a172e0e81.png)
- Se encontrará la carpeta "templates", en la cual se encontrarán todos los archivos html. Es probable que en algunas carpetas aparezcan errores, como los que se ven en la imagen de abajo, pero esto se debe a que Visual studio code al no reconocer algunas funcionalidades de Flask las marca como errores, sin embargo no afecta nada a su funcionalidad correcta.

![imagen](https://user-images.githubusercontent.com/44407924/148457583-ee7eb192-fcbe-4f69-91cd-64f8f161a08b.png)

### Para el Backend
- Se encontrará "Servidor.py" el cual contendrá las rutas y será el que mantenga funcionando el servidor
 ![imagen](https://user-images.githubusercontent.com/44407924/148458067-0220d01c-2d11-4d96-ab1f-ab7da4c87002.png)
- apPymongo.py el cual será el encargado de comunicar mongodb con python.
 ![imagen](https://user-images.githubusercontent.com/44407924/148458259-0ff0fe91-68b1-4ddc-9922-bcc404dd2f66.png)



## Autores ✒️
* **Daniel Fernando Araya Carmona**
* **Luis Felipe José Ortega Curillán**
* **Ignacio Alejandro Jesús Ortiz Ortiz**
* **Francisco Javier Fuentealba Peña**
### Supervisado por: 
* **Maximiliano Nicolás Cartes Neira**

