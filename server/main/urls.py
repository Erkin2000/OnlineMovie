from django.urls import path
from .views import example_view
urlpatterns = [
    path('allmovie/', example_view),
]
