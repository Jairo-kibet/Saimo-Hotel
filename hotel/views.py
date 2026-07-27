from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request): 
    return render(request, "saimo/index.html")

def xxx(request): 
    return render(request, "saimo/xxx.html")

def accommodation(request): 
    return render(request, "saimo/accommodation.html")

def dining(request): 
    return render(request, "saimo/dining.html")

def swimming(request): 
    return render(request, "saimo/swimming.html")

def recreational(request): 
    return render(request, "saimo/recreational.html")

def gallery(request): 
    return render(request, "saimo/gallery.html")


def conference(request): 
    return render(request, "saimo/conference.html")

def bar(request): 
    return render(request, "saimo/bar.html")

def contact(request): 
    return render(request, "saimo/contact.html")