from django.urls import path
from .views import transfer_to_wallet

urlpatterns = [
    path('transfer/', transfer_to_wallet, name='transfer_to_wallet'),
]