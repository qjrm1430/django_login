from django.urls import path
from .views import getIndex

urlpatterns = [
    path("", getIndex, name="user-admin"),
]
