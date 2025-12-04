from django.shortcuts import render

# Create your views here.
def loginUser(request):
    context = {}
    return render(request, '', context)

def logOutUser (request):
    context = {}
    return render (request, '', context)

def registerUser (request):
    context = {}
    return render (request, '', context)