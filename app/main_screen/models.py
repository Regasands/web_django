from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
TYPES_CHOICES = [
    ('POLL', 'Опрос'),
    ('multi_poll', 'Голосование')
]

class ListNewsModel(models.Model):
    name = models.CharField(verbose_name='Заголовок', max_length=255)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание новости')
    image = models.ImageField(upload_to='news_images/', verbose_name='Изображение', blank=True, null=True)
    describe = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Данные Новости'
        verbose_name_plural = 'Данные Новостей'
        ordering = ['-date']

    def __str__(self):
        return self.name

class CustomUserModel(models.Model):
    money = models.IntegerField(verbose_name='Монеты пользователя', default=0)
    poll_status = models.ManyToManyField('PollInfoModel', verbose_name='Пройденные опросы', blank=True, related_name='users_accept_poll')
    date_register = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    profile = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Профиль', related_name='custom_user')

    class Meta:
        ordering = ['-date_register']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.profile} {self.money}'

    @staticmethod
    def get_or_create_profile(user):
        profile, created = CustomUserModel.objects.get_or_create(profile=user)
        return profile

class TopicNameModel(models.Model):
    name_topic = models.CharField(verbose_name='Название темы', max_length=255)
    vote = models.IntegerField(verbose_name='Голоса за эту тему', default=0)
    descript = models.TextField(verbose_name='Описание темы', blank=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Все возможные темы'

    def __str__(self):
        return f'{self.name_topic}'

class PollInfoModel(models.Model):
    types = models.CharField(choices=TYPES_CHOICES, verbose_name='Тип опроса', max_length=255)
    poll_name = models.CharField(verbose_name='Имя опроса', max_length=255)
    topic = models.ForeignKey(
        TopicNameModel,
        on_delete=models.CASCADE,
        related_name='pools',
        verbose_name='Тема'
    )
    user_create = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Создатель опроса',
    )
    vote = models.IntegerField(default=0, verbose_name='Кол-во голосов на данный момент')
    max_vote = models.IntegerField(verbose_name='Кол-во голосов до закрытия опроса')
    status = models.BooleanField(verbose_name='Состояние', default=True, blank=True)
    json_variants = models.JSONField(verbose_name='Варианты ответа', blank=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Все возможные опросы'
        ordering = ['-status', 'max_vote']

    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.poll_name}'
