# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453739992.890363
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/quickstart.html'
_template_uri = 'quickstart.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html>\r\n  <head>\r\n    <!-- <script type="text/javascript">\r\n      // Your Client ID can be retrieved from your project in the Google\r\n      // Developer Console, https://console.developers.google.com\r\n      var CLIENT_ID = \'124147417835-dhse39i0se1jmtuojn1lagthpvr7v0b0.apps.googleusercontent.com\';\r\n\r\n      var SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"];\r\n\r\n      /**\r\n       * Check if current user has authorized this application.\r\n       */\r\n      function checkAuth() {\r\n        gapi.auth.authorize(\r\n          {\r\n            \'client_id\': CLIENT_ID,\r\n            \'scope\': SCOPES.join(\' \'),\r\n            \'immediate\': true\r\n          }, handleAuthResult);\r\n      }\r\n\r\n      /**\r\n       * Handle response from authorization server.\r\n       *\r\n       * @param {Object} authResult Authorization result.\r\n       */\r\n      function handleAuthResult(authResult) {\r\n        var authorizeDiv = document.getElementById(\'authorize-div\');\r\n        if (authResult && !authResult.error) {\r\n          // Hide auth UI, then load client library.\r\n          authorizeDiv.style.display = \'none\';\r\n          loadCalendarApi();\r\n        } else {\r\n          // Show auth UI, allowing the user to initiate authorization by\r\n          // clicking authorize button.\r\n          authorizeDiv.style.display = \'inline\';\r\n        }\r\n      }\r\n\r\n      /**\r\n       * Initiate auth flow in response to user clicking authorize button.\r\n       *\r\n       * @param {Event} event Button click event.\r\n       */\r\n      function handleAuthClick(event) {\r\n        gapi.auth.authorize(\r\n          {client_id: CLIENT_ID, scope: SCOPES, immediate: false},\r\n          handleAuthResult);\r\n        return false;\r\n      }\r\n\r\n      /**\r\n       * Load Google Calendar client library. List upcoming events\r\n       * once client library is loaded.\r\n       */\r\n      function loadCalendarApi() {\r\n        gapi.client.load(\'calendar\', \'v3\', listUpcomingEvents);\r\n      }\r\n\r\n      /**\r\n       * Print the summary and start datetime/date of the next ten events in\r\n       * the authorized user\'s calendar. If no events are found an\r\n       * appropriate message is printed.\r\n       */\r\n      function listUpcomingEvents() {\r\n        var request = gapi.client.calendar.events.list({\r\n          \'calendarId\': \'primary\',\r\n          \'timeMin\': (new Date()).toISOString(),\r\n          \'showDeleted\': false,\r\n          \'singleEvents\': true,\r\n          \'maxResults\': 10,\r\n          \'orderBy\': \'startTime\'\r\n        });\r\n\r\n        request.execute(function(resp) {\r\n          var events = resp.items;\r\n          appendPre(\'Upcoming events:\');\r\n\r\n          if (events.length > 0) {\r\n            for (i = 0; i < events.length; i++) {\r\n              var event = events[i];\r\n              var when = event.start.dateTime;\r\n              if (!when) {\r\n                when = event.start.date;\r\n              }\r\n              appendPre(event.summary + \' (\' + when + \')\')\r\n            }\r\n          } else {\r\n            appendPre(\'No upcoming events found.\');\r\n          }\r\n\r\n        });\r\n      }\r\n\r\n      /**\r\n       * Append a pre element to the body containing the given message\r\n       * as its text node.\r\n       *\r\n       * @param {string} message Text to be placed in pre element.\r\n       */\r\n      function appendPre(message) {\r\n        var pre = document.getElementById(\'output\');\r\n        var textContent = document.createTextNode(message + \'\\n\');\r\n        pre.appendChild(textContent);\r\n      }\r\n\r\n    </script> -->\r\n\r\n  </head>\r\n  <body>\r\n    <script src="https://apis.google.com/js/client.js?onload=checkAuth">\r\n    </script>\r\n    <div id="authorize-div" style="display: none">\r\n      <span>Authorize access to Google Calendar API</span>\r\n      <!--Button for the user to click to initiate auth sequence -->\r\n      <button id="authorize-button" onclick="handleAuthClick(event)">\r\n        Authorize\r\n      </button>\r\n    </div>\r\n    <pre id="output"></pre>\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "28": 22, "22": 1}, "source_encoding": "utf-8", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/quickstart.html", "uri": "quickstart.html"}
__M_END_METADATA
"""
