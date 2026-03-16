from django.contrib import admin
from .models import Wallet, Transaction, Ledger
# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
     list_display = ['wallet_number' , 'account_number' , 'balance', 'currency',  'status']
     list_editable = ['status']
     list_per_page = 10

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['sender_wallet' , 'receiver_wallet' , 'amount' , 'transaction_type' , 'status', 'created_at']
    list_per_page = 10

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ['transaction', 'balance_after', 'entry_type', 'created_at']
    list_per_page = 10