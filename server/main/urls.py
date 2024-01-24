from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ApiCategory.as_view()),
    path('category/<int:pk>/', views.ApiCategory.as_view()),
    # path('movie/', views.ApiMovie.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)