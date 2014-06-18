from django.shortcuts import render, render_to_response, Http404, HttpResponse, HttpResponseRedirect, RequestContext
from django.core.urlresolvers import reverse

from .models import Bank

def home(request):
    context = RequestContext(request)
    return HttpResponseRedirect(reverse('unsecured_credits'))

def banks(request):
    context = RequestContext(request)

    banks = Bank.objects.all()
    return render_to_response('banks/banks.html', locals(), context)
