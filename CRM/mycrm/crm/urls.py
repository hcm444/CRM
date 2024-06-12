# crm/urls.py
from django.urls import path
from .views import customer_list, add_customer, customer_detail

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('add/', add_customer, name='add_customer'),
    path('<int:pk>/', customer_detail, name='customer_detail'),
]