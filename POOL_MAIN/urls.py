from django.contrib import admin
from django.urls import path, include

from app.main_screen.views import HomeScreenView, CreateUsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.main_screen.url')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/register/', CreateUsersView.as_view(), name='register')
]
