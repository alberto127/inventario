$(document).ready(function(){
   $('#asignar_usuario').on('click', function(){

        var user = $(this).val(); //obtiene el usuario seleccionado
          //petición ajax
       //console.log(user)
        $.ajax({
            type: 'POST',
            url: 'dispositivos/muestra_usuario',
            //dataType: 'json',
            data: user,
            //async : false, //espera la respuesta antes de continuar
            success: function(result) {
            //userData=json.parse(data)
            alert('ok');
            //console.log(json);
            //document.getElementById('usuario').value = data.usuario
            //document.getElementById('departamento').value = data.departamento
            $('#usuario').val(userData.usuario);//repuesta
            $('#departamento').val(userData.departamento);
            },
        });
  });

});