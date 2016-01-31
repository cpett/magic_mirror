$(document).ready(function() {
  //Hide RSS feed by default
  $('#rss_div').hide();
  $('#commands').hide();

  var i = 1;

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
    // if ($('#commands').css("visibility") == "visible") {
    //     $('#commands').hide();
    // } else {
    //   //do nothing
    // }
    if(i==1){
      $('#calendar_div').hide();
      $('#rss_div').fadeIn(1000);
      i++
    }
    else{
      $('#rss_div').hide();
      $('#calendar_div').fadeIn(1000);
      i = 1
    }
  }, 15000);
});
