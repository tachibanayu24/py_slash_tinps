from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('user/', include('users.urls')),
    path('tinps/', include('tinps.urls')),
    path('accounts/', include('allauth.urls')),
    path('home', include('home.urls')),
    path('', include('home.urls')),
]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
