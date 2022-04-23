from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse("Hi")
    return render(request, 'about.html')

def Home(request):
    #return HttpResponse("How are u?")
    return render(request, 'Home.html')
