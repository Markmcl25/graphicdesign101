from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import PortfolioProject, Order, OrderItem
from .forms import InquiryForm, OrderForm
from .forms import ProjectMessageForm
from django.contrib import messages


# View for the homepage and /home/
def index(request):
    """ A view to return the homepage """
    return render(request, 'home/index.html')


def shopping_bag(request):
    """Render the shopping bag page."""
    return render(request, 'home/shopping_bag.html')


def checkout(request):
    """ A view to handle the checkout process """
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

def add_to_cart(request, project_id):
    """ Add a project to the shopping cart """
    project = get_object_or_404(PortfolioProject, id=project_id)
    quantity = int(request.POST.get('quantity', 1))
    bag = request.session.get('bag', {})

    if str(project_id) in bag:
        bag[str(project_id)] += quantity
    else:
        bag[str(project_id)] = quantity

    request.session['bag'] = bag
    messages.success(request, f'{project.title} has been added to your shopping bag!')
    return redirect('project_detail', project_id=project_id)    


def checkout_success(request):
    """ A view to display the checkout success page """
    return render(request, 'home/checkout_success.html')


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
    """ A view to display details of a specific project and handle messages """
    project = get_object_or_404(PortfolioProject, id=project_id)
    if request.method == 'POST':
        form = ProjectMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.project = project  # Link the message to the project
            message.save()
            messages.success(request, "Your message has been sent!")
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectMessageForm()
    
    return render(request, 'home/project_detail.html', {'project': project, 'form': form})

def submit_inquiry(request):
    """ A view to handle inquiries submission """
    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect('home')  # Redirect to the homepage or thank you page
    else:
        form = InquiryForm()

    return render(request, 'home/inquiry_form.html', {'form': form})
