//################################
// Drag and Drop
//################################
function handleDrop(e) {
    e.stopPropagation();
    e.preventDefault();
    p.innerHTML = '<b>Files dropped:</b>';
    list.innerHTML = '';

    var files = e.dataTransfer.files,
        folder;

    for (var i = 0, f; f = files[i]; i++) { // iterate in the files dropped
        if (!f.type && f.size % 4096 == 0) {
            // The file is a folder
            folder = true;
        } else {
            // The file is not a folder
            folder = false;
        }

        var x = document.createElement('li');
        x.innerText = (folder ? 'Folder: ' : 'File: ') + f.name + (f.type ? ' (' + f.type + ')' : '') + ', ' + f.size + 'bytes';
        list.appendChild(x);
    }

}

function handleDragOver(e) {
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy'; // say that is a copy
}

function handleDragEnter(e) {
    e.stopPropagation();
    e.preventDefault();
    p.innerHTML = '<b>Dragging...</b>';
    list.innerHTML = '';
}

function handleDragLeave(e) {
    e.stopPropagation();
    e.preventDefault();
    p.innerHTML = '';
    list.innerHTML = '';
}

var dropZone = document.getElementById('drop_zone'),
    list = document.getElementById('list'),
    p = document.getElementById('info').children[0];

dropZone.addEventListener('dragenter', handleDragEnter, false);
dropZone.addEventListener('dragover', handleDragOver, false);
dropZone.addEventListener('dragleave', handleDragLeave, false);
dropZone.addEventListener('drop', handleDrop, false);

