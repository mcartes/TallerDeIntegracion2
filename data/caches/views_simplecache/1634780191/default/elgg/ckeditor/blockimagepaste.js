CKEDITOR.plugins.add('blockimagepaste',{init:function(editor){function replaceImgText(html){var ret=html.replace(/<img[^>]*src="data:image\/(bmp|dds|gif|jpg|jpeg|png|psd|pspimage|tga|thm|tif|tiff|yuv|ai|eps|ps|svg);base64,.*?"[^>]*>/gi,function(img){alert(elgg.echo('ckeditor:blockimagepaste'));return'';});return ret;}
function chkImg(){if(editor.readOnly){return;}
setTimeout(function(){editor.document.$.body.innerHTML=replaceImgText(editor.document.$.body.innerHTML);},100);}
editor.on('contentDom',function(){editor.document.on('drop',chkImg);editor.document.getBody().on('drop',chkImg);});editor.on('paste',function(e){var html=e.data.dataValue;if(!html){return;}
e.data.dataValue=replaceImgText(html);});}});