$(document).ready(function(){
   alert("Esto funciona!");
   $('#agregar_user').click(function(){


   var nombre = $('#nombre').val();
   var departamento = $('#departamento').val();
   var email = $('#email').val();
   var fuera_convenio = $('#fuera_convenio').val();
   


   $.ajax({
   	type: 'POST',
    url: '/personas/nuevo',
    dataType: 'json',
    data: { 'nombre': nombre, 'departamento': departamento, 'email': email, 'fuera_convenio': fuera_convenio},
   });
   //success: function(data){
   // 	alert(data.mensaje);
   // 	},
   }
});
//   $.post("/personas/nuevo", { nombre: nombre, departamento: departamento, email: email, fuera_convenio: fuera_convenio})
//   		.done(function(data){
//   			alert(data.mensaje);
//   		});


//function comprobar()
//{
//   var nombre = document.add_persona.nombre_apellido.value;
//   var departamento = document.add_persona.departamento.value;
//
//   if (nombre_apellido.length > 30)
//   {
//      alert("Tu nombre es demasiado grande. Redúcelo.");
//      return false;
//   }
//   
//   if (departamento.lenght > 40)
//   {
//      alert("El nombre de Dpto. es demasiado grande. Redúcelo");
//      return false;
//   }
//   
//   return true;
//}
