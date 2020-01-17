from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Frameworks

def index(request):
    frameworks = Frameworks.objects.all()
    template = loader.get_template('Frameworks/list.html')
    context = {"frameworks": frameworks}
    return HttpResponse(template.render(context, request))