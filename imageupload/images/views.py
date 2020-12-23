from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Zdravo')

def broj(request, br=0):
    return HttpResponse('Broj: ' + str(br))

def rec(request, str):
    return HttpResponse('Rec: ' + str)

def params(request):
    return HttpResponse('Params: ' + str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))

def regex(request, godina, mesec):
    return HttpResponse('Godina: ' + godina + ' Mesec: ' + mesec)

def hello(request):
    return render(request, 'images/hello.html')