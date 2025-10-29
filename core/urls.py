from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view, index_view, greeting_view, get_products_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('', index_view, name='index'),
    path('greeting/<str:name>', greeting_view),
    path('products/<int:product_id>', get_products_view),
]
