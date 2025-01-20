from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import PortfolioProject, Order, OrderItem
from .forms import InquiryForm, OrderForm, ProjectMessageForm
from django.contrib import messages

# View for the homepage and /home/
def index(request):
    """ A view to return the homepage """
    return render(request, 'home/index.html')

def shopping_bag(request):
    """Render the shopping bag page with items and total price."""
    bag = request.session.get('bag', {})  # Retrieve the session cart
    bag_items = []  # List to hold item details
    grand_total = 0  # Total cost of items in the cart

    for item_id, quantity in bag.items():
        product = get_object_or_404(PortfolioProject, id=item_id)  # Get the product
        total_price = product.price * quantity  # Calculate total price for the product
        grand_total += total_price  # Add to the grand total

        # Append product details to bag_items list
        bag_items.append({
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price,
            'image': product.image,
            'quantity': quantity,
            'total_price': total_price,
        })

    # Pass bag items and grand total to the template
    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return render(request, 'home/shopping_bag.html', context)

def remove_item(request, project_id):  # Moved out of the `shopping_bag` function
    """Remove an item from the shopping bag."""
    bag = request.session.get('bag', {})
    if str(project_id) in bag:
        del bag[str(project_id)]  # Remove the item
        request.session['bag'] = bag  # Save the updated bag
        messages.success(request, "Item removed from your shopping bag.")
    return redirect('shopping_bag')

import stripe
from django.conf import settings

def checkout(request):
    """ A view to handle the checkout process with Stripe integration """
    stripe.api_key = settings.STRIPE_SECRET_KEY  # Set Stripe secret key

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None

            # Calculate total price based on shopping cart
            bag_items = request.session.get('bag', {})
            total_price = sum(PortfolioProject.objects.get(id=item_id).price * quantity for item_id, quantity in bag_items.items())

            # Create Stripe Payment Intent
            try:
                intent = stripe.PaymentIntent.create(
                    amount=int(total_price * 100),  # Convert to cents
                    currency='usd',
                    payment_method_types=['card'],
                    receipt_email=order.email,
                )
                
                # Save Stripe payment intent and total price to order
                order.total_price = total_price
                order.stripe_payment_intent = intent['id']
                order.save()

                # Save order items
                for item_id, quantity in bag_items.items():
                    product = PortfolioProject.objects.get(id=item_id)
                    OrderItem.objects.create(
                        order=order,
                        project=product,
                        quantity=quantity,
                        price=product.price
                    )

                # Clear the shopping bag after successful payment creation
                request.session['bag'] = {}
                messages.success(request, "Your order has been placed successfully!")
                return redirect('checkout_success')

            except stripe.error.StripeError as e:
                messages.error(request, f"Error processing payment: {e.user_message}")
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = OrderForm()

    context = {
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'home/checkout.html', context)

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

def update_quantity(request, project_id):
    """ Update the quantity of an item in the shopping bag. """
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        bag = request.session.get('bag', {})
        if str(project_id) in bag:
            bag[str(project_id)] = quantity
            messages.success(request, "Quantity updated successfully.")
        request.session['bag'] = bag
    return redirect('shopping_bag') 

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
