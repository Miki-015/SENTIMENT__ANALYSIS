from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    #return HttpResponse("hello")
    return render(request, 'index.html')