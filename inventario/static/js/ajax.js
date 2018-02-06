$(document).ready(function(){
   $('#asignar_usuario').on('change', function(e){
        e.preventDefault();
        var user = $(this).val(); //obtiene el usuario seleccionado
          //petición ajax
       //console.log(user)
       console.log("cambio");
        $.ajax({
            type: 'GET',
            url: '/dispositivos/muestra_usuario',
            dataType: 'json',
            data: {'user': user},
            //async : false, //espera la respuesta antes de continuar
            success: function(data) {
            //userData=json.parse(data)
                console.log("ejecutó");
                console.log(data[0].fields.usuario);
                //console.log(data[0].fields.departamento);
            $('#nombre').val(data[0].pk);
            //console.log(json);
            //document.getElementById('usuario').value = data.usuario
            //document.getElementById('departamento').value = data.departamento
            //repuesta
            $('#departamento').val(data[0].fields.departamento);
            $('#email').val(data[0].fields.email);
            },
        });
  });

});