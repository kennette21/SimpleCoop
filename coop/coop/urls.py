from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # bad url paths, fix please. should not have the base of products/
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
