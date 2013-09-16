from django.http import HttpResponse
from django.template import Template,Context,loader
#from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

'''
def current_time(request):
    now = datetime.datetime.now()
    #simple way of using templates from the filesystem.
    #This is BAD because it doesn't account for missing files!
    fp = open('/home/yn/django/templates/mytemplate.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'now':now})
    return HttpResponse(html)
'''

def current_time(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #t = get_template('index.html')
    #t = loader.get_template('index.html')
    #html = t.render(Context({'now':now}))
    #return HttpResponse(html)
    #return render_to_response('index.html',{'now':now})
    return render_to_response('index.html',locals())

def hours_ahead(request,hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,dt)
    #return HttpResponse(html)
    #return render_to_response('hours_ahead.html',{'hour_offset':hour_offset,'next_time':next_time})
    return render_to_response('hours_ahead.html',locals())
