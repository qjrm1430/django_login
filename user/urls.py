from django.urls import path

from .views import join_user, login_user, logout_user

urlpatterns = [
    path("", login_user, name="user-login"),
    path("join/", join_user, name="user-join"),
    path("logout/", logout_user, name="user-logout"),
]
