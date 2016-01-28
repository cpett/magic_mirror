// $(document).ready(function() {
//   // Your Client ID can be retrieved from your project in the Google
//   // Developer Console, https://console.developers.google.com
//   var CLIENT_ID = '124147417835-dhse39i0se1jmtuojn1lagthpvr7v0b0.apps.googleusercontent.com';
//
//   var SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"];
//
//   console.log("HERE")
//
//   /**
//    * Check if current user has authorized this application.
//    */
//   function checkAuth() {
//     gapi.auth.authorize(
//       {
//         'client_id': CLIENT_ID,
//         'scope': SCOPES.join(' '),
//         'immediate': true
//       }, handleAuthResult);
//   }
//
//   /**
//    * Handle response from authorization server.
//    *
//    * @param {Object} authResult Authorization result.
//    */
//   function handleAuthResult(authResult) {
//     console.log('handleAuthResult')
//     var authorizeDiv = document.getElementById('authorize-div');
//     if (authResult && !authResult.error) {
//       // Hide auth UI, then load client library.
//       authorizeDiv.style.display = 'none';
//       loadCalendarApi();
//     } else {
//       // Show auth UI, allowing the user to initiate authorization by
//       // clicking authorize button.
//       authorizeDiv.style.display = 'inline';
//     }
//   }
//
//   /**
//    * Initiate auth flow in response to user clicking authorize button.
//    *
//    * @param {Event} event Button click event.
//    */
//   function handleAuthClick(event) {
//     console.log('handleAuthClick')
//     gapi.auth.authorize(
//       {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
//       handleAuthResult);
//     return false;
//   }
//
//   /**
//    * Load Google Calendar client library. List upcoming events
//    * once client library is loaded.
//    */
//   function loadCalendarApi() {
//     console.log('loadCalendarApi')
//     gapi.client.load('calendar', 'v3', listUpcomingEvents);
//   }
//
//   /**
//    * Print the summary and start datetime/date of the next ten events in
//    * the authorized user's calendar. If no events are found an
//    * appropriate message is printed.
//    */
//   function listUpcomingEvents() {
//     console.log('listUpcomingEvents')
//     var request = gapi.client.calendar.events.list({
//       'calendarId': 'primary',
//       'timeMin': (new Date()).toISOString(),
//       'showDeleted': false,
//       'singleEvents': true,
//       'maxResults': 10,
//       'orderBy': 'startTime'
//     });
//
//     request.execute(function(resp) {
//       console.log('request.execute')
//       var events = resp.items;
//       appendPre('Upcoming events:');
//
//       if (events.length > 0) {
//         for (i = 0; i < events.length; i++) {
//           var event = events[i];
//           var when = event.start.dateTime;
//           if (!when) {
//             when = event.start.date;
//           }
//           appendPre(event.summary + ' (' + when + ')')
//         }
//       } else {
//         appendPre('No upcoming events found.');
//       }
//
//     });
//   }
//
//   /**
//    * Append a pre element to the body containing the given message
//    * as its text node.
//    *
//    * @param {string} message Text to be placed in pre element.
//    */
//   function appendPre(message) {
//     console.log('appendPre')
//     var pre = document.getElementById('output');
//     var textContent = document.createTextNode(message + '\n');
//     pre.appendChild(textContent);
//   }
// });
