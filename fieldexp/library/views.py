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

def submit(request):
    return render(request, 'library/submit.html', {})

def submit_paper(request):
    request_data = request.POST
'''
    response_string = "<br>".join(["filename: %s" % request_data["filename"],
                                 "type(s): %s" % request.POST.getlist('type'),
                                 "first name(s): %s" % request.POST.getlist('firstname'),
                                 "middle initial(s): %s" % request.POST.getlist('mi'),
                                 "last name(s): %s" % request.POST.getlist('lastname'),
                                 "title: %s" % request_data["title"],
                                 "citation: %s" % request_data["citation"],
                                 "jel: %s" % request_data["jel"],
                                 "keywords: %s" % request_data["keywords"],
                                 "yearmonth: %s" % request_data["yearmonth"],
                                 "abstract: %s" % request_data["abstract"],
                                 "submittee: %s" % request_data["submittee"],
                                 "email: %s" % request_data["email"],
                                ])
    '''
data = ", ".join(["file=%s" % request_data["filename"],
                  "type(s): %s" % request.POST.getlist('type'),
                  "first name(s): %s" % request.POST.getlist('firstname'),
                  "middle initial(s): %s" % request.POST.getlist('mi'),
                  "last name(s): %s" % request.POST.getlist('lastname'),
                  "title=%s" % request_data["title"],
                  "citation=%s" % request_data["citation"],
                  "JEL=%s" % request_data["jel"],
                  "keywords=%s" % request_data["keywords"],
                  "year=%s" % request_data["yearmonth"],
                  "abstract=%s" % request_data["abstract"],
                  "submittee=%s" % request_data["submittee"],
                  "email=%s" % request_data["email"],
                  ])
    paper = Paper(data)
    paper.errors
    return HttpResponseRedirect(response_string)
