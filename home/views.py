from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import PortfolioProject
from .forms import InquiryForm, OrderForm
from django.contrib import messages
from .models import Order, OrderItem
from home.models import PortfolioProject

# View for the homepage and /home/
def index(request):
    """ A view to return the homepage """
    return render(request, 'home/index.html')

def shopping_bag(request):
    """Render the shopping bag page."""
    return render(request, 'home/shopping_bag.html')

def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.save()

            # Save order items
            bag_items = request.session.get('bag', {})
            total_price = 0
            for item_id, quantity in bag_items.items():
                product = PortfolioProject.objects.get(id=item_id)
                total_price += product.price * quantity
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )
            order.total_price = total_price
            order.save()

            # Clear the shopping bag
            request.session['bag'] = {}
            messages.success(request, "Your order has been placed successfully!")
            return redirect('checkout_success')
    else:
        form = OrderForm()

    return render(request, 'home/checkout.html', {'form': form})    

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
