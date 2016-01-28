# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453946421.130071
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/time_ajax.html'
_template_uri = 'time_ajax.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        time = context.get('time', UNDEFINED)
        date = context.get('date', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        time = context.get('time', UNDEFINED)
        date = context.get('date', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div id="django-time">\r\n    <h2>')
        __M_writer(str(time))
        __M_writer('</h2>\r\n    <h3>')
        __M_writer(str(date))
        __M_writer('</h3>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "time_ajax.html", "line_map": {"49": 3, "67": 61, "59": 5, "37": 1, "38": 2, "57": 3, "58": 5, "43": 8, "28": 0, "61": 6, "60": 6}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/time_ajax.html"}
__M_END_METADATA
"""
