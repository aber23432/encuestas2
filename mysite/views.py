from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def inicio(request):
	return render(request, 'inicio/inicio.html')