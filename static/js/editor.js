//################################
// Editor de texto
//################################
var dragCallback = function (e) {
    e.dataTransfer.setData('Text', this.id);
    };
//Bloques de edición
document.querySelector('#drag-block-1').addEventListener('dragstart', dragCallback);
document.querySelector('#drag-block-2').addEventListener('dragstart', dragCallback);
document.querySelector('#drag-block-3').addEventListener('dragstart', dragCallback);

//Arquetipos
document.querySelector('#drag-arquetipo-1').addEventListener('dragstart', dragCallback);
document.querySelector('#drag-arquetipo-2').addEventListener('dragstart', dragCallback);
document.querySelector('#drag-arquetipo-3').addEventListener('dragstart', dragCallback);
document.querySelector('#drag-arquetipo-4').addEventListener('dragstart', dragCallback);
document.querySelector('#drag-arquetipo-5').addEventListener('dragstart', dragCallback);

var editor = new FroalaEditor('div#froala-editor', {
toolbarInline: false,
charCounterCount: true,
heightMax: 500,
heightMin: 499,
    events: {
        initialized: function () {
            var editor = this;

			editor.html.insert(docu['desarrollo']);

            editor.events.on('drop', function (dropEvent) {
                // Focus at the current posisiton.
                editor.markers.insertAtPoint(dropEvent.originalEvent);
                var $marker = editor.$el.find('.fr-marker');
                $marker.replaceWith(FroalaEditor.MARKERS);
                editor.selection.restore();

                // Save into undo stack the current position.
                if (!editor.undo.canDo()) editor.undo.saveStep();

                // Insertar bloques de código
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-block-1') {
                    editor.html.insert('<pre class="preBorder">Código</pre>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-block-2'){
                    editor.html.insert('<h3>Estructura de arquetipo con h3</h3>');
                }

                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-block-3'){
                    editor.html.insert('<p>Párrafo a editar</p>');
                }
                
                //Insertar arquetipos
                
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-1') {
                    editor.html.insert('<h1>Título</h1><h2>Subtitulo</h2><i>Autor</i><br><i>Fecha</i><hr><p>Párrafo</p><hr>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-2') {
                    editor.html.insert('<h1>Título</h1><h2>Subtitulo</h2><i>Autor</i><br><i>fecha</i><hr><h2>introducción</h2><p>párrafo</p><hr><h2>métodos</h2><p>párrafo</p><hr><h2>resultados</h2><p>párrafo</p><hr><h2>discusión</h2><p>párrafo</p>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-3') {
                    editor.html.insert('<h1>Título</h1><h2>Subtitulo</h2><i>Autor</i><br><i>Fecha</i><hr><p>Introducción Párrafo</p><hr><p>Desarrollo Párrafo</p><hr><p>Conclusión Párrafo</p><hr>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-4') {
                    editor.html.insert('<h1>Título</h1><i>Autor</i><hr><h3>Índice</h3><P>Párrafo</P><hr><h3>Requerimientos</h3><p>Párrafo</p><hr><h3>Instrucciones</h3><p>Párrafo</p><hr><h3>Normas de uso</h3><p>Párrafo</p><hr>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-5') {
                    editor.html.insert('<H1>Título</H1><i>Autor</i><hr><p>Introducción Párrafo</p><br><p>Desarrollo Párrafo</p><br><p>Desenlace Párrafo</p>');
                }

                // Save into undo stack the changes.
                editor.undo.saveStep();
                // Stop event propagation.
                dropEvent.preventDefault();
                dropEvent.stopPropagation();
                // Firefox show cursor.
                if (editor.core.hasFocus() && editor.browser.mozilla) {
                    editor.events.disableBlur();
                    setTimeout(function () {
                        editor.$el.blur().focus();
                        editor.events.enableBlur();
                    }, 0);
                }
            
                return false;
            }, true);
        }    
    }
});

function guardar(){
    var contenido = editor.html.get();
    var cat = docu['categoria']
    var doc = docu['_id']
    console.log(cat, doc)
    $.ajax({
        url:"/save",
        type:"POST",
        data: {"value": contenido, 
                "cat": cat, 
                "doc": doc},
        success: function(response){
            console.log(response);
        },
        error: function(error){
        //console.log(error);
        },
    });
}
function exportarJSON(){

    var fecha = new Date();              //Variable para crear un objsoneto fecha
    var objson = new Object();            //Variable para crear un objsoneto con los atributos del JSON

    sContent = editor.html.get(); //Extrae el contenido del cuadro de texto en formato de texto plano

    objson._id = docu["_id"];
    objson.categoria = docu['categoria'];
    objson.fecha = fecha.getFullYear()+'-'+ (fecha.getMonth()+1)+'-'  + fecha.getDate();
    objson.desc_categoria = docu['desc_categoria'];
    objson.desarrollo = sContent;

    var jsonString= JSON.stringify(objson); //Convierte el objeto a un string de json

    //Configuracion de encoding para la exportacion
    dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(jsonString);
    exportFileDefaultName = docu['nombredoc']+'.json';

    //Crea un elemento de tipo a, para exportar el archivo
    linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();

}
