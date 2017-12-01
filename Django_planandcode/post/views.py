from django.shortcuts import render
from .githubAPI import *
from django.template.loader import get_template
from django.http import HttpResponse
import datetime


def index(request):
    global deneme
    if (request.method == "POST"):
        get_text = request.POST["textfield"]
        get_text2 = request.POST["textfield2"]

        deneme = GitHubAPI(get_text, get_text2, "PlanAndCode")

    return render(request, 'index.html', {})

def page2(request):
     t = None
     if (request.method == "POST2"):
        t = deneme.show_projects()

     return render(request, 'page2.html', {'show': t})
