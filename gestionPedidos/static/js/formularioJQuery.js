$(document).ready(function () {
    $("#formulario").validate({
        rules:{
            nombre:{
                required: true,
                minlength: 3
            },

            apellido:{
                required: true,
                minlength: 3
            },

            correo:{
                required: true,
                email: true
            },

            telefono:{
                required: true,
                digits: true,
                maxlength: 9
            },

            mensaje:{
                required: true,
                minlength: 1,
                maxlength: 100
            }
        },

        messages:{
            nombre:{
                required: "Debe ingresar al menos un nombre.",
                minlength: "Debe ingresar al menos 3 carácteres."
            },

            apellido:{
                required: "Debe ingresar su apellido.",
                minlength: "Debe ingresar al menos 3 carácteres."
            },

            correo:{
                required: "Debe ingresar un correo electrónico.",
                email: "Debe ingresar un correo válido."
            },

            telefono:{
                required: "Debe ingresar un número telefónico.",
                digits: "Debe ingresar solo números.",
                maxlength: "Excede el límite de números permitidos."
            },

            mensaje:{
                required: "Debe ingresar un comentario.",
                maxlength: "Excede el límite de carácteres permitidos."
            }
        }

    
    })
})

function contadorChar(){
    let max = 100;
    let char = mensaje.value.length;
    let contador = (max - char);

    if(contador < 1){
        document.getElementById("numChar").innerHTML = "<span style='color : red';><i>Máximo permitido de carácteres.</i>"
    }else{
        document.getElementById("numChar").innerHTML = "Quedan " + contador + " carácteres restantes.";
    }
}


