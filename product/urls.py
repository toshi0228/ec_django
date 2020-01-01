from django.urls import path
from .views import provisional, plan_list

#  product_list

urlpatterns = [
    path('', provisional, name="pro"),
    path('index/', plan_list, name='product_list'),
]