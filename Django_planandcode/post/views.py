from django.shortcuts import render,HttpResponse
from django.http import *

# Create your views here.
def plan(request):
  	return render(request, 'plan.html', {})
def code(request):
  	return render(request, 'code.html', {})
