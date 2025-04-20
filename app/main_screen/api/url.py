
from django.urls import path
from app.main_screen.api.views import ListNewsListAPIView, ListNewsDetailAPIView, ListNewsCreateAPIView, ListNewsUpdateAPIView, ListNewsDeleteAPIView
from app.main_screen.api.views  import CustomUserListAPIView, CustomUserDetailAPIView
from app.main_screen.api.views import TopicNameListAPIView, TopicNameDetailAPIView
from app.main_screen.api.views import PollInfoListAPIView, PollInfoDetailAPIView, PollInfoCreateAPIView, PollInfoUpdateAPIView, PollInfoDeleteAPIView
urlpatterns = [
    # Новости
    path('news/', ListNewsListAPIView.as_view(), name='news-list'),
    path('news/<int:id>/', ListNewsDetailAPIView.as_view(), name='news-detail'),
    path('news/create/', ListNewsCreateAPIView.as_view(), name='news-create'),
    path('news/update/<int:id>/', ListNewsUpdateAPIView.as_view(), name='news-update'),
    path('news/delete/<int:id>/', ListNewsDeleteAPIView.as_view(), name='news-delete'),

    # Пользователи
    path('users/', CustomUserListAPIView.as_view(), name='user-list'),
    path('users/<int:id>/', CustomUserDetailAPIView.as_view(), name='user-detail'),

    # Темы
    path('topics/', TopicNameListAPIView.as_view(), name='topic-list'),
    path('topics/<int:id>/', TopicNameDetailAPIView.as_view(), name='topic-detail'),

    # Опросы
    path('polls/', PollInfoListAPIView.as_view(), name='poll-list'),
    path('polls/<int:id>/', PollInfoDetailAPIView.as_view(), name='poll-detail'),
    path('polls/create/', PollInfoCreateAPIView.as_view(), name='poll-create'),
    path('polls/update/<int:id>/', PollInfoUpdateAPIView.as_view(), name='poll-update'),
    path('polls/delete/<int:id>/', PollInfoDeleteAPIView.as_view(), name='poll-delete'),
]

