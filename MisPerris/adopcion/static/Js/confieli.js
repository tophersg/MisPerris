function alerta()
    {
    var mensaje;
    var opcion = confirm("¿Esta Sseguro que desea borrar?");
    if (opcion == true) {
        mensaje = "Confirmar";
	} else {
	    mensaje = "Cancelar";
	}
	document.getElementById("ejemplo").innerHTML = mensaje;
}