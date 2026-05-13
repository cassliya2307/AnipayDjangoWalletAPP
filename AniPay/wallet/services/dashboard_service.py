from wallet.models import Transaction

def get_dashboard_data(user):
    wallet = user.wallet
    transactions = Transaction.objects.filter(
        sender_wallet=wallet
    ).order_by('-created_at')[:5]

    return{
        'message': f"Hi, {user.first_name}!",
        'wallet': wallet.wallet_number,
        'balance' : wallet.balance,
        'status' : wallet.status,
        'currency' : wallet.currency,
        'transactions' : transactions
    }