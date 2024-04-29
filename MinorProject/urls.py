from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to ___ Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login', include('home.urls')),
    path('home', include('home.urls')),
    path('book', include('home.urls')),
    path('docLogin', include('home.urls')),
    path('register', include('home.urls')),
    path('docRegis', include('home.urls')),
    path('manage', include('home.urls')),
]
