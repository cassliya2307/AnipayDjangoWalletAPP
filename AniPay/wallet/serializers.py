from rest_framework import serializers

from .models import Wallet, Transaction


class WalletTransferSerializer(serializers.Serializer):
    receiver_wallet = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    idempotency_key = serializers.UUIDField()
    description = serializers.CharField(max_length=255, required=False)


    def validate_amount(self , value):
        if value < 0:
            raise serializers.ValidationError("Amount cannot be negative😑")
        return value

    def validate_receiver_wallet(self , value):
        try:
            receiver_wallet = Wallet.objects.get(wallet_number=value)
        except Wallet.DoesNotExist:
            raise Exception('Wallet does not exist!🪙')
        return receiver_wallet



class RecentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Transaction
        fields = ['receiver_wallet','amount','reference', 'status', 'created_at', 'transaction_type']


class DashBoardSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    wallet = serializers.CharField(max_length=10)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=3)
    status = serializers.CharField(max_length=10)
    transactions = RecentTransactionSerializer(many=True)

