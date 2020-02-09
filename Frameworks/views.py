from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Frameworks
from .forms import FrameworksForm

def index(request):
    frameworks = Frameworks.objects.order_by('using_percentage')
    template = loader.get_template('Frameworks/list.html')
    context = {"frameworks": frameworks}
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'POST':
        form = FrameworksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FrameworksForm()

    template = loader.get_template('Frameworks/create.html')
    context = {"form": form}
    return HttpResponse(template.render(context, request))