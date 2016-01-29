$(document).ready(function() {
  //Hide RSS feed by default
  $('#rss_div').hide();
  $('#commands').hide();

  setInterval(function ajax(){
    $.ajax({
      url : "index.time_ajax/",
      success : function(data) {
        // console.log('Success!')
        $('#django-time').html(data)
      },
      error : function() {
          console.log('Not happening')
      }
    });//end ajax
    if ($('#commands').css("visibility") == "visible") {
        $('#commands').hide();
    } else {
      //do nothing
    }
  }, 15000);
});
window.onload = function(){
    if (annyang) {
        var commands = {
            'Hello': function() {
                responsiveVoice.speak("Hello, I can hear you!", "UK English Male", {pitch: -2});
            },
            'Show calendar': function() {
              $('#rss_div').hide();
              $('#commands').hide();
              $('#calendar_div').fadeIn(1000);
            },
            'Hide calendar': function() {
              $('#calendar_div').fadeOut(1000);
            },
            'Show news': function() {
              $('#calendar_div').hide();
              $('#commands').hide();
              $('#rss_div').fadeIn(1000);
            },
            'Hide news': function() {
              $('#rss_div').fadeOut(1000);
            },
            'Who are you': function() {
                responsiveVoice.speak("Hi, my name is Alfred.", "UK English Male", {pitch: -2});
            },
            'What is on my calendar': function() {
              name = $('#name:first').text()
              date = $('#date:first').text()
              time = $('#time:first').text()
              // responsiveVoice.speak(name + date + time, "UK English Male", {pitch: -2});
              responsiveVoice.speak("Your first event is " + name, "UK English Male", {pitch: -2});


              var event_date = new Date(date),
                // locale = "en-us",
                // month = event_date.toLocaleString(locale, { month: "long" });
                month = event_date.toString();
              // console.log(event_date)
              // var date = event_date.substr(0, 16);
              var date = month.substr(0, 16);
              // console.log(date)

              responsiveVoice.speak("The date of your event is " + date, "UK English Male", {pitch: -2});
              responsiveVoice.speak("It starts at " + time, "UK English Male", {pitch: -2});

              // Maybe use to determine date?
              var d = new Date();
              var month = d.getMonth()+1;
              var day = d.getDate();
              var year = d.getFullYear();
            },
            'Show commands': function() {
              $('#rss_div').hide();
              $('#calendar_div').hide();
              $('#commands').fadeIn(1000)
            },
            'Hide commands': function() {
              $('#commands').fadeOut(1000)
            },
            'Who is the fairest of them all': function() {
              responsiveVoice.speak("Sidney Marie Pettit is the fairest of them all.", "UK English Male", {pitch: -2});
            }

        };
        annyang.addCommands(commands);
        annyang.start();
        responsiveVoice.speak("I have loaded", "UK English Male", {pitch: -2});

    }
}
