# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454631653.911627
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
        time = context.get('time', UNDEFINED)
        date = context.get('date', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        time = context.get('time', UNDEFINED)
        date = context.get('date', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="section1">\r\n  <div class="my_container col-sm-12 col-md-12 col-lg-12">\r\n<!-- Div for Google Calendar -->\r\n    <div class="col-sm-4 col-md-4 col-lg-4" id="calendar_div">\r\n<!-- Google Calendar Table -->\r\n      <h1 class="text-center" id="test">Upcoming Events</h1>\r\n      <table class="table table-hover" id="gcal">\r\n        <thead class="text-center">\r\n          <tr>\r\n            <th>Event Name</th>\r\n            <th>Start Date</th>\r\n            <th>Start Time</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody id="output" class="text-left">\r\n        </tbody>\r\n      </table>\r\n    </div>\r\n<!-- RSS Feed -->\r\n    <div class="col-sm-3 col-md-3 col-lg-3 rss" id="rss_div">\r\n      <!-- start feedwind code -->\r\n      <iframe  height="410"  width="400"\r\n        src="http://feed.mikle.com/widget/?rssmikle_url=http%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_topstories.rss%7Chttp%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_tech.rss%7Chttp%3A%2F%2Frss.cnn.com%2Frss%2Fmoney_latest.rss&rssmikle_frame_width=400&rssmikle_frame_height=400&frame_height_by_article=0&rssmikle_target=_blank&rssmikle_font=Arial%2C%20Helvetica%2C%20sans-serif&rssmikle_font_size=12&rssmikle_border=off&responsive=off&text_align=left&text_align2=left&corner=off&scrollbar=off&autoscroll=on_mc&scrolldirection=up&scrollstep=3&mcspeed=50&sort=Off&rssmikle_title=on&rssmikle_title_sentence=News&rssmikle_title_bgcolor=%230066FF&rssmikle_title_color=%23FFFFFF&rssmikle_item_bgcolor=%23FFFFFF&rssmikle_item_title_length=55&rssmikle_item_title_color=%230066FF&rssmikle_item_border_bottom=on&rssmikle_item_description=on&item_link=off&rssmikle_item_description_length=150&rssmikle_item_description_color=%23666666&rssmikle_item_date=gl1&rssmikle_timezone=Etc%2FGMT&datetime_format=%25b%20%25e%2C%20%25Y%20%25l%3A%25M%20%25p&item_description_style=text&item_thumbnail=full&item_thumbnail_selection=auto&article_num=15&rssmikle_item_podcast=off&"\r\n        scrolling="no" name="rssmikle_frame" marginwidth="0" marginheight="0" vspace="0" hspace="0" frameborder="0">\r\n      </iframe>\r\n      <div style="font-size:10px; text-align:center; width:400px;">\r\n        <a href="http://feed.mikle.com/" target="_blank" style="color:#CCCCCC;">RSS Feed Widget</a>\r\n        <!--Please display the above link in your web page according to Terms of Service.-->\r\n      </div>\r\n      <!-- end feedwind code --><!--  end  feedwind code -->\r\n    </div>\r\n<!-- Show Alfred\'s Commands -->\r\n    <div class="col-sm-3 col-md-3 col-lg-3" id="commands">\r\n      <table class="table table-hover">\r\n        <thead class="text-center">\r\n          <h2>Command List</h2>\r\n        </thead>\r\n        <tbody class="text-left">\r\n          <tr>\r\n            <td>Hello</td>\r\n            <td>Who are you?</td>\r\n          </tr>\r\n          <tr>\r\n            <td>Show calendar</td>\r\n            <td>Hide calendar</td>\r\n          </tr>\r\n          <tr>\r\n            <td>Show news</td>\r\n            <td>Hide news</td>\r\n          </tr>\r\n          <tr>\r\n            <td>Show commands</td>\r\n            <td>Hide commands</td>\r\n          </tr>\r\n          <tr>\r\n            <td>What is on my calendar?</td>\r\n            <td></td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n    </div>\r\n<!-- Weather Widget -->\r\n    <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3 pull-right" id="weather">\r\n      <div id="django-time">\r\n        <h2>')
        __M_writer(str(time))
        __M_writer('</h2>\r\n        <h3>')
        __M_writer(str(date))
        __M_writer('</h3>\r\n      </div>\r\n      <div id="weather_body"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/93/loader.gif" alt="Loading..." class="loading"><br />Loading...\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n<div class="section2 text-center" id="section2">\r\n  <!-- Google Authorization -->\r\n  <div id="authorize-div" style="display: none">\r\n    <span class="authorize">Authorize access to Google Calendar API</span>\r\n      <button class="btn btn-default auth-btn" id="authorize-button" onclick="handleAuthClick(event)">\r\n        Authorize\r\n      </button>\r\n  </div>\r\n</div>\r\n<!-- Stock Ticker -->\r\n<div class="section3">\r\n  <div id="Stocks">\r\n    <span class="Symbol">\r\n      <b class="Stat"><i data-replace=\'Symbol\'>PWR</i>:<i data-replace=\'StockExchange\'>NYSE</i></b>\r\n      <b class="Label">( <i data-replace=\'Name\'>Quanta Services</i> )</b>\r\n    </span>\r\n    <span class="Price"><b class="Label">Last Price</b> <b class="Stat">$<i data-replace=\'Bid\'></i></b></span>\r\n    <span class="Change"><b class="Label">Change</b> <b class="Stat"><i data-replace=\'Change\'></i></b> <b class="Stat">(<i data-replace=\'ChangeinPercent\'></i>)</b></span>\r\n    <span class="Volume"><b class="Label">Volume</b> <b class="Stat" data-replace=\'Volume\'></b></span>\r\n    <span class="MarketCapitalization"><b class="Label">Mkt Cap</b> <b class="Stat">$<i data-replace="MarketCapitalization"></i></b></span>\r\n    <span class="LastUpdated"><b class="Label">Last Trade</b> <b class="Stat"><i data-replace=\'LastTradeDate\'></i> <i data-replace="LastTradeTime"></i> </b></span>\r\n  </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/index.html", "source_encoding": "utf-8", "line_map": {"48": 3, "66": 60, "37": 1, "56": 3, "57": 68, "42": 100, "59": 69, "28": 0, "58": 68, "60": 69}, "uri": "index.html"}
__M_END_METADATA
"""
