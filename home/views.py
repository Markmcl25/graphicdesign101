from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import PortfolioProject
from .forms import InquiryForm
from django.contrib import messages

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
    portfolio_projects = PortfolioProject.objects.all()  # Fetch from the database
    return render(request, 'home/portfolio.html', {'portfolio_projects': portfolio_projects})

# View for a specific project detail
def project_detail(request, project_id):
    """ A view to display details of a specific project """
    project = get_object_or_404(PortfolioProject, id=project_id)
    return render(request, 'home/project_detail.html', {'project': project})

def submit_inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect('home')  # Redirect to the homepage or thank you page
    else:
        form = InquiryForm()
    
    return render(request, 'home/inquiry_form.html', {'form': form})    
