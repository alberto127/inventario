$(document).ready(function(){
    $('#nombre').val("Almacen");
    $('#departamento').val("Informatica");
    $('#email').val("informatica@apvigo.es");
    
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

    $('#btn_add_dispo').click(function(){


        var tipo_dispositivo = $('#tipo_dispositivo').val();
        var marca = $('#marca').val();
        var modelo = $('#modelo').val();
        var num_serie = $('#num_serie').val();
        var fecha_instalacion = $('#fecha_instalacion').val();
        var asignar_usuario = $('#asignar_usuario').val();


   $.ajax({
    type: 'POST',
    url: '/dispositivos/nuevo',
    dataType: 'json',
    data: { 'tipo_dispositivo': tipo_dispositivo, 'marca': marca, 'modelo': modelo, 'num_serie': num_serie, 'fecha_instalacion': fecha_instalacion, 'asignar_usuario': asignar_usuario},
   });
   //success: function(data){
   //   alert(data.mensaje);
   //   },
   }
});