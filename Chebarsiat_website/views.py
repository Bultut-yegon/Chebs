from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')