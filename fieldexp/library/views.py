from django.shortcuts import render, render_to_response, RequestContext
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    return render_to_response('library/index.html', locals(),
            context_instance=RequestContext(request))
