document.write('<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"><\/script>');
jQuery(document).ready(function ($) {
  // var Yelp = require('yelp');

  // <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBtapG46SfKsgGbZ-ChRlMFCxI6vgwcJRM&callback=initMap">

   if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(showPosition);
      } else {
          console.log("Geolocation is not supported by this browser.");
      }
      // if (jquery)
      // {console.log ("Hello");}


  // var yelp = new Yelp({
  //   consumer_key: 'consumer-key',
  //   consumer_secret: 'consumer-secret',
  //   token: 'token',
  //   token_secret: 'token-secret',
  // });

  // var x = document.getElementById("demo");

  $.getJSON('/JSON', {latitude: position.coords.latitude, longitude: position.coords.longitude}).done(function(data){
    console.log(data);
  }
  );


  function showPosition(position) {
      data = [position.coords.latitude, position.coords.longitude]
      // console.log("Latitude: " + position.coords.latitude +
      // "<br>Longitude: " + position.coords.longitude);
  }
});
