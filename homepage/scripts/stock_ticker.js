$(document).ready(function() {
  var i = 1;
  var $stocks = $("#Stocks"),
      animationend = (Modernizr.prefixed('animation') + "End").replace(/^ms/, "MS").replace(/^Webkit/, "webkit").replace(/^Moz.*/, "animationend");

  ////////////////////////////////////////
  // Get stock data via YQL query
  var getStocks = function () {

    var ticker = getTicker()


    var wsql = "select * from yahoo.finance.quotes where symbol in " + ticker;
  	stockYQL = 'http://query.yahooapis.com/v1/public/yql?q='+encodeURIComponent(wsql)+'&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json&callback=?';

    //http://download.finance.yahoo.com/d/quotes.csv?s=^DJI,^IXIC,^GSPC,^TNX&f=snl1d1t1c1ohg
    return $.ajax({
      url: stockYQL,
      dataType: 'json'
    });
  };

  ////////////////////////////////////////
  //Get Ticker symbols
  function getTicker(){
    if(i==1){
      i = i+1;
      return ticker = "('^GSPC')"
    }
    else if(i==2){
      i = i+1;
      return ticker = "('^IXIC')"
    }
    else if(i==3){
      i = i+1;
      return ticker = "('^DJX')"
    }
    else if(i==4){
      i = i+1;
      return ticker = "('XOM')"
    }
    else if(i==5){
      i = i+1;
      return ticker = "('MSFT')"
    }
    else if(i==6){
      i = i+1;
      return ticker = "('GOOG')"
    }
    else if(i==7){
      i = i+1;
      return ticker = "('IBM')"
    }
    else if(i==8){
      i = 1;
      return ticker = "('AAPL')"
    }
    else{
      return ticker = "('KO')"
    }
  }

  ////////////////////////////////////////
  // Format Numbers
  var getRepString = function (rep) {
    rep = rep+''; // coerce to string
    if (rep >= 1000000000) {
      return (rep / 1000000000).toFixed(1).replace(/\.0$/, '') + 'G';
    } else if (rep >= 1000000) {
      return (rep / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
    } else if (rep >= 1000) {
      return (rep / 1000).toFixed(1).replace(/\.0$/, '') + 'K';
    } else {
      return rep;
    }
  }


  ////////////////////////////////////////
  // Replace children with [data-replace] attribute given a data object
  $.fn.dataReplace = function(data) {
    var $replacers = this.find("[data-replace]");

    if ( $replacers.length ) {
      $replacers.each(function(){
        var $this = $(this);
        var replace = $this.data("replace");
        var content = data[replace];

        if ( replace === 'Name' ) {
          content = content.replace(/\W/gi, ' ');
        } else if ( replace === 'Volume' ) {
          content = getRepString(content);
        }

        //console.log("replace",replace,":",data[replace]);
        $this.html(content);
      });
      return true;
    } else {
      return false;
    }
  }


  /////////////////////////////////////////
  // Timer
  var interval = null;

  jQuery(function(){
    interval = setInterval(callFunc, 12000);
  });

  function callFunc(){
    jQuery('#Stocks').trigger('click');
  }

  ////////////////////////////////////////
  // Update on Click
  $stocks.on("click",function(){

    var _this = this;
  	var $this = $(this);
    var _uniqueID = "stockLoad.unique"+Math.floor(Math.random() * (100 - 1) + 1);

    $this
      .removeClass("is-Loaded")
      .addClass("is-Loading");

    if ( $this.hasClass("is-Visible") ) {
      $this.css("animation-play-state", "running");
    }

    //console.log("Triggering AJAX... ");

    $this
      .one(_uniqueID,function(data){

        //console.log("_uniqueID",_uniqueID,"triggered");
        window.setTimeout(function(){

          $this.dataReplace($this.data("quote"));

          if ( ! $this.is(":visible") ) {
             $this.addClass("is-Visible").fadeIn(1000);
          }

          $this
            .removeClass("is-Loading")
            .addClass("is-Loaded");
            //.html($this.data("stocks"));
          //console.log("Done!");
        }, 600)
      })
      .on(animationend,function(event){
        $this.css("animation-play-state","paused");
      });

    getStocks().done(function(data){
      //console.log("AJAX Returned.",data);

      //$this.data("stocks",formatStocks(data));
      $this.data("quote",data.query.results.quote);

      if ( Modernizr.cssanimations && $this.css("animation-play-state") === "running" ) {
        //console.log("Animating!");
        $this.on(animationend,function(event){
            $this.trigger(_uniqueID);
        });

        window.setTimeout(function(){
          //console.log("animation end no-trigger fallback");
          $this.trigger(_uniqueID);
        },2000);
      } else {
        //console.log("Not animating.");
        $this.trigger(_uniqueID);
      }
    });

  });

  $stocks.hide().click();

});
