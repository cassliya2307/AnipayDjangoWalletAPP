from django.urls import path
from .views import create_wallet , login

urlpatterns = [
    path('create_wallet/', create_wallet, name='create_wallet'),
    path('login/', login, name='login'),
]
