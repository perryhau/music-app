from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
	return render_to_response('index.html')

def counterpoint(request):
	return render_to_response('counterpoint.html')
	

def improvisation(request):
	return render_to_response('improvisation.html')

def orchestration(request):
	return render_to_response('orchestration.html')

def documentation(request):
	return render_to_response('documentation.html')