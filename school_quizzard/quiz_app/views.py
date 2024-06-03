from django.shortcuts import render,HttpResponse
from .services import generate_question
# Create your views here.

# def index(request):
#     return HttpResponse("This is our Home Page")

# def about(request):
#     return HttpResponse("This is our About Page")

# def services(request):
#     return HttpResponse("This is our Services Page")

def home(request):
    if request.method == "POST":
        text = request.POST['paragraph']
        questions = generate_question(text)
        context = {'questions': questions}
        return render(request, 'base.html', context)
    return render(request,'base.html')