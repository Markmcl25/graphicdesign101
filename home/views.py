from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')

def home_view(request):
    return render(request, 'home/home.html')  

def shopping_bag(request):
    """A view to return the shopping bag page"""
    return render(request, 'shopping_bag.html')      