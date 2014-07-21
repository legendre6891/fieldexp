from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.http import HttpResponse
from library.forms import PaperForm
# Create your views here.

def index(request):
    
    form = PaperForm(request.POST)
    
    if form.is_valid():
        form.save()
    
    return render_to_response('library/index.html',
                              locals(),
                              context_instance=RequestContext(request))
