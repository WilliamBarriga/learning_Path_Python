var d = document.getElementById("boton");
var contador = 0;

function hora(){
    horaActual = new Date ();
    horaProgramada = new Date();
    horaProgramada.setHours(21);
    horaProgramada.setMinutes(03);
    horaProgramada.setSeconds(0);
    return horaProgramada.getTime() - horaActual.getTime();
}


$(document).ready(function() {
    setTimeout(clickbutton(), 5000);
    
    function clickbutton() {
      $("boton").click();
      alert("Aqui llega");
    }
    $("boton").on('click',function() {
      console.log('action button clicked');
    });
  });