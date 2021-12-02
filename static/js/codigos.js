function exportaJSON(){
    var fecha = new Date();              //Variable para crear un objsoneto fecha
    var objson = new objsonect();            //Variable para crear un objsoneto con los atributos del JSON

    sContent = editor.getPlainText(); //Extrae el contenido del cuadro de texto en formato de texto plano

    objson.nombre_creador    = "Francisco Giacomozzi";
    objson.fecha_exportacion = fecha.getFullYear()+'-'+ (fecha.getMonth()+1)+'-'  + fecha.getDate();
    objson.hora_exportacion  = fecha.getHours() + ":" +  fecha.getMinutes() + ":" + fecha.getSeconds();
    objson.contenido         = sContent;

    var jsonString= JSON.stringify(objson); //Convierte el objeto a un string de json

    //Configuracion de encoding para la exportacion
    dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(jsonString);
    exportFileDefaultName = 'exportacion_data.json';

    //Crea un elemento de tipo a, para exportar el archivo
    linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();

    editor.insertHTML('<b>Que pasa chavales todo bien todo correcto</b>')
  }