# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454265364.649271
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date = context.get('date', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        time = context.get('time', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date = context.get('date', UNDEFINED)
        def content():
            return render_content(context)
        time = context.get('time', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!-- Weather/Greeting -->\r\n<div class="section1">\r\n  <div class="my_container col-sm-12 col-md-12 col-lg-12">\r\n<!-- Div for Google Calendar -->\r\n    <div class="col-sm-6 col-md-3 col-lg-3" id="calendar_div">\r\n      <script type="text/javascript">\r\n        // Your Client ID can be retrieved from your project in the Google\r\n        // Developer Console, https://console.developers.google.com\r\n        var CLIENT_ID = \'124147417835-dhse39i0se1jmtuojn1lagthpvr7v0b0.apps.googleusercontent.com\';\r\n\r\n        var SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"];\r\n\r\n        /**\r\n         * Check if current user has authorized this application.\r\n         */\r\n        function checkAuth() {\r\n          gapi.auth.authorize(\r\n            {\r\n              \'client_id\': CLIENT_ID,\r\n              \'scope\': SCOPES.join(\' \'),\r\n              \'immediate\': true\r\n            }, handleAuthResult);\r\n        }\r\n\r\n        /**\r\n         * Handle response from authorization server.\r\n         *\r\n         * @param {Object} authResult Authorization result.\r\n         */\r\n        function handleAuthResult(authResult) {\r\n          var authorizeDiv = document.getElementById(\'authorize-div\');\r\n          if (authResult && !authResult.error) {\r\n            // Hide auth UI, then load client library.\r\n            authorizeDiv.style.display = \'none\';\r\n            $(\'.section2\').hide();\r\n            loadCalendarApi();\r\n          } else {\r\n            // Show auth UI, allowing the user to initiate authorization by\r\n            // clicking authorize button.\r\n            authorizeDiv.style.display = \'inline\';\r\n          }\r\n        }\r\n\r\n        /**\r\n         * Initiate auth flow in response to user clicking authorize button.\r\n         *\r\n         * @param {Event} event Button click event.\r\n         */\r\n        function handleAuthClick(event) {\r\n          gapi.auth.authorize(\r\n            {client_id: CLIENT_ID, scope: SCOPES, immediate: false},\r\n            handleAuthResult);\r\n          return false;\r\n        }\r\n\r\n        ///////////Timer for loadCalendarApi\r\n        setInterval(function timer(){\r\n          // var old = document.getElementById(\'event\').remove();\r\n          // old.parentNode.removeChild(old);\r\n          $(\'#output\').remove();\r\n          $(\'#gcal\').append("<tbody id=\'output\'></tbody>");\r\n          loadCalendarApi()\r\n        }, 43200000);\r\n\r\n        /**\r\n         * Load Google Calendar client library. List upcoming events\r\n         * once client library is loaded.\r\n         */\r\n        function loadCalendarApi() {\r\n          gapi.client.load(\'calendar\', \'v3\', listUpcomingEvents);\r\n        }\r\n\r\n        /**\r\n         * Print the summary and start datetime/date of the next ten events in\r\n         * the authorized user\'s calendar. If no events are found an\r\n         * appropriate message is printed.\r\n         */\r\n        function listUpcomingEvents() {\r\n          var request = gapi.client.calendar.events.list({\r\n            \'calendarId\': \'primary\',\r\n            \'timeMin\': (new Date()).toISOString(),\r\n            \'startTime\':\'startTime\',\r\n            \'showDeleted\': false,\r\n            \'singleEvents\': true,\r\n            \'maxResults\': 10,\r\n            \'orderBy\': \'startTime\'\r\n          });\r\n\r\n          //console.log(request)\r\n\r\n          request.execute(function(resp) {\r\n            var events = resp.items;\r\n            //appendPre(\'Upcoming events:\');\r\n            //console.log(events)\r\n\r\n            if (events.length > 0) {\r\n              for (i = 0; i < events.length; i++) {\r\n                var event = events[i];\r\n                var when = event.start.dateTime;\r\n                // var time = when.substr(13, 3);\r\n                //\r\n                // //console.log(when)\r\n                var d = new Date(when);\r\n                // var time_12 = hours12(d)\r\n                // time = time_12 + time\r\n                var time = formatAMPM(d)\r\n                when = d.toLocaleDateString();\r\n                if (!when) {\r\n                  when = event.start.date;\r\n                }\r\n                //console.log(event.summary)\r\n                // appendPre(event.summary + \' (\' + when + \')\')\r\n                appendPre(event.summary, when, time)\r\n              }\r\n            } else {\r\n              appendPre(\'No upcoming events found.\');\r\n            }\r\n\r\n          });\r\n          function hours12(date) { return (date.getHours() + 24) % 12 || 12; }\r\n\r\n          function formatAMPM(date) {\r\n            var hours = date.getHours();\r\n            var minutes = date.getMinutes();\r\n            var ampm = hours >= 12 ? \'pm\' : \'am\';\r\n            hours = hours % 12;\r\n            hours = hours ? hours : 12; // the hour \'0\' should be \'12\'\r\n            minutes = minutes < 10 ? \'0\'+minutes : minutes;\r\n            var strTime = hours + \':\' + minutes + \' \' + ampm;\r\n            return strTime;\r\n          }\r\n        }\r\n\r\n        /**\r\n         * Append a pre element to the body containing the given message\r\n         * as its text node.\r\n         *\r\n         * @param {string} message Text to be placed in pre element.\r\n         */\r\n        function appendPre(message, when, time) {\r\n          var pre = document.getElementById(\'output\');\r\n          var textContent = document.createTextNode(message + \'\\n\');\r\n          // pre.appendChild(textContent);\r\n          var newdiv = document.createElement(\'tr\');\r\n          var divId = \'event\';\r\n          newdiv.setAttribute(\'id\', divId);\r\n          newdiv.innerHTML = "<td id=\'name\'>" + message + \'</td>\' + "<td id=\'date\'>" + when + \'</td>\' + "<td id=\'time\'>" + time + \'</td>\'\r\n          pre.appendChild(newdiv)\r\n        }\r\n      </script>\r\n      <script src="https://apis.google.com/js/client.js?onload=checkAuth"></script>\r\n<!-- Google Calendar Table -->\r\n      <h1 class="text-center" id="test">Upcoming Events</h1>\r\n      <table class="table table-hover" id="gcal">\r\n        <thead class="text-center">\r\n          <tr>\r\n            <th>Event Name</th>\r\n            <th>Start Date</th>\r\n            <th>Start Time</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody id="output" class="text-left">\r\n        </tbody>\r\n      </table>\r\n    </div>\r\n<!-- RSS Feed -->\r\n    <div class="col-sm-3 col-md-3 col-lg-3 rss" id="rss_div">\r\n      <!-- start feedwind code -->\r\n      <iframe  height="410"  width="400"\r\n        src="http://feed.mikle.com/widget/?rssmikle_url=http%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_topstories.rss%7Chttp%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_tech.rss%7Chttp%3A%2F%2Frss.cnn.com%2Frss%2Fmoney_latest.rss&rssmikle_frame_width=400&rssmikle_frame_height=400&frame_height_by_article=0&rssmikle_target=_blank&rssmikle_font=Arial%2C%20Helvetica%2C%20sans-serif&rssmikle_font_size=12&rssmikle_border=off&responsive=off&text_align=left&text_align2=left&corner=off&scrollbar=off&autoscroll=on_mc&scrolldirection=up&scrollstep=3&mcspeed=50&sort=Off&rssmikle_title=on&rssmikle_title_sentence=News&rssmikle_title_bgcolor=%230066FF&rssmikle_title_color=%23FFFFFF&rssmikle_item_bgcolor=%23FFFFFF&rssmikle_item_title_length=55&rssmikle_item_title_color=%230066FF&rssmikle_item_border_bottom=on&rssmikle_item_description=on&item_link=off&rssmikle_item_description_length=150&rssmikle_item_description_color=%23666666&rssmikle_item_date=gl1&rssmikle_timezone=Etc%2FGMT&datetime_format=%25b%20%25e%2C%20%25Y%20%25l%3A%25M%20%25p&item_description_style=text&item_thumbnail=full&item_thumbnail_selection=auto&article_num=15&rssmikle_item_podcast=off&"\r\n        scrolling="no" name="rssmikle_frame" marginwidth="0" marginheight="0" vspace="0" hspace="0" frameborder="0">\r\n      </iframe>\r\n      <div style="font-size:10px; text-align:center; width:400px;">\r\n        <a href="http://feed.mikle.com/" target="_blank" style="color:#CCCCCC;">RSS Feed Widget</a>\r\n        <!--Please display the above link in your web page according to Terms of Service.-->\r\n      </div>\r\n      <!-- end feedwind code --><!--  end  feedwind code -->\r\n    </div>\r\n<!-- Show Alfred\'s Commands -->\r\n    <div class="col-sm-3 col-md-3 col-lg-3" id="commands">\r\n      <table class="table table-hover">\r\n        <thead class="text-center">\r\n          <h2>Command List</h2>\r\n        </thead>\r\n        <tbody class="text-left">\r\n          <tr>\r\n            <td>Hello</td>\r\n            <td>Who are you?</td>\r\n          </tr>\r\n          <tr>\r\n            <td>Show calendar</td>\r\n            <td>Hide calendar</td>\r\n          </tr>\r\n          <tr>\r\n            <td>Show news</td>\r\n            <td>Hide news</td>\r\n          </tr>\r\n          <tr>\r\n            <td>Show commands</td>\r\n            <td>Hide commands</td>\r\n          </tr>\r\n          <tr>\r\n            <td>What is on my calendar?</td>\r\n            <td></td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n    </div>\r\n<!-- Weather Widget -->\r\n    <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 pull-right" id="weather">\r\n      <div id="django-time">\r\n        <h2>')
        __M_writer(str(time))
        __M_writer('</h2>\r\n        <h3>')
        __M_writer(str(date))
        __M_writer('</h3>\r\n      </div>\r\n      <div id="weather_body"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/93/loader.gif" alt="Loading..." class="loading"><br />Loading...\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n<div class="section2 text-center" id="section2">\r\n  <!-- Google Authorization -->\r\n  <div id="authorize-div" style="display: none">\r\n    <span class="authorize">Authorize access to Google Calendar API</span>\r\n    <!--Button for the user to click to initiate auth sequence -->\r\n      <button class="btn btn-default auth-btn" id="authorize-button" onclick="handleAuthClick(event)">\r\n        Authorize\r\n      </button>\r\n  </div>\r\n</div>\r\n<!-- Stock Ticker -->\r\n<div class="section3">\r\n  <div id="Stocks">\r\n    <span class="Symbol">\r\n      <b class="Stat"><i data-replace=\'Symbol\'>PWR</i>:<i data-replace=\'StockExchange\'>NYSE</i></b>\r\n      <b class="Label">( <i data-replace=\'Name\'>Quanta Services</i> )</b>\r\n    </span>\r\n    <span class="Price"><b class="Label">Last Price</b> <b class="Stat">$<i data-replace=\'Bid\'></i></b></span>\r\n    <span class="Change"><b class="Label">Change</b> <b class="Stat"><i data-replace=\'Change\'></i></b> <b class="Stat">(<i data-replace=\'ChangeinPercent\'></i>)</b></span>\r\n    <span class="Volume"><b class="Label">Volume</b> <b class="Stat" data-replace=\'Volume\'></b></span>\r\n    <span class="MarketCapitalization"><b class="Label">Mkt Cap</b> <b class="Stat">$<i data-replace="MarketCapitalization"></i></b></span>\r\n    <span class="LastUpdated"><b class="Label">Last Trade</b> <b class="Stat"><i data-replace=\'LastTradeDate\'></i> <i data-replace="LastTradeTime"></i> </b></span>\r\n  </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"48": 3, "66": 60, "37": 1, "56": 3, "57": 215, "42": 248, "59": 216, "28": 0, "58": 215, "60": 216}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/index.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
