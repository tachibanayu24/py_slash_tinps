from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('post/', include('post.urls')),
    path('user/', include('user.urls')),
    path('tinps/', include('tinps.urls')),
]
