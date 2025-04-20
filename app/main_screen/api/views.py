
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from app.main_screen.models import ListNewsModel, CustomUserModel, TopicNameModel, PollInfoModel
from .serializers import ListNewsSerializer, CustomUserSerializer, TopicNameSerializer, PollInfoSerializer



class ListNewsListAPIView(generics.ListAPIView):
    queryset = ListNewsModel.objects.all()
    serializer_class = ListNewsSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Получить новость
class ListNewsDetailAPIView(generics.RetrieveAPIView):
    queryset = ListNewsModel.objects.all()
    serializer_class = ListNewsSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам
    lookup_field = 'id'


# Создать новость
class ListNewsCreateAPIView(generics.CreateAPIView):
    queryset = ListNewsModel.objects.all()
    serializer_class = ListNewsSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Обновить новость
class ListNewsUpdateAPIView(generics.UpdateAPIView):
    queryset = ListNewsModel.objects.all()
    serializer_class = ListNewsSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Удалить новость
class ListNewsDeleteAPIView(generics.DestroyAPIView):
    queryset = ListNewsModel.objects.all()
    serializer_class = ListNewsSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Список пользователей
class CustomUserListAPIView(generics.ListAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Получить пользователя
class CustomUserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Список тем
class TopicNameListAPIView(generics.ListAPIView):
    queryset = TopicNameModel.objects.all()
    serializer_class = TopicNameSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Получить тему
class TopicNameDetailAPIView(generics.RetrieveAPIView):
    queryset = TopicNameModel.objects.all()
    serializer_class = TopicNameSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Список опросов
class PollInfoListAPIView(generics.ListAPIView):
    queryset = PollInfoModel.objects.all()
    serializer_class = PollInfoSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Получить опрос
class PollInfoDetailAPIView(generics.RetrieveAPIView):
    queryset = PollInfoModel.objects.all()
    serializer_class = PollInfoSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Создать опрос
class PollInfoCreateAPIView(generics.CreateAPIView):
    queryset = PollInfoModel.objects.all()
    serializer_class = PollInfoSerializer
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Обновить опрос
class PollInfoUpdateAPIView(generics.UpdateAPIView):
    queryset = PollInfoModel.objects.all()
    serializer_class = PollInfoSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам


# Удалить опрос
class PollInfoDeleteAPIView(generics.DestroyAPIView):
    queryset = PollInfoModel.objects.all()
    serializer_class = PollInfoSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]  # Разрешаем доступ только админам
