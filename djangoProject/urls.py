from django.contrib import admin
from django.urls import path, include
from devops import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include(urls))
]
