from django.urls import path

from app.main_screen.views import HomeScreenView, CreatePollViews
urlpatterns = [
    path('',HomeScreenView.as_view(), name='home_page'),
    path('creat_poll', CreatePollViews.as_view(), name='create_poll')
]