from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.onboarding_service import create_user_and_wallet
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def create_wallet(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    create_user_and_wallet(serializer.validated_data)
    return Response( {"message" : "Registration Successful"}, status=status.HTTP_201_CREATED)