function validar(){
var fecha,expresion;
fecha = document.getElementById("#fecha").value;
var fechaMenor = '2001/01/01';

if(fecha > fechaMenor){
alert('correcto');

return true;
}else{
    alert('error');
    return false;
}

}