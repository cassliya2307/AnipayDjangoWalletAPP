from django.db import models
from django.conf import settings
from .util import get_account_number , generate_reference

# Create your models here.

class Wallet(models.Model):
    CURRENCY_CHOICES = (
    ('NGN' , 'Naira'),
    ('USD' , 'Dollar'),
    ('EUR' , 'Euro')
    )
    wallet_number = models.CharField(max_length=10, unique=True)
    account_number = models.CharField(max_length=10, unique=True , default=get_account_number)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES , default='NGN')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class Transaction(models.Model):
    TRANSACTION_TYPE = (
    ('DEBIT', 'Debit'),
    ('CREDIT', 'Credit')
    )

    STATUS_TYPE = (
    ('PENDING', 'Pending'),
    ('SUCCESS', 'Success'),
    ('CANCELED', 'Canceled'),
    ('FAILED', 'Failed')
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender_wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='sender_wallet')
    receiver_wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='receiver_wallet')
    status = models.CharField(max_length=10, choices=STATUS_TYPE)
    description = models.TextField(blank=True)
    idempotency_key = models.UUIDField(unique=True, editable=False , blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=40, default=generate_reference)

class Ledger(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    balance_after = models.DecimalField(max_digits=40, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    entry_type = models.CharField(max_length=6, choices=Transaction.TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


