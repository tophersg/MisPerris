$('#oso').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Oso</h3></div><div class="parrafo1"><p>Tiene 2 años de edad y tamaño mediano, es cariñoso, super dócil y está siempre buscando cariño.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';


    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })

})

$('#maya').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Maya</h3></div><div class="parrafo1"><p>Es una perrita joven de 2 meses y tamaño mediano-grande. Es regalona, juguetona y puede vivir dentro o fuera de la casa.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';


    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })

})

$('#wifi').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Wifi</h3></div><div class="parrafo1"><p>Con 7 añitos, mantiene una personalidad alegre y juvenil, al mismo tiempo que es dócil y amistoso.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';


    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })


})

$('#chocolate').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Chocolate</h3></div><div class="parrafo1"><p>Es un lindo cachorro de 6 meses cafecito con botitas blancas. Es tímido, tranquilo y será de gran tamaño cuando termine de crecer.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';


    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })


})

$('#pexel').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Pexel</h3></div><div class="parrafo1"><p>Es un lindo perrito peludito de 4 años, mestizo poodle y tamaño pequeño. Es de color café y pelo largo, así que es probable que necesite mucha peluquería a lo largo de su vida para mantener el estilo.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';


    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })


})

$('#bigotes').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Bigotes</h3></div><div class="parrafo1"><p>Tiene 5 años de edad y tamaño mediano. Es súper peludito (no te dejes engañar por su corte de pelo) y le encanta salir a pasear. Es limpio, amoroso y ya está castrado.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';

    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })


})

$('#luna').click(function (e) {
    var img = e.target.src;

    var modal = '<div class=""><div class="modal" id="modal"><div class="nombre1"><h3>Luna</h3></div><div class="parrafo1"><p>Es una perrita cachorro de 2 meses, de tamaño mediano-grande, orejitas pequeñitas y naricita respingada. Es muy tierna y conversadora.</p></div><img src="' + img + '" class="modal__img"><div class="modal__boton" id="modal_salir">X</div></div></div>';


    $('#fotografias').append(modal)
    $('#modal_salir').click(function () {
        $('#modal').remove();
    })


})


$(document).keyup(function (e) {
    if (e.which == 27) {
        $('#modal').remove();
    }
})


