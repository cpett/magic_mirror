# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454202910.369455
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
        __M_writer('<div class="col-sm-3 col-md-3 col-lg-3 rss" id="rss_div">\r\n  <!-- start feedwind code -->\r\n    <iframe  height="400"  width="300" src="http://feed.mikle.com/widget/?rssmikle_url=http%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_topstories.rss&rssmikle_frame_width=300&rssmikle_frame_height=400&frame_height_by_article=0&rssmikle_target=_blank&rssmikle_font=Arial%2C%20Helvetica%2C%20sans-serif&rssmikle_font_size=12&rssmikle_border=off&responsive=off&text_align=left&text_align2=left&corner=off&scrollbar=on&autoscroll=on_mc&scrolldirection=up&scrollstep=3&mcspeed=50&sort=Off&rssmikle_title=on&rssmikle_title_bgcolor=%230066FF&rssmikle_title_color=%23FFFFFF&rssmikle_item_bgcolor=%23FFFFFF&rssmikle_item_title_length=55&rssmikle_item_title_color=%230066FF&rssmikle_item_border_bottom=on&rssmikle_item_description=on&item_link=off&rssmikle_item_description_length=150&rssmikle_item_description_color=%23666666&rssmikle_item_date=gl1&rssmikle_timezone=Etc%2FGMT&datetime_format=%25b%20%25e%2C%20%25Y%20%25l%3A%25M%20%25p&item_description_style=text&item_thumbnail=full&item_thumbnail_selection=auto&article_num=15&rssmikle_item_podcast=off&"\r\n      scrolling="no" name="rssmikle_frame" marginwidth="0" marginheight="0" vspace="0" hspace="0" frameborder="0">\r\n    </iframe>\r\n    <div >\r\n      <a href="http://feed.mikle.com/" target="_blank" style="color:#CCCCCC;">RSS Feed Widget</a>\r\n      <!--Please display the above link in your web page according to Terms of Service.-->\r\n    </div>\r\n    <!-- end feedwind code --><!--  end  feedwind code -->\r\n</div>\r\n\r\n<!-- start feedwind code -->\r\n  <iframe  height="400"  width="400"\r\n    src="http://feed.mikle.com/widget/?rssmikle_url=http%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_topstories.rss%7Chttp%3A%2F%2Frss.cnn.com%2Frss%2Fcnn_tech.rss%7Chttp%3A%2F%2Frss.cnn.com%2Frss%2Fmoney_latest.rss&rssmikle_frame_width=400&rssmikle_frame_height=400&frame_height_by_article=0&rssmikle_target=_blank&rssmikle_font=Arial%2C%20Helvetica%2C%20sans-serif&rssmikle_font_size=12&rssmikle_border=off&responsive=off&text_align=left&text_align2=left&corner=off&scrollbar=off&autoscroll=on_mc&scrolldirection=up&scrollstep=3&mcspeed=50&sort=Off&rssmikle_title=on&rssmikle_title_sentence=News&rssmikle_title_bgcolor=%230066FF&rssmikle_title_color=%23FFFFFF&rssmikle_item_bgcolor=%23FFFFFF&rssmikle_item_title_length=55&rssmikle_item_title_color=%230066FF&rssmikle_item_border_bottom=on&rssmikle_item_description=on&item_link=off&rssmikle_item_description_length=150&rssmikle_item_description_color=%23666666&rssmikle_item_date=gl1&rssmikle_timezone=Etc%2FGMT&datetime_format=%25b%20%25e%2C%20%25Y%20%25l%3A%25M%20%25p&item_description_style=text&item_thumbnail=full&item_thumbnail_selection=auto&article_num=15&rssmikle_item_podcast=off&"\r\n    scrolling="no" name="rssmikle_frame" marginwidth="0" marginheight="0" vspace="0" hspace="0" frameborder="0">\r\n  </iframe>\r\n  <div style="font-size:10px; text-align:center; width:400px;">\r\n    <a href="http://feed.mikle.com/" target="_blank" style="color:#CCCCCC;">RSS Feed Widget</a>\r\n    <!--Please display the above link in your web page according to Terms of Service.-->\r\n  </div>\r\n  <!-- end feedwind code --><!--  end  feedwind code -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "quickstart.html", "line_map": {"17": 0, "28": 22, "22": 1}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\magic_mirror\\homepage\\templates/quickstart.html"}
__M_END_METADATA
"""
