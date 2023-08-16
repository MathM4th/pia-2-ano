from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def sobre(request):
    return render(request, "app/sobre.html")

def equipe(request):
    return render(request, "app/equipe.html")
    