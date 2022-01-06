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
Luego, vamos a la carpeta contenedora de nuestro proyecto y ejecutamos el archivo **servidor.py**

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
## Autores ✒️
* **Daniel Fernando Araya Carmona**
* **Luis Felipe José Ortega Curillán**
* **Ignacio Alejandro Jesús Ortiz Ortiz**
* **Francisco Javier Fuentealba Peña**
### Supervisado por: 
* **Maximiliano Nicolás Cartes Neira**

