from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import viewsForCategory

urlpatterns = [
    path('category/', viewsForCategory.ApiCategoryListView.as_view()),
    path('category/refactor/<int:pk>/', viewsForCategory.ApiCategoryUpdate.as_view()),
    path('category/delete/<int:pk>/', viewsForCategory.ApiCategoryDestroy.as_view()),
    path('api/category/<int:pk>/', viewsForCategory.ApiCategoryDestroy.as_view()),
    # path('movie/', views.ApiMovie.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)