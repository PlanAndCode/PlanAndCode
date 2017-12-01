
from django.shortcuts import render
from .githubAPI import *
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

deneme=None

def index(request):
    global deneme
    if (request.method == "POST"):
        get_text = request.POST["textfield"]
        get_text2 = request.POST["textfield2"]
        get_text3 = request.POST["textfield3"]
        deneme = GitHubAPI(get_text, get_text2, get_text3)

    return render(request, 'index.html', {})

def page2(request):
    t=GitHubAPI("burakfurkanaksahin", "software2017", "PlanAndCode")
    #show2=t.new_project( "deneme", "deneme", "deneme")
    show=t.show_project()
    return render(request,'page2.html',context={'show': show },)

