from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from wallet.models import Wallet
from wallet.serializers import WalletTransferSerializer, DashBoardSerializer
from wallet.services.dashboard_service import get_dashboard_data
from wallet.services.wallet_transfer import wallet_to_wallet_transfer

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_to_wallet(request):
    sender = request.user.wallet
    serializer = WalletTransferSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    amount = serializer.validated_data['amount']
    idempotency_key = serializer.validated_data['idempotency_key']
    receiver_wallet = serializer.validated_data['receiver_wallet']
    receiver = get_object_or_404(Wallet, wallet_number=receiver_wallet.pk)
    description = serializer.validated_data['description']
    tx = wallet_to_wallet_transfer(sender, receiver, amount, idempotency_key, description)

    return Response(
        {
        "Reference": tx.reference,
        "Amount": "${}".format(tx.amount),
        "Status": tx.status,
        "Description": tx.description,
        "Created": tx.created_at,
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user
    dashboard_data = get_dashboard_data(user)
    serializer = DashBoardSerializer(dashboard_data)
    return Response(serializer.data, status=status.HTTP_200_OK)


