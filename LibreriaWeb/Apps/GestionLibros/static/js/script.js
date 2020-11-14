
$(document).ready(function() {
  $(".boton_detalles").click(function() {
      alert("Sitio web en construcción, por favor intente más tarde.");
  });
});

var slideIndex = 1;
showSlides(slideIndex);

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

// Controles para imagen siguiente y anterior con flechas:
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Permite cambiar imagenes clicando los puntitos: 
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function buscar(){
  var busqueda = document.getElementById('txt_busqueda').value;
  /*Esto debiese tomar las palabras y buscarlas en alguna base de datos, pero aún no hay base de datos. */
}

/* Estas dos funciones de abajo abren y cierran la ventana para iniciar sesión. */
function miUsuario(){
  var modal = document.getElementById('modal_usuario');
  if(modal.style.display == "none" || modal.style.display == ""){
    modal.style.display= "block";
  }
  else{
    modal.style.display = "none";
  }
  
}

function cerrarModal(){
  var modal = document.getElementById("modal_usuario");
  modal.style.display = "none";
}

function logIn(){
  var username = document.getElementById("username").value;
  var pass = document.getElementById("password").value;

  var usuariosRegistrados = 15;
  var encontrado = false;

  //Aquí se debería contrastar las credenciales con las presentes en la base de datos de los usuarios registrados.
  for(var i = 0; i<usuariosRegistrados; i++){
    if(encontrado ==true){
      alert("Ahora se iniciará sesión!");
    }
  }
  alert("Las credenciales de usuario no son válidas. Intente de nuevo.")
  encontrado = false;
}


function enviarCorreo(){
  var asunto = document.getElementById("asunto").value;
  var nombre = document.getElementById("nombre").value;
  var email = document.getElementById("email").value;
  var numero = document.getElementById("numero").value;
  var comentario = document.getElementById("comentario").value;
  
  if(nombre.value == ""|| nombre.value == undefined){
    alert("El nombre del emisor no puede quedar en blanco!");
  }
  else if(email.value == ""||email.value == undefined){
    alert("El campo email no puede quedar en blanco!");
  }
  else if(numero.value == ""||numero.value == undefined){
    alert("El numero de telefono no puede quedar en blanco!");
  }
  else if(comentario.value == ""||comentario.value == undefined){
    alert("Se debe proporcionar un comentario o contenido del mensaje!");
  }
  else{
    alert("Mensaje enviado con exito! (no realmente, pero no han habido inconvenientes)");
  }
}