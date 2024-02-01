from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from main.views import ViewsForActor

urlpatterns = [
    path('api/ActorAll', ViewsForActor.AllActor.as_view()),
    path('Actor/refactor/<int:pk>/', ViewsForActor.AllActor.as_view()),
    path('Actor/delete/<int:pk>/', ViewsForActor.AllActor.as_view()),
    path('api/Actor/GetId/<int:pk>/', ViewsForActor.getWithId),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)