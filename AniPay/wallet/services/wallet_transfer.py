from decimal import Decimal
from uuid import UUID
from django.db import transaction
from wallet.models import Wallet, Transaction, Ledger


def wallet_to_wallet_transfer(sender : Wallet, receiver : Wallet, amount : Decimal, idempotency_key : UUID, description : str = None):
    amount = Decimal(amount)
    if sender.pk == receiver.pk:
        raise Exception('You cannot transfer money to yourself!😑')

    if amount > sender.balance:
        raise Exception('Insufficient funds!💸')

    existing_tx = Transaction.objects.filter(idempotency_key=idempotency_key).first()
    if existing_tx:
        return existing_tx

    with transaction.atomic():
        receiver_wallet = Wallet.objects.select_for_update().get(pk=receiver.pk)
        sender_wallet = Wallet.objects.select_for_update().get(pk=sender.pk)

        sender_wallet.balance -= amount
        receiver_wallet.balance += amount
        sender_wallet.save(update_fields=['balance'])
        receiver_wallet.save(update_fields=['balance'])


    tx = Transaction.objects.create(
        idempotency_key=idempotency_key,
        sender_wallet=sender,
        receiver_wallet=receiver,
        amount=amount,
        description=description,
        transaction_type = 'CREDIT',
        status = 'SUCCESS',
    )

    Ledger.objects.create(
        transaction=tx,
        amount=amount,
        balance_after= receiver.balance,
        entry_type = 'CREDIT',
        wallet = receiver_wallet,
    )

    Ledger.objects.create(
        transaction=tx,
        amount=amount,
        balance_after=sender.balance,
        entry_type='DEBIT',
        wallet=sender_wallet,
    )

    return tx


