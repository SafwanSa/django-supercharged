from django.urls import include, path
from . import views

urlpatterns = [
    # path('', views.UserView.as_view())
    path('', views.V.as_view())
]
