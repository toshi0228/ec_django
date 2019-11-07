from django.urls import path
from .views import provisional 

urlpatterns = [
    path('', provisional, name="pro"),
]