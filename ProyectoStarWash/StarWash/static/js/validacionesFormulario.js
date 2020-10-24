function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        return false;
    }
    var suma = 0;
    var num = 3;
    //Operatoria
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    //Remplazar los rut 10 y 11
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K'
        } else {
            dv = 0;
        }
    }
    //comparar los dv si es valido
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        //alert("Rut Incorrecto")
        return false;
    } else {
        //alert("Rut Valido");
        return true;
    }
}

function validarFecha() {
    //fecha la que ingresa el usuario
    var fechaUsuario = document.getElementById("dtpFecha").value;
    //fecha actual del sistema
    var fechaActual = new Date;
    /////////////SEPARAR EL DIA - MES - ANNO del USUARIO/////////////
    var dia = fechaUsuario.slice(8, 10);
    var mes = fechaUsuario.slice(5, 7);
    var anno = fechaUsuario.slice(0, 4);
    //JUNTAR LOS DATOS
    var fechaUsFinal = new Date(anno, (mes - 1), dia);
    //VALIDA QUE LA FECHA JUNTADA SEA CORRECTA
    if (fechaUsFinal < fechaActual) {
        //alert("Fecha incorrecta");
        return false;
    } else {
        //alert("Fecha correcta");
        return true;
    }
}

function validarNombre() {
    nombre = document.getElementById("txtNombre").value;
    if (nombre.trim().length >= 3 && nombre.trim().length <= 80) {
        return true;
    } else {
        return false;
    }
}

function validarApellido() {
    apellido = document.getElementById("txtApellido").value;
    if (apellido.trim().length >= 3 && apellido.trim().length <= 80) {
        return true;
    } else {
        return false;
    }
}

function validarEmail() {
    email = document.getElementById("txtEmail").value;
    if (email.trim().length >= 3 && email.trim().length <= 200) {
        return true;
    } else {
        return false;
    }
}

function validarUsuario() {
    user = document.getElementById("txtNombreUsuario").value;
    if (user.trim().length >= 3 && user.trim().length <= 200) {
        return true;
    } else {
        return false;
    }
}

function valFormulatioUsuario() {
    var resp;
    resp = validarNombre();
    if (resp == false) {
        alert("El Nombre es incorrecto");
        return false;
    }
    resp = validarApellido();
    if (resp == false) {
        alert("El Apellido es incorrecto");
        return false;
    }
    resp = validarEmail();
    if (resp == false) {
        alert("El Email es incorrecto");
        return false;
    }
    resp = validarUsuario();
    if (resp == false) {
        alert("El Email es incorrecto");
        return false;
    }
    if (resp == true) {
        //alert("Todos los datos son correctos :D")
    }
}