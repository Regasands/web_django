from django.contrib import admin
from django.urls import path

from app.main_screen.views import HomeScreenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeScreenView.as_view(), name='home_screen')
]
