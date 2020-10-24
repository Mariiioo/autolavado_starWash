function validarNombre() {
    var nombre = document.getElementById("txtNombreInsumo").value;
    if (nombre.trim().length >= 3 && nombre.trim().length <= 200) {
        // alert("Nombre valido " + nombre); 
        return true;
    } else {
        //alert("Nombre invalido");
        return false;
    }
}

function validarPrecio() {
    var precio = document.getElementById("txtPrecio").value;
    if (precio >= 1) {
        //alert("Precio Bueno")
        return true;
    } else {
        //alert("Precio Malo")
        return false;
    }
}

function validarDescripcion() {
    var descripcion = document.getElementById("txtDescripcion").value;
    if (descripcion.length == 0) {
        return true
    } else {
        if (descripcion.trim().length >= 3 && descripcion.trim().length <= 200) {
            // alert("Descripcion valida" + descripcion); 
            return true;
        } else {
            //alert("descripcion invalida");
            return false;
        }
    }
}



function validarStock() {
    var stock = document.getElementById("txtStock").value;
    if (stock > 0) {
        return true;
    } else {
        return false;
    }
}

function validarFormularioProductos() {
    var resp;
    //Validar Nombre
    resp = validarNombre();
    if (resp == false) {
        alert("El nombre del insumo debe poseer más de 3 carácteres.");
        return false;
    }
    //Validar Nombre
    resp = validarDescripcion();
    if (resp == false) {
        alert("La descripcion del insumo debe poseer más de 3 carácteres.");
        return false;
    }
    //Validar Precio
    resp = validarPrecio();
    if (resp == false) {
        alert("El precio debe ser mayor o igual a $1");
        return false;
    }

    //Validar Stock
    resp = validarStock();
    if (resp == false) {
        alert("Si tiene stock debe ser mayor o igual a 0");
        return false;
    }

    if (resp == true) {
        alert("Todos los datos del insumo son correctos :D");
    }
}