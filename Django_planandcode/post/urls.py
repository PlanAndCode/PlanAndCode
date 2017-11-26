from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.plan, name='plan'),
 	url(r'^$', views.code, name='code'),  
]
