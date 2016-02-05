# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454632784.957297
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'modal']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def modal():
            return render_modal(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>homepage</title>\r\n\r\n')
        __M_writer('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>\r\n    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\r\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>\r\n\r\n')
        __M_writer('    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery.simpleWeather/3.0.2/jquery.simpleWeather.min.js"></script>\r\n')
        __M_writer('    <script src="http://code.responsivevoice.org/responsivevoice.js"></script>\r\n')
        __M_writer('    <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/annyang/1.1.0/annyang.min.js"></script> -->\r\n\r\n\r\n')
        __M_writer('    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/weather.css">\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/stock_ticker.css">\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/weather.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/stock_ticker.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/calendar.js"></script>\r\n    <script src="https://apis.google.com/js/client.js?onload=checkAuth"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/annayng.min.js"></script>\r\n\r\n\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'modal'):
            context['self'].modal(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_modal(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def modal():
            return render_modal(context)
        __M_writer = context.writer()
        __M_writer('\r\n      <div class="modal fade" id="myModal" tabindex="-1" role="dialog">\r\n        <div class="modal-dialog">\r\n          <div class="modal-content">\r\n            <div class="modal-header">\r\n              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n              <h4 class="modal-title">Google Calendar</h4>\r\n            </div>\r\n            <div class="modal-body">\r\n              <p id="authorize-div">Click here to authorize access to your Google Calendar</p>\r\n            </div>\r\n            <div class="modal-footer">\r\n              <button class="btn btn-primary" id="authorize-button" onclick="handleAuthClick(event)">\r\n                Authorize\r\n              </button>\r\n            </div>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/base.htm", "source_encoding": "utf-8", "line_map": {"67": 69, "68": 72, "69": 72, "70": 72, "76": 47, "17": 4, "82": 47, "19": 0, "88": 50, "94": 50, "31": 2, "32": 4, "33": 5, "100": 94, "37": 5, "38": 15, "39": 20, "40": 22, "41": 24, "42": 28, "43": 28, "44": 28, "45": 29, "46": 29, "47": 30, "48": 30, "49": 31, "50": 31, "51": 32, "52": 32, "53": 34, "54": 34, "55": 42, "56": 42, "57": 42, "62": 49}, "uri": "base.htm"}
__M_END_METADATA
"""
