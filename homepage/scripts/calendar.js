  // Your Client ID can be retrieved from your project in the Google
  // Developer Console, https://console.developers.google.com
  var CLIENT_ID = '124147417835-dhse39i0se1jmtuojn1lagthpvr7v0b0.apps.googleusercontent.com';

  var SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"];

  /**
   * Check if current user has authorized this application.
   */
  function checkAuth() {
    gapi.auth.authorize(
      {
        'client_id': CLIENT_ID,
        'scope': SCOPES.join(' '),
        'immediate': true
      }, handleAuthResult);
  }

  /**
   * Handle response from authorization server.
   *
   * @param {Object} authResult Authorization result.
   */
  function handleAuthResult(authResult) {
    var authorizeDiv = document.getElementById('authorize-div');
    if (authResult && !authResult.error) {
      // Hide auth UI, then load client library.
      authorizeDiv.style.display = 'none';
      $('.section2').hide();
      loadCalendarApi();
    } else {
      // Show auth UI, allowing the user to initiate authorization by
      // clicking authorize button.
      // $('#myModal').modal('show');
      // $('.modal-body').text('Authorize access to your Google calendar.')
      authorizeDiv.style.display = 'inline';
    }
  }

  /**
   * Initiate auth flow in response to user clicking authorize button.
   *
   * @param {Event} event Button click event.
   */
  function handleAuthClick(event) {
    gapi.auth.authorize(
      {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
      handleAuthResult);
    return false;
  }

  ///////////Timer for loadCalendarApi
  setInterval(function timer(){
    // var old = document.getElementById('event').remove();
    // old.parentNode.removeChild(old);
    $('#output').remove();
    $('#gcal').append("<tbody id='output'></tbody>");
    loadCalendarApi()
  }, 1800000);

  /**
   * Load Google Calendar client library. List upcoming events
   * once client library is loaded.
   */
  function loadCalendarApi() {
    gapi.client.load('calendar', 'v3', listUpcomingEvents);
  }

  /**
   * Print the summary and start datetime/date of the next ten events in
   * the authorized user's calendar. If no events are found an
   * appropriate message is printed.
   */
  function listUpcomingEvents() {
    var request = gapi.client.calendar.events.list({
      'calendarId': 'primary',
      'timeMin': (new Date()).toISOString(),
      'startTime':'startTime',
      'showDeleted': false,
      'singleEvents': true,
      'maxResults': 10,
      'orderBy': 'startTime'
    });

    //console.log(request)

    request.execute(function(resp) {
      var events = resp.items;
      //appendPre('Upcoming events:');
      //console.log(events)

      if (events.length > 0) {
        for (i = 0; i < events.length; i++) {
          var event = events[i];
          var when = event.start.dateTime;
          // var time = when.substr(13, 3);
          //
          // //console.log(when)
          var d = new Date(when);
          // var time_12 = hours12(d)
          // time = time_12 + time
          var time = formatAMPM(d)
          when = d.toLocaleDateString();
          if (!when) {
            when = event.start.date;
          }
          //console.log(event.summary)
          // appendPre(event.summary + ' (' + when + ')')
          appendPre(event.summary, when, time)
        }
      } else {
        appendPre('No upcoming events found.');
      }

    });
    function hours12(date) { return (date.getHours() + 24) % 12 || 12; }

    function formatAMPM(date) {
      var hours = date.getHours();
      var minutes = date.getMinutes();
      var ampm = hours >= 12 ? 'pm' : 'am';
      hours = hours % 12;
      hours = hours ? hours : 12; // the hour '0' should be '12'
      minutes = minutes < 10 ? '0'+minutes : minutes;
      var strTime = hours + ':' + minutes + ' ' + ampm;
      return strTime;
    }
  }

  /**
   * Append a pre element to the body containing the given message
   * as its text node.
   *
   * @param {string} message Text to be placed in pre element.
   */
  function appendPre(message, when, time) {
    var pre = document.getElementById('output');
    var textContent = document.createTextNode(message + '\n');
    // pre.appendChild(textContent);
    var newdiv = document.createElement('tr');
    var divId = 'event';
    newdiv.setAttribute('id', divId);
    newdiv.innerHTML = "<td id='name'>" + message + '</td>' + "<td id='date'>" + when + '</td>' + "<td id='time'>" + time + '</td>'
    pre.appendChild(newdiv)
  }
