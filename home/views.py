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

def portfolio(request):
    """A view to display the portfolio page."""
    portfolio_projects = [
        {'title': 'Project 1', 'description': 'Description of Project 1', 'image': '/path/to/image1.jpg'},
        {'title': 'Project 2', 'description': 'Description of Project 2', 'image': '/path/to/image2.jpg'},
        {'title': 'Project 3', 'description': 'Description of Project 3', 'image': '/path/to/image3.jpg'},
    ]
    return render(request, 'portfolio.html', {'portfolio_projects': portfolio_projects})     