"""
Root GymStrength URL dispatcher. Handles all REST API requests.
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('api/gym/', include('api.gymapp.urls', namespace='gym')),
    path('api/admin/', admin.site.urls),
    # path('api/auth/', include('api.authapp.urls', namespace='auth')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
