from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.utils.translation import gettext_lazy as _
from core.errors import Error, APIError


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer