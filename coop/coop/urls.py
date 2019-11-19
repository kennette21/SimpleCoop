from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ToDo: bad url paths, fix please. should not have the base of products/
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('frontend.urls')), # ToDo: visually separate urls by frontend vs backend vs api
]
