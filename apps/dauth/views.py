from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import *


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request):
        return super().post(request)
