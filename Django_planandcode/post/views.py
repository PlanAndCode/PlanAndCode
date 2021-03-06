
from django.shortcuts import render
from django import *

from .githubAPI import *

from .planCodeAPI import planCodeAPI

from django.template.loader import get_template
from django.http import HttpResponse
import datetime

from django.views.decorators.csrf import csrf_protect
get_text=None
get_text2=None
get_text3=None
get_text4=None
get_text5=None
pc=None
def index(request):
    global get_text
    global get_text2
    global get_text3
    global get_text4
    global get_text5
    global pc

    return render(request, 'index.html',  {})


def page2(request):
    global pc
    str2 = "\n"
    try:
        get_text=request.POST["projeAdd"]
        pc.createTrelloOrganization(get_text)
        pc.createProject(get_text)
        print(get_text)
    except:
        print('')


    try:
        get_text=request.POST["chooseProject"]
        pc.chooseProject(get_text)
    except:
        print('')

    delete = False

    try:
        delete= True
        get_text=request.POST["projeDelete"]
        pc.chooseProject(get_text)
        pc.deleteProject()
        print(get_text)
    except:
        print('')


    try:
        if (request.method == "POST"):
            get_text = request.POST["textfield"]
            get_text2 = request.POST["textfield2"]
            get_text3 = request.POST["textfield3"]
            get_text4 = request.POST["textfield4"]
            get_text5 = request.POST["textfield5"]
            pc= planCodeAPI(get_text,get_text2,get_text3,get_text4,get_text5)

    except:
        print('')

    projects = pc.showProjects()
    for i in range(0, len(projects)):
        str2 += str(i+1) +"." + projects[i] + "\n"
    if delete:
        str2.replace(get_text,'')
    return render(request, 'page2.html',  {'show' : str2})


def page3(request):
    global pc
    strMember="\n"
    members = pc.showMembers()
    print (members)
    for i in range(0, len(members[0])):
        strMember += str(i+1) + "." + members[0][i] + "\n"


    try:
        get_text=request.POST["memAdd"]
        pc.addMemberGitHub(get_text)
        print(get_text)
    except:
        print('')

    return render(request, 'page3.html',  {'showMember' : strMember })


def showTrello(request):
    global pc
    #print(pc.getTrelloDoingList().id)
    #print(pc.getTrelloBuildList().id)
    doingID=''
    buildID=''


    try:
        get_text = request.POST["chooseProject"]
        pc.chooseProject(get_text)
    except:
        print('')

    try:
        get_text=request.POST["cardAdd"]
        pc.createCard(pc.getTrelloToDoList().id,get_text)
        print(get_text)
    except:
        print('')

    toDo = pc.getTrelloToDoCards()
    doing = pc.getTrelloDoingCards()
    build = pc.getTrelloBuildCards()
    test = pc.getTrelloTestCards()
    deploy = pc.getTrelloDeployCards()

    return render(request,"ShowTrello.html",{'doingID' :  doingID, 'buildID' :  buildID,'toDo': toDo , 'doing' : doing, 'build' : build, 'test' :test, 'deploy': deploy})
