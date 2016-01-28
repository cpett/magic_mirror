// Docs at http://simpleweatherjs.com
$(document).ready(function() {
  ///////////////////
  // Call simpleWeather every minute
  setInterval(function timer(){
    $.simpleWeather({
      woeid: '2477080', //2357536
      location: '',
      unit: 'f',
      success: function(weather) {
        if(weather.temp > 75) {
          $('body').animate({backgroundColor: '#F7AC57'}, 1500);
        } else {
          $('body').animate({backgroundColor: '#0091c2'}, 1500);
        }

        html = '<h1 class="icon-'+weather.code+'"></h1>';
        html += '<h3>'+weather.city+', '+weather.region+'</h3>';
        html += '<h4>'+ weather.currently + ' ' + weather.temp+'&deg;</h4>';
        //html += '<li>'+weather.tempAlt+'&deg;C</li></ul>';

        $("#weather_body").html(html);
      },
      error: function(error) {
        $("#weather_body").html('<p>'+error+'</p>');
      }
    });
  }, 10000);
});
