
var zip = 0;
function getZip() 
{
  zip = document.getElementById("zc").value;
  alert(zip);
  $.getJSON('/JSON', zip).done(function(data){
    console.log(data);
  }
  );
}
  



