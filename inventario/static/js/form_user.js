
(function(){
	'use strict';
	var usuario_nuevo=document.getElementById('usuario_nuevo');
		usuario_nuevo.addEventListener('click', function(){
			document.getElementById("add_persona").style.display = "";
		});
})();


(function(){
	var user=document.getElementById('asignar_usuario');
	user.addEventListener('click', function(){
		document.getElementById("usuario").value="asignar_usuario"
	})
})
