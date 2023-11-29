function Validar(){
  var errorS = document.getElementById("Errorsalario");
  var errorN = document.getElementById("Errornombre");
  var nombre = document.getElementById("nombre").value;
  var salario = document.getElementById("salario").value;
  var validador = true;

  if(nombre == "" ){
    errorN.style="display:block";
    validador=false;
  }else{
     errorN.style="display:none";
    validador=true;
  }
    


  if(salario==""){
    errorS.style="display:block";
  validador=false;
  }else{
    errorS.style="display:none";
    validador=true;
  }
if(validador==true){
  var formulario = document.getElementById("formulario");
  formulario.submit()
}
  

  
  
}