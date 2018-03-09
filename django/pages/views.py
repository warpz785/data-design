from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homepageview(request):
	return HttpResponse("<h3>It's So Wonderful</h3>")

class HomePageView(TemplateView):
	template_name = 'home.html'

class aboutpageview(TemplateView):
	template_name = 'about.html'

class projectpageview(TemplateView):
	template_name = 'projects.html'
