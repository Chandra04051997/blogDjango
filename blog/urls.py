from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import HomeListView
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeListView.as_view(), name='home'),
    path('<int:page>',HomeListView.as_view(), name='home'),
    path('artikel/', include('artikel.urls', namespace='artikel')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)