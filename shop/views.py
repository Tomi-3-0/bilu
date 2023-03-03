from django.shortcuts import render

# Create your views here.

# store view
def store(request):
    # dictionary for contexts
    context = {}
    return render(request, 'shop/store.html', context)

def cart(request):
    # dictionary for contexts
    context = {}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    # dictionary for contexts
    context = {}
    return render(request, 'shop/checkout.html', context)

