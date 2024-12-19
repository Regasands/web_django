from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group

from app.main_screen.forms import PollCreateForm
from app.main_screen.models import ListNewsModel, PollInfoModel, CustomUserModel, TopicNameModel

# Create your views here.

class HomeScreenView(PermissionRequiredMixin, ListView):
    model = ListNewsModel
    permission_required = 'main_screen.view_listnewsmodel'

class CreateUsersView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main_screen/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        CustomUserModel.objects.create(profile=user)
        group = Group.objects.get(name='User')
        if group:
            group.user_set.add(user)
        return super().form_valid(form)

class CreatePollViews(PermissionRequiredMixin, CreateView):
    form_class = PollCreateForm
    success_url = reverse_lazy('home_page')
    template_name = 'main_screen/create_poll.html'
    permission_required = 'main_screen.add_pollinfomodel'

    def form_valid(self, form):
        form.instance.user_create = self.request.user.custom_user
        my_dicters = {}
        for index, value in enumerate(self.request.POST.getlist('additional_input', '')):
            my_dicters[f'{index}. {value}'] = 0
        form.instance.json_variants = my_dicters
        return super().form_valid(form)

class IntermediateListView(PermissionRequiredMixin, ListView):
    model = TopicNameModel
    permission_required = 'main_screen.view_topicnamemodel'
    

class CheckPollView(PermissionRequiredMixin, ListView):
    permission_required = 'main_screen.view_pollinfomodel'
    model = PollInfoModel

    def get_queryset(self):
        index_poll = self.kwargs.get('id_theam')
        obj = self.request.user.custom_user.poll_status
        print(obj)
        return super().get_queryset().exclude(pk__in=obj)