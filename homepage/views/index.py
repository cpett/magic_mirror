from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):
    params = {}
    date_time = datetime.now()
    date = date_time.strftime('%a, %b %d, %Y')
    time = date_time.strftime('%I:%M %p')

    params = {
        'date': date,
        'time': time,
        'date_time': date_time,
    }
    return dmp_render_to_response(request, 'index.html', params)


@view_function
def time_ajax(request):
    params = {}
    date_time = datetime.now()
    date = date_time.strftime('%a, %b %d, %Y')
    time = date_time.strftime('%I:%M %p')

    params = {
        'date': date,
        'time': time,
        'date_time': date_time,
    }
    return dmp_render_to_response(request, 'time_ajax.html', params)
