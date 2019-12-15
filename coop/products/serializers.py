from rest_framework import serializers
from products.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = '__all__'
