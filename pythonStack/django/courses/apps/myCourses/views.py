from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, "myCourses/index.html", context)

def confirm(request, id):
    course = Course.objects.get(id=id)

    context  = {
        'name': course.name,
        'description': course.description,
        'id': course.id
        }
    return render(request, 'myCourses/confirm.html', context)

def create(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    return redirect('/')

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
