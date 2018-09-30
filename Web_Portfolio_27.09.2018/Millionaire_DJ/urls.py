from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('web.url')),
    path('admin/', admin.site.urls),
]
