from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework import generics

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def index(request):
    products_list = Product.objects.all()
    order_list = request.user.order.products.all() if hasattr(request.user, 'order') else None ## I don't like this solution

    context = {
        'products_list': products_list,
        'order_list': order_list,
    }
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
    except:
        raise Http404("Product does not exist")

    return render(request, 'products/detail.html', {'product': product})