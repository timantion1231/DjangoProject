from django.contrib import admin
from django.urls import path, include
from .views import redirect_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('blog.urls'), name='home'),
    path('', redirect_home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls'), name = 'users_url')
]
