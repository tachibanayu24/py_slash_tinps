from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('post/', include('post.urls')),
    path('user/', include('user.urls')),
    path('tinps/', include('tinps.urls')),
]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
