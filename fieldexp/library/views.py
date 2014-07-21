from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'library/index.html', {})
    #return render_to_response('library/index.html', locals(),
            #context_instance=RequestContext(request))
    template = loader.get_template('library/index.html')
    return HttpResponse()
