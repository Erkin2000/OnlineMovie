from django.urls import path
from main.views.ViewsAuthorization import Auth

urlpatterns = [
    path('/Users', Auth)
]