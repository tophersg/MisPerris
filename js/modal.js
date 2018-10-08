$('.galeria__img').click(function(e){
    var img = e.target.src;
    var historia = $("#historia").text();
    var modal= '<div class=""><div class="modal" id="modal"><img src="'+ img +'" class="modal__img"> '+historia+'<div class="modal__boton" id="modal_salir">X</div></div></div>';
    $('#fotografias').append(modal)
    $('#modal_salir').click(function(){
    $('#modal').remove();
    })
    })
    
    
    $(document).keyup(function(e) {
        if(e.which==27){
            $('#modal').remove();
        }
    
    
    })