function validarNombre() {
    nombre = document.getElementById("txtNombre").value;
    if (nombre.trim().length >= 3 && nombre.trim().length <= 50) {
        return true;
    } else {
        return false;
    }
}

function validarApellido() {
    apellido = document.getElementById("txtApellido").value;
    if (apellido.trim().length >= 3 && apellido.trim().length <= 50) {
        return true;
    } else {
        return false;
    }
}

function validarAsunto() {
    apellido = document.getElementById("txtAsunto").value;
    if (apellido.trim().length >= 8 && apellido.trim().length <= 50) {
        return true;
    } else {
        return false;
    }
}

function validarMensaje() {
    apellido = document.getElementById("txtMensaje").value;
    if (apellido.trim().length >= 10 && apellido.trim().length <= 200) {
        return true;
    } else {
        return false;
    }
}

function valFormulatioContacto() {
    var resp;
    resp = validarNombre();
    if (resp == false) {
        alert("El Nombre debe poseer mínimo 3 carácteres.");
        return false;
    }
    resp = validarApellido();
    if (resp == false) {
        alert("El Apellido debe poseer mínimo 3 carácteres.");
        return false;
    }
    resp = validarAsunto();
    if (resp == false) {
        alert("El Asunto debe poseer mínimo 8 carácteres.");
        return false;
    }
    resp = validarMensaje();
    if (resp == false) {
        alert("El Mensaje debe poseer mínimo 10 carácteres.");
        return false;
    }
    if (resp == true) {
        //alert("Todos los datos son correctos :D")
    }
}