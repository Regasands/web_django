from django.contrib import admin
from app.main_screen.models import *
# Register your models here.
sp = [ListNewsModel, CustomUserModel, TopicNameModel, PollInfoModel, ]
for e in sp:
    admin.site.register(e)