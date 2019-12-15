from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.index, name='index'),
    path('products/<int:product_id>/', views.detail, name='detail'),
    # --- API --- #
    # ToDo: consider better way of separating/defining urls (e.g. swagger)
    path('api/products/', views.ProductListCreate.as_view()),

    path('api/orders/', views.OrderListCreate.as_view()),
]
