from django.shortcuts import render,HttpResponse
from django.http import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse


def homepage(request):
    return render(request, 'index.html')

def plan(request):
    return render(request, 'plan.html')

