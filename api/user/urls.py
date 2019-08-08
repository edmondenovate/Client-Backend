from django.urls import path
from .views import RegisteredUsersView

urlpatterns = [
    path('users', RegisteredUsersView.as_view(), name="users-all")
]