from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from app.main_screen.views import HomeScreenView, CreatePollViews, CheckPollView, IntermediateListView, CheckProfile, PollDetail

urlpatterns = [
    path('', HomeScreenView.as_view(), name='home_page'),
    path('create_poll/', CreatePollViews.as_view(), name='create_poll'),
    path('list_poll/<int:id_theam>/', CheckPollView.as_view(), name='list_poll'),
    path('chose_team/', IntermediateListView.as_view(), name='chose_team'),
    path('profile/', CheckProfile.as_view(), name='profile'),
    path('poll_info/<int:pk>/', PollDetail.as_view(), name='poll_detail'),
    path('api/', include('app.main_screen.api.url')),  # Подключаем API
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
