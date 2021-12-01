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

new FroalaEditor('div#froala-editor', {
toolbarInline: false,
charCounterCount: true,
heightMax: 500,
heightMin: 499,
    events: {
        initialized: function () {
            var editor = this;

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
                    editor.html.insert('<pre>Código</pre>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-block-2'){
                    editor.html.insert('<h3>Estructura de arquetipo con h3</h3>');
                }

                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-block-3'){
                    editor.html.insert('<p>Párrafo a editar</p>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-1') {
                    editor.html.insert('<h1>T&iacute;tulo</h1><hr><h2>Subt&iacute;tulo</h2><p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi debitis saepe quo, error ratione optio ullam asperiores, quaerat ipsa sint ut voluptatem, exercitationem ea! Quam soluta consequuntur voluptas totam eius!</p><p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi debitis saepe quo, error ratione optio ullam asperiores, quaerat ipsa sint ut voluptatem, exercitationem ea! Quam soluta consequuntur voluptas totam eius!</p>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-2') {
                    editor.html.insert('<h1>T&iacute;tulo sensual</h1><hr><h2>Subt&iacute;tulo</h2><p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi debitis saepe quo, error ratione optio ullam asperiores, quaerat ipsa sint ut voluptatem, exercitationem ea! Quam soluta consequuntur voluptas totam eius!</p><p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi debitis saepe quo, error ratione optio ullam asperiores, quaerat ipsa sint ut voluptatem, exercitationem ea! Quam soluta consequuntur voluptas totam eius!</p>');
                }
                if (dropEvent.originalEvent.dataTransfer.getData('Text') == 'drag-arquetipo-3') {
                    editor.html.insert('<h1>T&iacute;tulo</h1><hr><h2>Subt&iacute;tulo</h2><p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi debitis saepe quo, error ratione optio ullam asperiores, quaerat ipsa sint ut voluptatem, exercitationem ea! Quam soluta consequuntur voluptas totam eius!</p><p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi debitis saepe quo, error ratione optio ullam asperiores, quaerat ipsa sint ut voluptatem, exercitationem ea! Quam soluta consequuntur voluptas totam eius!</p>');
                }
                //Insertar arquetipos

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