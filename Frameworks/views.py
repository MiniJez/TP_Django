from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Frameworks

def index(request):
    frameworks = Frameworks.objects.order_by('using_percentage')
    template = loader.get_template('Frameworks/list.html')
    context = {"frameworks": frameworks}
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('Frameworks/create.html')
    context = {}
    return HttpResponse(template.render(context, request))