from django.urls import path

from app.main_screen.views import HomeScreenView, CreatePollViews, CheckPollView, IntermediateListView
urlpatterns = [
    path('', HomeScreenView.as_view(), name='home_page'),
    path('create_poll/', CreatePollViews.as_view(), name='create_poll'),
    path('list_poll/<int:id_theam>/', CheckPollView.as_view(), name='list_poll'),
    path('chose_team/', IntermediateListView.as_view(), name='chose_team'),
]
