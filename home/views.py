from django.shortcuts import render, redirect
from django.urls import reverse
from .models import PortfolioProject

# View for the homepage and /home/
def index(request):
    """ A view to return the homepage """
    return render(request, 'home/index.html')

# View for the shopping bag page
def shopping_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'shopping_bag.html')

# Redirect to login page
def example_view(request):
    """ Redirects to the login page """
    return redirect(reverse('account_login'))

# View for the portfolio page
def portfolio(request):
    """ A view to display the portfolio page """
    portfolio_projects = [
        {'title': 'Project 1', 'description': 'Description of Project 1', 'image': 'images/project1.jpg'},
        {'title': 'Project 2', 'description': 'Description of Project 2', 'image': 'images/project2.jpg'},
        {'title': 'Project 3', 'description': 'Description of Project 3', 'image': 'images/project3.jpg'},
    ]
    return render(request, 'home/portfolio.html', {'portfolio_projects': portfolio_projects})

def portfolio(request):
    """ A view to display the portfolio page """
    portfolio_projects = [
        {'id': 1, 'title': 'Project 1', 'description': 'Innovative logo design', 'image': '/static/images/project1.jpg'},
        {'id': 2, 'title': 'Project 2', 'description': 'Creative branding solutions', 'image': '/static/images/project2.jpg'},
        {'id': 3, 'title': 'Project 3', 'description': 'Stunning poster designs', 'image': '/static/images/project3.jpg'},
    ]
    return render(request, 'home/portfolio.html', {'portfolio_projects': portfolio_projects})

def project_detail(request, project_id):
    """ A view to display details of a specific project """
    projects = {
        1: {'title': 'Project 1', 'description': 'Innovative logo design', 'image': '/static/images/project1.jpg'},
        2: {'title': 'Project 2', 'description': 'Creative branding solutions', 'image': '/static/images/project2.jpg'},
        3: {'title': 'Project 3', 'description': 'Stunning poster designs', 'image': '/static/images/project3.jpg'},
    }
    project = projects.get(project_id, None)
    if not project:
        return render(request, '404.html')  # Handle project not found
    return render(request, 'home/project_detail.html', {'project': project})
