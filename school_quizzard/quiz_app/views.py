from django.shortcuts import render,HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("This is our Home Page")

# def about(request):
#     return HttpResponse("This is our About Page")

# def services(request):
#     return HttpResponse("This is our Services Page")

def home(request):
    return render(request,'base.html')