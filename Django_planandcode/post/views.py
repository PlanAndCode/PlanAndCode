from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
	return HttpResponse('<b> Plan and Code </b>')
