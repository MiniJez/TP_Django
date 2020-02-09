from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Frameworks
from .forms import FrameworksForm

def index(request):
    frameworks = Frameworks.objects.order_by('-using_percentage')
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

def delete(request, pk):
    framework = Frameworks.objects.get(pk=pk)
    framework.delete()
    return HttpResponseRedirect('/')

def update(request, pk):
    if request.method == 'POST':
        framework = Frameworks.objects.get(pk=pk)
        form = FrameworksForm(request.POST, instance=framework)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        framework = Frameworks.objects.get(pk=pk)
        data = {'id': framework.id, 'name': framework.name, 'language': framework.language, 'using_percentage': framework.using_percentage}
        form = FrameworksForm(initial=data)

    template = loader.get_template('Frameworks/update.html')
    context = {"form": form, "id": framework.id}
    return HttpResponse(template.render(context, request))