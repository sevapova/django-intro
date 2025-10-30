from django.contrib import admin
from django.urls import path

from pages.views import (
    index_view, 
    root_view, 
    home_view, 
    about_view, 
    projects_view, 
    contact_view, 
    greeting_view, 
    get_products_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view, name='root'),
    path('', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('projects/', projects_view, name='projects'),
    path('contact/', contact_view, name='contact'),
    path('greeting/<str:name>', greeting_view),
    path('products/<int:product_id>', get_products_view),
]
