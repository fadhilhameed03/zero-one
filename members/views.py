from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def projects(request):
    return render(request, "explore.html")