from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request,'home.html')

def templates(request):
    return render(request,'templates.html')

def details(request):
    return render(request,'details.html')

def template1(request):
    return render(request,'template1.html')
def template2(request):
    return render(request,'template2.html')
def template3(request):
    return render(request,'template3.html')

def resume(request):
    return render(request,'resume.html')