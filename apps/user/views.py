from rest_framework.response import Response
# from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from core.errors import Error, APIError


class UserView(APIView):
    
    def get(self, request):
        raise APIError(Error._DEFAULT_MESSAGE, extra=["this is a message"])
        return Response('hello')