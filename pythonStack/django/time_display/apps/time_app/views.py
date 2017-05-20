from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "somekey":""
        }
    return render(request,'time_app/index.html', context)
