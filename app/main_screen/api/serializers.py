from rest_framework import serializers
from ..models import ListNewsModel, CustomUserModel, PollInfoModel, TopicNameModel


class ListNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNewsModel
        fields = ['id', 'name', 'describe', 'date', 'image']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'money', 'poll_status', 'date_register', 'profile']

class TopicNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicNameModel
        fields = ['id', 'name_topic', 'vote', 'descript']

class PollInfoSerializer(serializers.ModelSerializer):
    topic = TopicNameSerializer()  # Включаем тему
    user_create = CustomUserSerializer()  # Включаем создателя опроса

    class Meta:
        model = PollInfoModel
        fields = ['id', 'types', 'poll_name', 'topic', 'user_create', 'vote', 'max_vote', 'status', 'json_variants']

