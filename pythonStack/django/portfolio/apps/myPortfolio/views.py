from django.shortcuts import render


def index(request):
    return render(request, 'myPortfolio/index.html')

def testimonials(request):
    print(request.method)
    return render(request, 'myPortfolio/testimonials.html')

def about(request):
    print(request.method)
    return render(request, 'myPortfolio/about.html')

def projects(request):
    print(request.method)
    return render(request, 'myPortfolio/projects.html')
