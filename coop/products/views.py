from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
    }
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
    except:
        raise Http404("Product does not exist")

    return render(request, 'products/detail.html', {'product': product})